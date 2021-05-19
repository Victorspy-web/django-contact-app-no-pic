from django import forms
from django.contrib.auth.models import User


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
		fields = ['username','first_name','last_name', 'email']
