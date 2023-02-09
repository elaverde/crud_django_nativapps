from django import forms
from .models import Student, Curse, Registration
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})



class CurseForm(forms.ModelForm):
    class Meta:
        model = Curse
        fields = ['name','schedule','date_start','date_end']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa tu nombre aquí'}),
            'schedule': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa el horario aquí'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Ingresa la fecha de inicio aquí'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Ingresa la fecha de finalización aquí'}),
        }
   
class StudentForm(forms.ModelForm):
    curse = forms.ModelMultipleChoiceField(queryset=Curse.objects.all(), widget=forms.CheckboxSelectMultiple, label='Cursos', required=True)

    class Meta:
        model = Student
        fields = ['name','last_name','age','email','curse']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre aquí'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tus apellidos aquí'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu edad aquí'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo electrónico aquí'})
        }
        
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student','curse']
        
