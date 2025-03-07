from django import forms
from .models import Student
from django.forms.widgets import DateInput

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'course', 'enrollment_date', 'year_level']
        widgets = {
            'enrollment_date': DateInput(attrs={'type': 'date'}),
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }