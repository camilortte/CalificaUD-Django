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


class RegisterFormForm(forms.ModelForm):
	nombreUsuario = forms.CharField(max_length=50)
	password1= forms.CharField(
		max_length=50,
		widget=forms.PasswordInput(attrs={'class':'input-xlarge','required':True}),
		label='Ingrese Password',
		required=True
		)
	password2= forms.CharField(
		max_length=50,
		widget=forms.PasswordInput(attrs={'class':'input-xlarge','required':True}),
		label='Repita Password',
		required=True
		)

	def comprobarPassword(self):
		if (self.password1==self.password2):
			return True
		else:
			return False

	class Meta:
		model = Estudiante

        exclude = ('password1','nombre',)
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': u'input-xlarge'}),
            'apellido': forms.TextInput(attrs={'class': u'input-xlarge'}),
            'email': forms.TextInput(attrs={'class': u'input-xlarge'}),
            'codigo': forms.TextInput(attrs={'class': u'input-xlarge'}),
            'localidad': forms.Select(attrs={'class': u'input-xlarge'}),
            'carrera': forms.Select(attrs={'class': u'input-xlarge'}),
        } 
    