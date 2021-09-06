from djongo import models
#from djangotoolbox.fields import EmbeddedModelField

# class Hero(models.Model):
#     name = models.CharField(max_length=60)
#     alias = models.CharField(max_length=60)
#     def __str__(self):
#         return self.name

class upload(models.Model):
    actuators=models.JSONField()
    sensors=models.JSONField()
    metadata=models.JSONField()
    system=models.JSONField()
