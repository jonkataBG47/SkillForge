from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','image']
# class DeleteUserForm(forms.ModelForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if not self.user.check_password(password):
#             raise forms.ValidationError("Incorrect password.")
#         return password