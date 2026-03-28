from django.urls import path,include
from skills import views
from skills import api_views
urlpatterns = [
    path('skills/',include([
        path('',views.SkillListView.as_view(), name='skill_list'),
        path('create/', views.CreateSkillView.as_view(), name='create_skill'),
        path('<int:pk>/update/', views.UpdateSkillView.as_view(), name='update_skill'),
        path('<int:pk>/delete/', views.DeleteSkillView.as_view(), name='delete_skill'),
        path('<slug:slug>/', views.SkillDetailView.as_view(), name='skill_detail'),
    ])),
    path('api/skills/',api_views.SkillApiView.as_view(), name='api_skill_list'),
]
