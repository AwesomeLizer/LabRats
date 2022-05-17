from django.urls import path
from .views import ListLab, DetailLab, ListExperiment, DetailExperiment, ListSample, DetailSample, ListExpert, DetailExpert

urlpatterns = [
    path('laboratories/', ListLab.as_view()),
    path('laboratories/<int:pk>', DetailLab.as_view()),
    path('experiments/', ListExperiment.as_view()),
    path('experiments/<int:pk>', DetailExperiment.as_view()),
    path('samples/', ListSample.as_view()),
    path('samples/<int:pk>', DetailSample.as_view()),
    path('experts/', ListExpert.as_view()),
    path('experts/<int:pk>', DetailExpert.as_view()),
]