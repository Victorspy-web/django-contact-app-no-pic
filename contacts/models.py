from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	name = models.CharField(max_length=200)
	group = models.CharField(max_length=14, blank=True)
	number = models.IntegerField()
	email = models.EmailField(blank=True)
	address = models.CharField(max_length=100, blank=True)
	note = models.CharField(max_length=300, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
