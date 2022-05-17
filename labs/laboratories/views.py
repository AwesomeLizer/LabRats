from django.shortcuts import render
from rest_framework import generics
from .models import Lab, Sample, Expert, Experiment
from .serializers import LabSerializer, ExperimentSerializer, ExpertSerializerForPost, SampleSerializerForPost

class ListLab(generics.ListCreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class DetailLab(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class ListExperiment(generics.ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
