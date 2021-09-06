from rest_framework import serializers

#from .models import Hero, upload
from .models import upload

# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name', 'alias')

class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = upload
        fields = '__all__'
        actuators = serializers.JSONField()
        sensors = serializers.JSONField()
        metadata = serializers.JSONField()
        system = serializers.JSONField()
