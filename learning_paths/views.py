from django.shortcuts import render,redirect
from learning_paths.models import LearningPath
from django.db.models import Count
from learning_paths.forms import FormLearningPaths
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
def create_path(request:HttpRequest):
    form = FormLearningPaths(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,'path_create.html',context)
def update_path(request:HttpRequest,id):
    post = get_object_or_404(LearningPath,id=id)
    form = FormLearningPaths(request.POST or None,instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'path_update.html',context)
def remove_path(request:HttpRequest,id):
    post = get_object_or_404(LearningPath,id=id)
    form = FormLearningPaths(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'path_delete_confirm.html',context)
def path_list(request:HttpRequest):
    path = LearningPath.objects.all()
    context = {'path':path}
    return render(request,'path_list.html',context)
def path_detail(request:HttpRequest,slug):
    path = get_object_or_404(LearningPath,slug=slug)
    context = {'path':path}
    return render(request,'path_detail.html',context)
