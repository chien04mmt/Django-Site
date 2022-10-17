

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#-------------------------------------------UPLOAD FORM----------------------------------------------------------------------------
#Up load 1 file
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
    

# Up load nhiều file
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#----------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------USER REGISTER FORM---------------------------------------------------------------------
class RegisterForm(UserCreationForm):
    #fields we want to include and customize in our form
    # first_name = forms.CharField(max_length=100,
    #                              required=True,
    #                              widget=forms.TextInput(attrs={'placeholder': 'First Name',
    #                                                            'class': 'form-control',
    #                                                            }))
    # last_name = forms.CharField(max_length=100,
    #                             required=True,
    #                             widget=forms.TextInput(attrs={'placeholder': 'Last Name',
    #                                                           'class': 'form-control',
    #                                                           }))
    # username = forms.CharField(max_length=100,
    #                            required=True,
    #                            widget=forms.TextInput(attrs={'placeholder': 'Username',
    #                                                          'class': 'form-control',
    #                                                          }))
    # email = forms.EmailField(required=False,
    #                          widget=forms.TextInput(attrs={'placeholder': 'Email',
    #                                                        'class': 'form-control',
    #                                                        }))
    # password1 = forms.CharField(max_length=50,
    #                             required=False,
    #                             widget=forms.PasswordInput(attrs={'placeholder': 'Password',
    #                                                               'class': 'form-control',
    #                                                               'data-toggle': 'password',
    #                                                               'id': 'password',
    #                                                               }))
    # password2 = forms.CharField(max_length=50,
    #                             required=False,
    #                             widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
    #                                                               'class': 'form-control',
    #                                                               'data-toggle': 'password',
    #                                                               'id': 'password',
    #                                                               }))
    username = forms.CharField(required =True)
    password1 = forms.CharField(required =True, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(required = True, widget=forms.PasswordInput, label='Repeat Password')
    email = forms.EmailField(required = True)
    
    
    
# from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.contrib.auth import get_user_model
# # Create your views here.
# User= get_user_model()
# class LoginForm(forms.Form):
#     username= forms.CharField()
#     password= forms.CharField()
#     widget= forms.PasswordInput(
#         attrs={
#             "class":"form-control",
#             "id":"user-password"
#         }
#     )
    
#     def clean_username(self):
#         username= self.cleaned_data.get("username")
#         qs= User.objects().fillter(username_iexact= username)
#         if not qs.exists():
#             raise forms.ValidationError("This is an invalid user.")
#         return username
  
# non_allowed_username=['abc']      
# #check for unique Email and username
# class RegisterForm1(forms.Form):
#     username= forms.CharField()
#     email= forms.EmailField()
    
#     password1= forms.CharField(required=False)
#     label="Password",
#     widget= forms.PasswordInput(
#         attrs={
#             "class":"form-control",
#             "id":"user-password"
#         }
#     )
#     password2= forms.CharField()
#     label="Confirm Password",
#     widget= forms.PasswordInput(
#         attrs={
#             "class":"form-control",
#             "id":"user-fonfirm-password"
#         }
#     )
    
#     def clean_username(self):
#         username= self.cleaned_data.get("username")
#         qs= User.objects().fillter(username_iexact= username)
#         if username in non_allowed_username:
#             raise forms.ValidationError("This is an invalid user.Please pick another.")
#         if not qs.exists():
#             raise forms.ValidationError("This is an invalid user.Please pick another.")
#         return username
    
#     def clean_email(self):
#         email= self.cleaned_data.get("email")
#         qs= User.objects().fillter(username_iexact= email)        
#         if not qs.exists():
#             raise forms.ValidationError("This email is alreaddy in use.")
#         return email
    
    
# class RegisterForm2(UserCreationForm):
#     username= forms.CharField()
#     email= forms.EmailField()
    
#     password1= forms.CharField(required=False)
#     label="Password",
#     widget= forms.PasswordInput(
#         attrs={
#             "class":"form-control",
#             "id":"user-password"
#         }
#     )
#     password2= forms.CharField()
#     label="Confirm Password",
#     widget= forms.PasswordInput(
#         attrs={
#             "class":"form-control",
#             "id":"user-confirm-password"
#         }
#     )



































#     def clean_username(self):
#         username= self.cleaned_data.get("username")
#         qs= User.objects().fillter(username_iexact= username)
#         if username in non_allowed_username:
#             pass
#             #raise forms.ValidationError("This is an invalid user.Please pick another.")
#         if not qs.exists():
#             pass
#             #raise forms.ValidationError("This is an invalid user.Please pick another.")
#         return username
    
#     def clean_email(self):
#         email= self.cleaned_data.get("email")
#         qs= User.objects().fillter(username_iexact= email)        
#         if not qs.exists():
#             pass
#             #raise forms.ValidationError("This email is alreaddy in use.")
#         return email
    
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email',)

#     def clean_email(self):
#         # Get the email
#         email = self.cleaned_data.get('email')

#         # Check to see if any users already exist with this email as a username.
#         try:
#             match = User.objects.get(email=email)
#         except User.DoesNotExist:
#             # Unable to find a user, this is fine
#             return email

#         # A user was found with this as a username, raise an error.
#         raise forms.ValidationError('This email address is already in use.')


    
    
    
    
    
    
    
    
