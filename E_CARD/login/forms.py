from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms

# class UserForm(ModelForm):
#     class Meta:
#        model = User
#        fields = ('username','email', 'password','is_staff','is_active','is_superuser')
#     widgets={
#     'password': TextInput(attrs={'type':'password'})
#     }
    
# class SignupForm(UserCreationForm):
#     username = forms.CharField(max_length=30, required=True, help_text='Required.')
#     password = forms.CharField(max_length=30, required=True, help_text='Required.')
#     first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
#     last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
        
         
# user_form = UserForm(request.POST, instance=user)
# if form.is_valid():
#     user = user_form.save()
#     user.set_password('unencrypted_password')  # replace with your real password
#     user.save()
#     return redirect('index_guru')