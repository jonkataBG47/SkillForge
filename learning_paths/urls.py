from django.urls import path, include
from learning_paths import views
urlpatterns = [
    path('paths/',include([
        path('',views.PathListView.as_view(),name='path_list'),
        path('create/',views.CreatePathView.as_view(),name='create_path'),
        path('update/<int:pk>/',views.UpdatePathView.as_view(),name='update_path'),
        path('delete/<int:pk>/',views.DeletePathView.as_view(),name='delete_path'),
        path('<slug:slug>/',views.PathDetailView.as_view(),name='path_detail'),
    ])),
]
