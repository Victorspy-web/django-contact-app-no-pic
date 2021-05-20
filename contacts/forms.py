from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordChangeForm


class UserUpdateForm(forms.ModelForm):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'type',
				'placeholder': 'New Username',
			}
		)
	)

	first_name = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
				'class': 'type',
				'placeholder': 'First Name',
			}
		)
	)

	last_name = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
				'class': 'type',
				'placeholder': 'Last Name',
			}
		)
	)

	email = forms.EmailField(
		required=False,
		widget=forms.TextInput(
			attrs={
				'class': 'type',
				'placeholder': 'Add Email',
			}
		)
	)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']


class CustomPasswordChangeForm(PasswordChangeForm):
	error_css_class = 'has-error'
	error_messages = {'password_incorrect': "Sorry you entered an incorrect password."}
	old_password = forms.CharField(
		required=True,
		label='Old Password',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter your old password'
			}
		),
		error_messages={'required': 'Please enter your valid old password'})

	new_password1 = forms.CharField(
		required=True,
		label='New password',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter your new password'
			}
		),
		error_messages={'required': 'Enter a valid password'})

	new_password2 = forms.CharField(
		required=True,
		label='Confirm new password',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Confirm new password'
			}
		),
		error_messages={'required': 'Enter a valid password'})

