from django.urls import path, include
from learning_paths import views
urlpatterns = [
    path('paths/',include([
        path('',views.path_list,name='path_list'),
        path('create/',views.create_path,name='create_path'),
        path('update/<int:id>/',views.update_path,name='update_path'),
        path('delete/<int:id>/',views.delete_path,name='delete_path'),
        path('<slug:slug>/',views.path_detail,name='path_detail'),
    ])),
]
