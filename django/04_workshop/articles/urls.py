from django.urls import path
from . import views

urlpatterns = [
   
    path('<title>/',views.detail, name= 'detail'), #int:pk

    path('', views.index, name = 'index'),
    
    
   
    path('new/', views.new, name= 'new'),

    path('create/', views.create, name= 'create')
]
