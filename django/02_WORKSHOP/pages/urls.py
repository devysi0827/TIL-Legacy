from django.urls import path
from . import views

urlpatterns = [
    path('dinner/<menu>/<int:people>/', views.dinner),
]