from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from resources.models import Resource
from resources.forms import FormResource
from django.http import HttpRequest
from core.forms import SearchForm
class CreateResourceView(LoginRequiredMixin,CreateView):
    model = Resource
    form_class = FormResource
    template_name = 'resources/resource_create.html'
    success_url = reverse_lazy('resource_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
# def create_resource(request:HttpRequest):
#     form = FormResource(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('resource_list')
#     context = {'form':form}
#     return render(request,'resources/resource_create.html',context)
class UpdateResourceView(LoginRequiredMixin,UpdateView):
    model = Resource
    form_class = FormResource
    template_name = 'resources/resource_update.html'
    success_url = reverse_lazy('resource_list')
    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user)
# def update_resource(request:HttpRequest,id):
#     resource = get_object_or_404(Resource,id=id)
#     form = FormResource(request.POST or None,instance=resource)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('resource_list')
#     context = {'form':form,'resource':resource}
#     return render(request,'resources/resource_update.html',context)
class DeleteResourceView(LoginRequiredMixin,DeleteView):
    model = Resource
    template_name = 'resources/resource_delete_confirm.html'
    success_url = reverse_lazy('resource_list')
    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user)
# def delete_resource(request:HttpRequest,id):
#     resource = get_object_or_404(Resource,id=id)
#     form = FormResource(instance=resource)
#     if request.method == 'POST':
#         resource.delete()
#         return redirect('resource_list')
#     context = {'form':form,'resource':resource}
#     return render(request,'resources/resource_delete_confirm.html',context)
class ResourceListView(LoginRequiredMixin,ListView):
    model = Resource
    template_name = 'resources/resource_list.html'
    context_object_name = 'resources'
    def get_queryset(self):
        resources = Resource.objects.filter(user=self.request.user).order_by('-updated_at','title')
        self.form = SearchForm(self.request.GET or None)
        if self.form.is_valid():
            query = self.form.cleaned_data['query']
            resources = resources.filter(title__icontains=query)
        return resources
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
# def resource_list(request:HttpRequest):
#     form = SearchForm(request.GET or None)
#     resource = Resource.objects.all().order_by('-updated_at','title')
#     if request.method == 'GET' and form.is_valid():
#         query = form.cleaned_data['query']
#         resource = Resource.objects.filter(title__icontains=query)
#     context = {'form':form,'resources':resource}
#     return render(request,'resources/resource_list.html',context)
class ResourceDetailView(LoginRequiredMixin,DetailView):
    model = Resource
    template_name = 'resources/resource_detail.html'
    context_object_name = 'resource'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_queryset(self):
        return Resource.objects.filter(user=self.request.user).prefetch_related('skills')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = self.object.skills.all().order_by('-updated_at','title')
        return context
# def resource_detail(request:HttpRequest,slug):
#     resource = get_object_or_404(Resource,slug=slug)
#     skills = resource.skills.all().order_by('-updated_at','title')
#     context = {'resource':resource,'skills':skills}
#     return render(request,'resources/resource_detail.html',context)

