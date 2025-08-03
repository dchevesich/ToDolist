from django import forms
from .models import Tarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        # Es mejor ser explícito con los campos
        fields = ['nombre', 'prioridad', 'completo']

        # Aquí definimos cómo se verá cada campo en el HTML
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': '¿Qué necesitas hacer?'
            }),
            'prioridad': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'
            }),
            'completo': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'
            }),
        }


class UserRegistration(forms.Form):
    usuario = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Nombre de usuario'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'placeholder': 'Tu contraseña'
        }),
        help_text='Ingresa password.'
    )


class UserSignUpForm(UserCreationForm):
    pass



