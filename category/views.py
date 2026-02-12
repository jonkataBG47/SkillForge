from django.shortcuts import render,redirect,get_object_or_404
from category.models import Category
from django.db.models import Count
from category.forms import FormCategory
from django.http import HttpRequest, HttpResponse
from core.forms import SearchForm
from django.db.models import Q
def create_category(request:HttpRequest):
    form = FormCategory(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('category_list')
    context = {'form':form}
    return render(request,'category/category_create.html',context)
def update_category(request:HttpRequest,id):
    category = get_object_or_404(Category,id=id)
    form = FormCategory(request.POST or None,instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('category_list')
    context = {'form':form,'category':category}
    return render(request,'category/category_update.html',context)
def delete_category(request:HttpRequest,id):
    category = get_object_or_404(Category,id=id)
    form = FormCategory(instance=category)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    context = {'form':form,'category':category}
    return render(request,'category/category_delete_confirm.html',context)
def category_list(request:HttpRequest):
    form = SearchForm(request.GET or None)
    categories = Category.objects.annotate(count_skill=Count('skills')).order_by('-updated_at','name')
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data['query']
        categories = Category.objects.annotate(count_skill=Count('skills')).filter(name__icontains=query).order_by('-updated_at','name')
    context = {'form':form,'categories':categories}
    return render(request,'category/category_list.html',context)
def category_detail(request:HttpResponse,slug):
    category = get_object_or_404(Category.objects.annotate(count_skill=Count('skills')).prefetch_related('skills'),slug=slug)
    skills = category.skills.all().order_by('-updated_at','title')
    context = {'category':category,'skills':skills}
    return render(request,'category/category_detail.html',context)
