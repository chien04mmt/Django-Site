
from django.urls import path
from . views import logout_view
from .views import LOGIN_USER,REGISTER_USER,FORGOT_PASSWORD
from home.views import get_homeindex

urlpatterns = [
    
    path("",get_homeindex, name="home"),#Homepage login
    path("register/",REGISTER_USER,name='register'), #page register  
    path("forgotpass/",FORGOT_PASSWORD,name='forgotpass'),#page forgotpass
    path("logout/",logout_view,name='logout'),#page login
    path("login/",LOGIN_USER,name='login'),#page login logout_view
    path("accounts/login/",LOGIN_USER,name='login'),#page login logout_view
]