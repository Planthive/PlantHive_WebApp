from rest_framework import serializers

#from .models import Hero, upload
from .models import growth_schedule

# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name', 'alias')

class Growth_scheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = growth_schedule
        fields = '__all__'
        isactive = serializers.BooleanField()
        timestamps = serializers.JSONField()

        def create(self, validated_data):
            """
            Create and return a new `Upload` instance, given the validated data.
            """
            return upload.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Snippet` instance, given the validated data.
            """
            instance.isactive = validated_data.get('isactive', instance.isactive)
            instance.timestamps = validated_data.get('timestamps', instance.timestamps)
            instance.save()
            return instance
