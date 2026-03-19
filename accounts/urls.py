from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user = True), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'home'), name='logout'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile_detail'),
]
