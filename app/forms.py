#-*- coding: utf-8 -*-
from django import forms
from app.models import MyUser
from django.forms import ModelForm
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from django.contrib.auth.models import User

class ConnexionForm(forms.Form):
	username = forms.CharField(
		label="Nom d'utilisateur",
		max_length=30)
	password = forms.CharField(
		label="Mot de passe", 
		max_length=30, 
		widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30,help_text=None)
	password = forms.CharField(max_length=30,widget=forms.PasswordInput)
	class Meta:
		model=MyUser
		fields = ['username', 'password', 'first_name', 'last_name','email']

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			MyUser.objects.get(username=username)
		except MyUser.DoesNotExist:
			return username
		raise forms.ValidationError("Ce pseudonyme existe déjà.")
	
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
		    user.save()
		return user