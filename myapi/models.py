from djongo import models
#from djangotoolbox.fields import EmbeddedModelField

# class Hero(models.Model):
#     name = models.CharField(max_length=60)
#     alias = models.CharField(max_length=60)
#     def __str__(self):
#         return self.name

class growth_schedule(models.Model):
    isactive=models.BooleanField()
    timestamps=models.JSONField()
