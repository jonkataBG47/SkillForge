from django.urls import path, include
from category import views
urlpatterns = [
    path('categories/', include([
        path('', views.category_list, name='category_list'),
        path('create/', views.create_category, name='create_category'),
        path('<int:id>/update/', views.update_category, name='update_category'),
        path('<int:id>/delete/', views.delete_category, name='delete_category'),
        path('<slug:slug>/', views.category_detail, name='category_detail')
    ])),
]
