from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class PostAdmin(admin.ModelAdmin):
	list_display = ('name', 'user', 'number', 'group', 'email', 'address')
	list_filter = ('user', 'group', 'address')
	search_fields = ('name', 'number', 'email')
	ordering = ('name',)