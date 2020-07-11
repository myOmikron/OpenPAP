from django import forms
from django.core.exceptions import ValidationError

from dashboard import models


class CreateTemplateForm(forms.Form):
    name = forms.CharField(max_length=255, min_length=1)

    def clean_name(self):
        if self.cleaned_data["name"] in [obj.name for obj in models.Template.objects.all()]:
            raise ValidationError("Object already exists!")
        return self.cleaned_data["name"]

    def create_template(self):
        temp = models.Template()
        temp.name = self.cleaned_data["name"]
        temp.save()
