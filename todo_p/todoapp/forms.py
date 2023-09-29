from django import forms

from todoapp.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task','priority','date')

