from django.shortcuts import render
from rest_framework import viewsets

#from .serializers import HeroSerializer, UploadSerializer
#from .models import Hero, upload
from .serializers import  UploadSerializer
from .models import upload

# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer

class UploadViewSet(viewsets.ModelViewSet):
    queryset = upload.objects.all()
    serializer_class = UploadSerializer
