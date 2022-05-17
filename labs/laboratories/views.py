from django.shortcuts import render
from rest_framework import generics
from .models import Lab, Sample, Expert, Experiment

def laboratories_home(request):
    return render(request,