from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import RegistrationForm

User = get_user_model()
class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
    def get_object(self, queryset=None):
        return self.request.user