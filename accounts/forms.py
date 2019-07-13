from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_image', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_image')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'id': 'form_full_name',
                'placeholder': 'Your Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'id': 'form_full_name',
                'placeholder': 'Your Password'
            }
        )
    )


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'name': 'confirm_password',
                'class': 'form-control',
                'id': 'form_confirm_password',
                'placeholder': 'Confirm Password'
            }
        )
    )
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not Match")
        return make_password(password1, salt=None, hasher='default')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_image', 'password', 'confirm_password',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 'id': 'form_fisrt_name',
                    'placeholder': 'Enter First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 'id': 'form_last_name',
                    'placeholder': 'Enter last Name'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control', 'id': 'form_username',
                    'placeholder': 'Enter a Username'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 'id': 'form_email',
                    'placeholder': 'Enter your Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control', 'id': 'form_password',
                    'placeholder': 'Enter a Password'
                }
            )
        }
