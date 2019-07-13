from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import forms


class CustomUserAdmin(UserAdmin):
	add_form = forms.CustomUserCreationForm
	form = forms.CustomUserChangeForm
	add_fieldsets = (
		(
			None, {
				'classes': ('wide',),
				'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'profile_image')}
		),
	)
	fieldsets = UserAdmin.fieldsets + (
		('Profile', {'fields': ('profile_image',)}),
	)
	model = User
	list_display = ['username', 'email', 'first_name', 'last_name']
	list_display_links = ['username', 'email']


admin.site.register(User, CustomUserAdmin)
