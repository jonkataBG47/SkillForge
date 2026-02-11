from django.urls import path,include
from resources import views
urlpatterns = [
    path('resources/',include([
        path('', views.resource_list, name='resource_list'),
        path('create/', views.create_resource, name='create_resource'),
        path('<int:id>/update/', views.update_resource, name='update_resource'),
        path('<int:id>/delete/', views.delete_resource, name='delete_resource'),
        path('<slug:slug>/', views.resource_detail, name='resource_detail')
    ]))
]
