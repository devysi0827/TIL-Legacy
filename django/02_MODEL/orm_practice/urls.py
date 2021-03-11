from django.urls import path
from . import views

# practice/
urlpatterns = [
    # practice/'' => 목록 보여주기 HTML(전체 조회)
    path('', views.index, name='index'),
    # practice/1/ => 1번 학생 정보 보여주기 HTML(단일 조회)
    path('<int:pk>/', views.detail, name='detail'),
    # practice/new/ => 새로운 데이터 입력용 HTML(생성 준비단계)
    path('new/', views.new, name='new'),
    # practice/create/ => 사용자 입력 데이터 처리
    path('create/', views.create, name='create'),

    path('<int:pk>', views.edit, name='edit'),
    path('<int:pk>', views.update, name='update'),
    path('<int:pk>', views.delete, name='delete')
]


#pratice/1/edit => 특정데이터에 대한 정보를 url을 가지고 있어야함
#pratice/   -> 공백
