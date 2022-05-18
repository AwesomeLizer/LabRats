from rest_framework import generics
from .models import Lab, Sample, Expert, Experiment
from .serializers import LabSerializer, ExperimentSerializer, ExpertSerializer, SampleSerializer

class ListLab(generics.ListCreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class DetailLab(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class ListExperiment(generics.ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class DetailExperiment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class ListSample(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class DetailSample(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class ListExpert(generics.ListCreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


class DetailExpert(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
