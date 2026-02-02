from django.shortcuts import render,redirect,get_object_or_404
from resources.models import Resource
from django.db.models import Count
from resources.forms import FormResource
from django.http import HttpRequest, HttpResponse
def add_resource(request:HttpRequest):
    form = FormResource(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,'resource_create.html',context)
def update_skill(request:HttpRequest,id):
    post = get_object_or_404(Resource,id=id,instance=post)
    form = FormResource(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'resource_update.html',context)
def remove_skill(request:HttpRequest,id):
    post = get_object_or_404(Resource,id=id)
    form = FormResource(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'resource_delete_confirm.html',context)
def resource_list(request:HttpRequest):
    resourse = Resource.objects.all().order_by('title')
    context = {'resourse':resourse}
    return render(request,'resource_list.html',context)
def resource_detail(request:HttpRequest,slug):
    resource = get_object_or_404(Resource,slug=slug)
    context = {'resource':resource}
    return render(request,'resource_detail.html',context)

