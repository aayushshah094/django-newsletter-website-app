from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm

from news_api.models import Profile

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class Profileform(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']