from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from skills.models import Skill
from skills.forms import FormSkill
from django.db.models import Q
from core.forms import SearchForm
from django.urls import reverse_lazy
class CreateSkillView(LoginRequiredMixin,CreateView):
    model = Skill
    form_class = FormSkill
    template_name = 'skills/skill_create.html'
    success_url = reverse_lazy('skill_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
class UpdateSkillView(LoginRequiredMixin,UpdateView):
    model = Skill
    form_class = FormSkill
    template_name = 'skills/skill_update.html'
    success_url = reverse_lazy('skill_list')
    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)
class DeleteSkillView(LoginRequiredMixin,DeleteView):
    model = Skill
    template_name = 'skills/skill_delete_confirm.html'
    success_url = reverse_lazy('skill_list')
    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)
class SkillListView(LoginRequiredMixin,ListView):
    model = Skill
    template_name = 'skills/skill_list.html'
    context_object_name = 'skills'
    def get_queryset(self):
        skills = Skill.objects.filter(user=self.request.user).order_by('-updated_at','title')
        self.form = SearchForm(self.request.GET or None)
        if self.form.is_valid():
            query = self.form.cleaned_data['query']
            filters = Q(title__icontains=query) | Q(category__name__icontains = query)
            skills = skills.filter(filters)
        return skills
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
class SkillDetailView(LoginRequiredMixin,DetailView):
    model = Skill
    template_name = 'skills/skill_detail.html'
    context_object_name = 'skill'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user).prefetch_related('resources')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources'] = self.object.resources.all().order_by('-updated_at','title')
        return context

