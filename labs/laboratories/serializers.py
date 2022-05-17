from rest_framework import serializers
from .models import Lab, Experiment, Expert, Sample


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'


class ExpertSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'


class SampleSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'
