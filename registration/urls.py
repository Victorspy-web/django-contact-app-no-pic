from django.urls import path
from registration.views import CustomLoginView, CustomLogoutView, RegisterPage

urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),
	path('register/', RegisterPage.as_view(), name='register'),
]