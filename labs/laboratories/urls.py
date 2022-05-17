from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratories_home, name = 'laboratories_home'),
    path('create', views.create, name = 'create')
]