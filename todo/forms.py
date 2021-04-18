from .models import Todo
from django import forms






class TodoForm(forms.ModelForm):

    content = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder':'enter your task',
        'class': 'todo-input', 
    }))

    class Meta:
        model = Todo
        fields = ['content']



class TodoUpdateForm(forms.ModelForm):

    content = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder':'update this task',
        'class': 'todo-input', 
    }))

    class Meta:
        model = Todo
        fields = ['content', 'completed']









