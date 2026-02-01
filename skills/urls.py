from django.urls import path,include
from skills import views
urlpatterns = [
    path('categories/',include([
        path('',views.categories_list,name='categories_list'),
        path('<slug:slug>/',views.categories_detail,name='category_detail'),
    ])),
    path('skills/',include([
        path('',views.skill_list,name='skill_list'),
        path('<slug:slug>/',views.skill_detail,name='skill_detail'),
    ])),
]
