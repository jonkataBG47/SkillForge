from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name','phone_number']
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phone_number','image']