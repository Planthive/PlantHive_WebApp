from django.shortcuts import render
from rest_framework import viewsets

#from .serializers import HeroSerializer, UploadSerializer
#from .models import Hero, upload
from .serializers import  Growth_scheduleSerializer, Manual_scheduleSerializer
from .models import growth_schedule, manual_schedule

# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

class Growth_scheduleViewSet(viewsets.ModelViewSet):
    queryset = growth_schedule.objects.all()
    serializer_class = Growth_scheduleSerializer

class Manual_scheduleViewSet(viewsets.ModelViewSet):
    queryset = manual_schedule.objects.all()
    serializer_class = Manual_scheduleSerializer
