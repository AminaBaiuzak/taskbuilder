from .models import Task_1
from django.forms import ModelForm, TextInput, Textarea

class Task1Form(ModelForm):
    class Meta:
        model = Task_1
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the text of task'
            }),
        }

