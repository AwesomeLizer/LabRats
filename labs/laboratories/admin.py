from django.contrib import admin
from .models import Lab, Expert, Sample, Experiment

admin.site.register(Lab)
admin.site.register(Expert)
admin.site.register(Sample)
admin.site.register(Experiment)