from django.urls import path, include
from category import views
urlpatterns = [
    path('categories/', include([
        path('', views.CategoryListView.as_view(), name='category_list'),
        path('create/', views.CreateCategoryView.as_view(), name='create_category'),
        path('<int:pk>/update/', views.UpdateCategoryView.as_view(), name='update_category'),
        path('<int:pk>/delete/', views.DeleteCategoryView.as_view(), name='delete_category'),
        path('<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail')
    ])),
]
