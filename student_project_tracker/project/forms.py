from django import forms
from project.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'