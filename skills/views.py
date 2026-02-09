from django.shortcuts import render,redirect
from skills.models import Skill
from django.db.models import Count
from skills.forms import FormSkill,SearchForm
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
def create_skill(request:HttpRequest):
    form = FormSkill(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,'skills/skill_create.html',context)
def update_skill(request:HttpRequest,id):
    skill = get_object_or_404(Skill,id=id)
    form = FormSkill(request.POST or None,instance = skill)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form,'skill':skill}
    return render(request,'skills/skill_update.html',context)
def delete_skill(request:HttpRequest,id):
    skill = get_object_or_404(Skill,id=id)
    form = FormSkill(instance=skill)
    if request.method == 'POST':
        skill.delete()
        return redirect('home')
    context = {'form':form,'skill':skill}
    return render(request,'skills/skill_delete_confirm.html',context)
def skill_list(request:HttpRequest):
    form = SearchForm(request.GET or None)
    skills = Skill.objects.all()
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data['query']
        filters = Q(title__icontains=query) | Q(category__name__icontains = query)
        skills = Skill.objects.filter(filters)
    context = {'form':form,'skills':skills}
    return render(request,'skills/skill_list.html',context)
def skill_detail(request:HttpRequest,slug):
    skill = get_object_or_404(Skill.objects.prefetch_related('resources'),slug=slug)
    resources = skill.resources.all()
    context = {'skill':skill,'resources':resources}
    return render(request,'skills/skill_detail.html',context)

