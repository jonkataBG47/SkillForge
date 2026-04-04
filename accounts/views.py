from django.contrib import messages
from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

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
class DeleteProfileView(LoginRequiredMixin, FormView):
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('home')
    form_class = AuthenticationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = self.request.POST or None
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        logout(self.request)
        user.delete()
        messages.success(self.request, 'Profile deleted successfully.')
        return redirect(self.success_url)