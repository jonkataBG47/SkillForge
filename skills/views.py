from django.shortcuts import render,redirect
from skills.models import Skill
from django.db.models import Count
from skills.forms import FormSkill
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
def add_skill(request:HttpRequest):
    form = FormSkill(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,'skill_create.html',context)
def update_skill(request:HttpRequest,id):
    post = get_object_or_404(Skill,id=id)
    form = FormSkill(request.POST or None,isinstance = post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'skill_update.html',context)
def remove_skill(request:HttpRequest,id):
    post = get_object_or_404(Skill,id=id)
    form = FormSkill(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'skill_delete_confirm.html',context)
def skill_list(request:HttpRequest):
    skill = Skill.objects.all()
    context = {'skill':skill}
    return render(request,'skill_list.html',context)
def skill_detail(request:HttpRequest,slug):
    skill = get_object_or_404(Skill.objects.prefetch_related('resources'),slug=slug)
    context = {'skill':skill}
    return render(request,'skill_detail.html',context)

