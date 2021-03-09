from django.urls import path
from . import views

urlpatterns = [
    #pratice 030/lotoo/ =>?
    # path('var_route/<value>/', views.var_route),
    path('lotto/', views.lotto),
    path('ping/', views.ping), #name='ping'
    # path('pong/', views.pong, name='pong'),



]

