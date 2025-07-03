from django import forms
from .models import Task

CATEGORY_CHOICES = [
    ('work', 'Work'),
    ('study', 'Study'),
    ('personal', 'Personal'),
]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
