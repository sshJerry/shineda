from django import forms
from .models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'style':'width:20px;height:20px;align-items:center;'}),
        }
