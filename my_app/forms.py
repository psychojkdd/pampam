from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Post

        
class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Введите ваш email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']

