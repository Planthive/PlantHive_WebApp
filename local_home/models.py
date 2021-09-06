from djongo import models

class sensors(models.Model):
    actuators=models.JSONField()
    sensors=models.JSONField()
    metadata=models.JSONField()
    system=models.JSONField()

class images(models.Model):
    data=models.JSONField()
    metadata=models.JSONField()

class growthrecipe(models.Model):
    isactive=models.BooleanField()
    timestamps=models.JSONField()
