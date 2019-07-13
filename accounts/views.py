from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User
from . import forms


def register(request):
	register_form = forms.RegisterForm()
	if request.method == 'POST':
		register_form = forms.RegisterForm(request.POST, request.FILES)
	context = {
		'form': register_form
	}
	if register_form.is_valid():
		first_name = register_form.cleaned_data.get('first_name')
		last_name = register_form.cleaned_data.get('last_name')
		username = register_form.cleaned_data.get('username')
		email = register_form.cleaned_data.get('email')
		password = register_form.cleaned_data.get('password')
		if User.objects.filter(username=username).exists():
			messages.error(request, "Username taken")
		elif User.objects.filter(email=email).exists():
			messages.error(request, "Email taken")
		else:
			register_form.save()
			messages.success(request, "Successfully Registered")
			return redirect('login')
	return render(request, 'accounts/register.html', context)


def login(request):
	login_form = forms.LoginForm(request.POST or None)
	context = {
		'form': login_form
	}
	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		user = auth.authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('index')
		else:
			messages.error(request, "Incorrect Credentials")
	return render(request, 'accounts/login.html', context)


def logout(request):
	auth.logout(request)
	return redirect('index')
