from django.shortcuts import render,redirect,get_object_or_404
from resources.models import Resource
from django.db.models import Count
from resources.forms import FormResource
from django.http import HttpRequest, HttpResponse
def create_resource(request:HttpRequest):
    form = FormResource(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('resource_list')
    context = {'form':form}
    return render(request,'resources/resource_create.html',context)
def update_resource(request:HttpRequest,id):
    resource = get_object_or_404(Resource,id=id)
    form = FormResource(request.POST or None,instance=resource)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('resource_list')
    context = {'form':form,'resource':resource}
    return render(request,'resources/resource_update.html',context)
def delete_resource(request:HttpRequest,id):
    resource = get_object_or_404(Resource,id=id)
    form = FormResource(instance=resource)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    context = {'form':form,'resource':resource}
    return render(request,'resources/resource_delete_confirm.html',context)
def resource_list(request:HttpRequest):
    resources = Resource.objects.all().order_by('-created_at','title')
    context = {'resources':resources}
    return render(request,'resources/resource_list.html',context)
def resource_detail(request:HttpRequest,slug):
    resource = get_object_or_404(Resource,slug=slug)
    skills = resource.skills.all().order_by('-created_at','title')
    context = {'resource':resource,'skills':skills}
    return render(request,'resources/resource_detail.html',context)

