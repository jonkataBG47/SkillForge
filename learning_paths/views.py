from django.shortcuts import render,redirect
from learning_paths.models import LearningPath
from django.db.models import Count
from learning_paths.forms import FormLearningPaths
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from core.forms import SearchForm
def create_path(request:HttpRequest):
    form = FormLearningPaths(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('path_list')
    context = {'form':form}
    return render(request,'learning_paths/path_create.html',context)
def update_path(request:HttpRequest,id):
    path = get_object_or_404(LearningPath,id=id)
    form = FormLearningPaths(request.POST or None,instance=path)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('path_list')
    context = {'form':form,'path':path}
    return render(request,'learning_paths/path_update.html',context)
def delete_path(request:HttpRequest,id):
    path = get_object_or_404(LearningPath,id=id)
    form = FormLearningPaths(instance=path)
    if request.method == 'POST':
        path.delete()
        return redirect('path_list')
    context = {'form':form,'path':path}
    return render(request,'learning_paths/path_delete_confirm.html',context)
def path_list(request:HttpRequest):
    form = SearchForm(request.GET or None)
    path = LearningPath.objects.all().order_by('-updated_at','title')
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data['query']
        path = LearningPath.objects.filter(title__icontains=query)
    context = {'form':form,'path':path}
    return render(request,'learning_paths/path_list.html',context)
def path_detail(request:HttpRequest,slug):
    path = get_object_or_404(LearningPath.objects.annotate(count_skills = Count('skills')),slug=slug)
    context = {'path':path}
    return render(request,'learning_paths/path_detail.html',context)
