from django.urls import path,include
from resources import views
urlpatterns = [
    path('resources/',include([
        path('', views.ResourceListView.as_view(), name='resource_list'),
        path('create/', views.CreateResourceView.as_view(), name='create_resource'),
        path('<int:pk>/update/', views.UpdateResourceView.as_view(), name='update_resource'),
        path('<int:pk>/delete/', views.DeleteResourceView.as_view(), name='delete_resource'),
        path('<slug:slug>/', views.ResourceDetailView.as_view(), name='resource_detail')
    ]))
]
