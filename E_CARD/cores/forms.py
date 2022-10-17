from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Profile, User

# from django.contrib.auth.models import User


Area_Name = (
    ('', 'Choose your Area'),
    ("QV", "Quế Võ"),
    ("HT","Đình Trám"),
    ("QC","Quang Châu"),
)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'id': 'imageUpload', 'type': 'file', 'name': 'profile_photo', 'capture' : '' ,'hidden':''}))
    displayName = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid','id':'displayName','placeholder':'Dislay Name'}))
    class Meta:
        model = Profile
        fields = ['avatar','displayName']

class UpdateUserForm(forms.ModelForm):
    # username = forms.CharField(label=False, max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'User Name'}))
    first_name = forms.CharField(label=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid','placeholder':'First Name'}))
    last_name = forms.CharField(label=False, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder':'Last Name'}))
    email = forms.EmailField(label=False, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder':'Email Address'}))
    EmployeeID = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder form-control-lg form-control-solid': 'Employee ID', 'id': 'UserID'}))
    Location = forms.ChoiceField(label=False, choices=Area_Name, widget=forms.Select(attrs={'class': 'form-select form-select-solid', 'data-control': 'select2', 'data-placeholder': 'Choose your area', 'data-hide-search': 'true', 'id': 'userArea'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'EmployeeID', 'Location']


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control form-control-lg form-control-solid',}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control form-control-lg form-control-solid',}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control form-control-lg form-control-solid',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control form-control-lg form-control-solid',}))
    EmployeeID = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder': 'Employee ID', 'id': 'UserID'}))
    Location = forms.ChoiceField(required=True, label=False, choices=Area_Name, widget=forms.Select(attrs={'class': 'form-select form-select-solid', 'data-control': 'select2', 'data-placeholder': 'Choose Your Area:', 'data-hide-search': 'true', 'id': 'Location'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control form-control-lg form-control-solid', 'data-toggle': 'password', 'id': 'password',}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control form-control-lg form-control-solid', 'data-toggle': 'password','id': 'password',}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2','Location', 'EmployeeID']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'placeholder': 'User Name','class': 'form-control form-control-lg form-control-solid', 'id': 'username'}))
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control form-control-lg form-control-solid','data-toggle': 'password','id': 'password','name': 'password',}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class RegisterForm2(forms.ModelForm):
    UserID = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID', 'id': 'UserID'}))
    UserArea = forms.ChoiceField(label=False, choices=Area_Name, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'User Area', 'id': 'userArea'}))

    class Meta:
        model = Profile
        fields = ['UserID', 'UserArea']
