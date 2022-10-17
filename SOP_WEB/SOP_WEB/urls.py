
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("LAMDON.urls")),
    path('', include("QUANLYHETHONG.urls")),
    path('', include("TRACUU.urls")),
    path('', include("USER.urls")),
    path('', include("HOME.urls")),
    path('', include("CONGVANDEN.urls")),
    
]
