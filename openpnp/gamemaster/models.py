from django.db import models


class Template(models.Model):
    name = models.CharField(default="", max_length=255, unique=True)

    def __str__(self):
        return self.name
