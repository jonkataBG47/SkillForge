from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from learning_paths.models import LearningPath
from django.db.models import Count
from learning_paths.forms import FormLearningPaths
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from core.forms import SearchForm
class CreatePathView(LoginRequiredMixin,CreateView):
    model = LearningPath
    form_class = FormLearningPaths
    template_name = 'learning_paths/path_create.html'
    success_url = reverse_lazy('path_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
# def create_path(request:HttpRequest):
#     form = FormLearningPaths(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('path_list')
#     context = {'form':form}
#     return render(request,'learning_paths/path_create.html',context)
class UpdatePathView(LoginRequiredMixin,UpdateView):
    model = LearningPath
    form_class = FormLearningPaths
    template_name = 'learning_paths/path_update.html'
    success_url = reverse_lazy('path_list')
    def get_queryset(self):
        return LearningPath.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['path'] = self.object
        return context
# def update_path(request:HttpRequest,id):
#     path = get_object_or_404(LearningPath,id=id)
#     form = FormLearningPaths(request.POST or None,instance=path)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('path_list')
#     context = {'form':form,'path':path}
#     return render(request,'learning_paths/path_update.html',context)
class DeletePathView(LoginRequiredMixin,DeleteView):
    model = LearningPath
    template_name = 'learning_paths/path_delete_confirm.html'
    success_url = reverse_lazy('path_list')
    def get_queryset(self):
        return LearningPath.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['path'] = self.object
        return context
# def delete_path(request:HttpRequest,id):
#     path = get_object_or_404(LearningPath,id=id)
#     form = FormLearningPaths(instance=path)
#     if request.method == 'POST':
#         path.delete()
#         return redirect('path_list')
#     context = {'form':form,'path':path}
#     return render(request,'learning_paths/path_delete_confirm.html',context)
class PathListView(LoginRequiredMixin,ListView):
    model = LearningPath
    template_name = 'learning_paths/path_list.html'
    context_object_name = 'paths'
    def get_queryset(self):
        paths = LearningPath.objects.filter(user=self.request.user).order_by('-updated_at','title')
        self.form = SearchForm(self.request.GET or None)
        if self.form.is_valid():
            query = self.form.cleaned_data['query']
            paths = paths.filter(title__icontains=query)
        return paths
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
# def path_list(request:HttpRequest):
#     form = SearchForm(request.GET or None)
#     paths = LearningPath.objects.all().order_by('-updated_at','title')
#     if request.method == 'GET' and form.is_valid():
#         query = form.cleaned_data['query']
#         paths = LearningPath.objects.filter(title__icontains=query)
#     context = {'form':form,'paths':paths}
#     return render(request,'learning_paths/path_list.html',context)
class PathDetailView(LoginRequiredMixin,DetailView):
    model = LearningPath
    template_name = 'learning_paths/path_detail.html'
    context_object_name = 'path'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_queryset(self):
        return LearningPath.objects.filter(user=self.request.user).annotate(count_skills = Count('skills'))
# def path_detail(request:HttpRequest,slug):
#     path = get_object_or_404(LearningPath.objects.annotate(count_skills = Count('skills')),slug=slug)
#     context = {'path':path}
#     return render(request,'learning_paths/path_detail.html',context)
