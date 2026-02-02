from django.shortcuts import render,redirect,get_object_or_404
from category.models import Category
from django.db.models import Count
from category.forms import FormCategory
from django.http import HttpRequest, HttpResponse
def add_category(request:HttpRequest):
    form = FormCategory(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form}
    return render(request,'category_create.html',context)
def update_category(request:HttpRequest,id):
    post = get_object_or_404(Category,id=id)
    form = FormCategory(request.POST or None,instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'category_update.html',context)
def remove_category(request:HttpRequest,id):
    post = get_object_or_404(Category,id=id)
    form = FormCategory(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {'form':form,'post':post}
    return render(request,'category_delete_confirm.html',context)
def category_list(request:HttpRequest):
    category = Category.objects.annotate(count_skill=Count('skills')).order_by('-count_skill','name')
    context = {'category':category}
    return render(request,'category_list.html',context)
def category_detail(request:HttpResponse,slug):
    category = get_object_or_404(Category.objects.prefetch_related('skills'),slug=slug)
    context = {'category':category}
    return render(request,'category_detail.html',context)
