
from django.urls import path
from . views import logout_view
from .views import LOGIN_USER,FORGOT_PASSWORD
from HOME.views import HOME_PAGE

urlpatterns = [
    
    path("",HOME_PAGE, name="home"),#Homepage login
     path("home/",HOME_PAGE, name="home"),#Homepage index
    path("forgotpass/",FORGOT_PASSWORD,name='forgotpass'),#page forgotpass
    path("logout/",logout_view,name='logout'),#page login
    path("login/",LOGIN_USER,name='login'),#page login logout_view
    path("accounts/login/",LOGIN_USER,name='login'),#page login logout_view
    
    
]