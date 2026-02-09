from django.urls import path,include
from skills import views
urlpatterns = [
    path('skills/',include([
        path('',views.skill_list, name='skill_list'),
        path('create/', views.create_skill, name='create_skill'),
        path('<int:id>/update/', views.update_skill, name='update_skill'),
        path('<int:id>/delete/', views.delete_skill, name='delete_skill'),
        path('<slug:slug>/', views.skill_detail, name='skill_detail')
    ])),
]
