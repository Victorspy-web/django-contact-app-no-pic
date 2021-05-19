from django.urls import path
from .views import contact_create, contact, update_contact, delete_contact, ContactList

urlpatterns = [
	path('', ContactList.as_view(), name='home'),

	# path('', landing_page, name='home'),
	path('create/', contact_create, name='create'),

	path('contact/<str:pk>/', contact, name='contact'),
	path('update/<str:pk>/', update_contact, name='update'),
	path('delete/<str:pk>/', delete_contact, name='delete'),
]