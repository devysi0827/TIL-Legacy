from django.urls import path
from . import views

urlpatterns = [
    #전체조회
    path('', views.index, name = 'index'),
    #단일조히
    
    path('<int:pk>/',views.detail, name= 'detail'),
    #생성준비단계
    
    path('new/', views.new, name= 'new'),

    path('create/', views.create, name= 'create')
]
