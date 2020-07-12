from django.db import models

# Create your models here.


class Template(models.Model):
    name = models.CharField(default="", max_length=255)
