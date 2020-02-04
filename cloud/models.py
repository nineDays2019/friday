from django.db import models


# Create your models here.

class File(models.Model):
    create_time = models.fields.DateTimeField()
    path = models.fields.CharField(max_length=1024)

