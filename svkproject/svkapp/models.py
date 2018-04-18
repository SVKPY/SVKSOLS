from django.db import models


# Create your models here
class Todo(models.Model):
    name = models.CharField(primary_key=True, max_length=36)
    desc = models.CharField(max_length=36)
    topic = models.CharField(max_length=36)

