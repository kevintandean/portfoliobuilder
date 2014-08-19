from django.forms import ModelForm
from builder.models import Project

__author__ = 'kevin'

class ProjectImageForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image']