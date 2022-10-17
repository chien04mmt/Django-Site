from ast import Return

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from project.models import ProjectInformations

from .forms import LoginForm, RegisterForm, UpdateProfileForm, UpdateUserForm
from .models import Profile, User

# Create your views here.


@login_required()
def home(request):
    context = {'AllInfor': ProjectInformations,
               }
    return render(request, 'index.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Your profile is updated successfully')
            status = 1
            return render(request, 'users/profile.html', {'status': status,'user_form': user_form, 'profile_form': profile_form})
            # return redirect(to='/profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            status = 1
            username = form.cleaned_data.get('username')
            return render(request, self.template_name, {'status':status,'username':username})

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        if user is not None and user.is_active:
            login(self.request, user)
            return super(CustomLoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'User name or password are not correct')
        return redirect('login')

@login_required()
def changetheme(request):
    if request.method == 'GET' and request.GET['mode']:
        theme = request.GET['mode']
        link = request.GET['redirect']
        print(link)
        instance = request.user.profile
        instance.theme = theme
        instance.save()
    return redirect(to=link)
