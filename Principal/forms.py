# -*- coding: utf-8 -*-
from django import forms 
from Principal.models import Estudiante


from django.contrib.auth.forms import ReadOnlyPasswordHashField

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

    
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=u'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme Password', widget=forms.PasswordInput)

    class Meta:
        model = Estudiante
        #fields = ('email', 'date_of_birth')
        fields = ('email','nombre','apellido','codigo','localidad','carrera')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("El password no coincide")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.    """

    password = ReadOnlyPasswordHashField(help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = Estudiante

    def clean_password(self):
        return self.initial["password"]

class ActualizarUserForm(forms.ModelForm):
    password1 = forms.CharField(label=u'Contraseña', widget=forms.PasswordInput,required=True)
    password2 = forms.CharField(label='Confirme Password', widget=forms.PasswordInput,required=True)
    class Meta:
        model = Estudiante
        exclude =['password','groups','user_permissions','last_login','is_superuser','is_staff','is_active','date_joined']

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("El password no coincide")
        return password2