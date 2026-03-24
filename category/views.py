from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from rest_framework.reverse import reverse_lazy

from category.models import Category
from django.db.models import Count
from category.forms import FormCategory
from django.http import HttpRequest, HttpResponse
from core.forms import SearchForm
class CreateCategoryView(LoginRequiredMixin,CreateView):
    model = Category
    form_class = FormCategory
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('category_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# def create_category(request:HttpRequest):
#     form = FormCategory(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('category_list')
#     context = {'form':form}
#     return render(request,'category/category_create.html',context)
class UpdateCategoryView(LoginRequiredMixin,UpdateView):
    model = Category
    form_class = FormCategory
    template_name = 'category/category_update.html'
    success_url = reverse_lazy('category_list')
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
# def update_category(request:HttpRequest,id):
#     category = get_object_or_404(Category,id=id)
#     form = FormCategory(request.POST or None,instance=category)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('category_list')
#     context = {'form':form,'category':category}
#     return render(request,'category/category_update.html',context)
class DeleteCategoryView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = 'category/category_delete_confirm.html'
    success_url = reverse_lazy('category_list')
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
# def delete_category(request:HttpRequest,id):
#     category = get_object_or_404(Category,id=id)
#     form = FormCategory(instance=category)
#     if request.method == 'POST':
#         category.delete()
#         return redirect('category_list')
#     context = {'form':form,'category':category}
#     return render(request,'category/category_delete_confirm.html',context)
class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    def get_queryset(self):
        categories = Category.objects.annotate(count_skill=Count('skills')).filter(user = self.request.user).order_by('-updated_at','name')
        self.form = SearchForm(self.request.GET or None)
        if self.form.is_valid():
            query = self.form.cleaned_data['query']
            categories = Category.objects.annotate(count_skill=Count('skills')).filter(name__icontains=query)
        return categories
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
# def category_list(request:HttpRequest):
#     form = SearchForm(request.GET or None)
#     categories = Category.objects.annotate(count_skill=Count('skills')).order_by('-updated_at','name')
#     if request.method == 'GET' and form.is_valid():
#         query = form.cleaned_data['query']
#         categories = Category.objects.annotate(count_skill=Count('skills')).filter(name__icontains=query)
#     context = {'form':form,'categories':categories}
#     return render(request,'category/category_list.html',context)
class CategoryDetailView(LoginRequiredMixin,DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_queryset(self):
        return Category.objects.annotate(count_skill=Count('skills')).prefetch_related('skills').filter(user = self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = self.object.skills.all().order_by('-updated_at','title')
        return context
# def category_detail(request:HttpRequest,slug):
#     category = get_object_or_404(Category.objects.annotate(count_skill=Count('skills')).prefetch_related('skills'),slug=slug)
#     skills = category.skills.all().order_by('-updated_at','title')
#     context = {'category':category,'skills':skills}
#     return render(request,'category/category_detail.html',context)
