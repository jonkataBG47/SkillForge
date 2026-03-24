from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RegistrationForm, UpdateProfileForm

User = get_user_model()
class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
    def get_object(self, queryset=None):
        return self.request.user
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')
    def get_object(self, queryset=None):
        return self.request.user
class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('home')
    def get_object(self, queryset=None):
        return self.request.user