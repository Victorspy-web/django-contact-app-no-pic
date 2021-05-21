from django.contrib.auth import views as auth_views
from django.urls import path

from registration.views import CustomLoginView, CustomLogoutView, RegisterPage

urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),
	path('register/', RegisterPage.as_view(), name='register'),

	path('change_password/', auth_views.PasswordChangeView.as_view(
		template_name='registration/change_password.html',
		success_url='/'), name='change_password'),

	path('update_password/',
		 auth_views.PasswordResetConfirmView.as_view(template_name="registration/update_password.html"),
		 name='update_password'),

	path('reset_password/',
		 auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
		 name='reset_password'),

	path('reset_password_sent/',
		 auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
		 name='password_reset_done'),

	path('reset/<uidb64>/<token>/',
		 auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
		 name='password_reset_confirm'),

	path('reset_password_complete/',
		 auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
		 name='password_reset_complete'),
]
