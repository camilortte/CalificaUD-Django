from django import forms 
from Principal.models import Estudiante

class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(attrs={'class':'input-block-level','required':True}),
		label='Ingrese su correo',
		required=True)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'class':'input-block-level','required':True}),
		label='password',
		required=True)


