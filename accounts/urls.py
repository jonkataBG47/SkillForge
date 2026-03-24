from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('login/',LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user = True), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'home'), name='logout'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/update/', views.UpdateProfileView.as_view(), name='profile_update'),
    path('profile/delete/', views.DeleteProfileView.as_view(), name='profile_delete'),
]
