from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from cores import views
from cores.forms import LoginForm
from cores.views import CustomLoginView

#
urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='user_profile'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('theme', views.changetheme, name='changetheme'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
