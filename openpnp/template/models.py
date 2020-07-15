from django.db import models


class AttributeTemplateModel(models.Model):
    name = models.CharField(default="", max_length=255)
    min_value = models.IntegerField(default=0)
    min_value_alt = models.IntegerField(default=0)
    max_value = models.IntegerField(default=100)
    max_value_alt = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class SkillTemplateModel(models.Model):
    name = models.CharField(default="", max_length=255)
    min_value = models.IntegerField(default=0)
    max_value = models.IntegerField(default=100)
    description = models.CharField(default="", max_length=255)

    def __str__(self):
        return self.name


class TemplateModel(models.Model):
    name = models.CharField(default="", max_length=255, unique=True)
    skills = models.ManyToManyField(SkillTemplateModel)
    attributes = models.ManyToManyField(AttributeTemplateModel)

    def __str__(self):
        return self.name
