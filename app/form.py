from django.forms import forms,ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import task

class UserRegistration(UserCreationForm):
    email = forms.EmailField(label="email")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddTask(ModelForm):
    class Meta:
        model = task
        fields = ('user', 'name', 'day','checkout')
        widgets = {
            # 'user':forms.TextInput(attrs={'class':'form-control'}),

            'name': forms.TextInput(attrs={'placeholder':'Escriba nombre de tarea', 'class':'form-control'}),
            
        }


class AddTask2(forms.Form):
    name = forms.CharField(label="Nombre",max_length=250)


    