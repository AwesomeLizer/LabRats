from django.urls import path
from .views import ListLab

urlpatterns = [
    path('laboratories/', ListLab.as_view()),
]