from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import FormView


class CustomLoginView(LoginView):
	template_name = 'registration/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('home')


class CustomLogoutView(LogoutView):
	template_name = 'registration/logout.html'


class RegisterPage(FormView):
	template_name = 'registration/signup.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('home')

	# Logs registered user automatically
	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterPage, self).form_valid(form)

	# Redirects authenticated users
	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('home')
		return super(RegisterPage, self).get(*args, **kwargs)
