# forms.py
from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2', 'course_number']
        widgets = {
            'course_number': forms.TextInput(attrs={'readonly': 'readonly'})  # Make the course_number field read-only
        }
