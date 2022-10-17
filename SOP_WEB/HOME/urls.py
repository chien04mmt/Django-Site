
from django.contrib import admin
from django.urls import path
from .views import HOME_PAGE,SHOW_PERMISSION_USER,CHANGE_LANGUAGE,Manual_Show,GET_LANGUAGE,SHOW_ICON_USER
from .views import ChangeImage,GET_USER_LOGIN

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',HOME_PAGE,name='home'),
    path('',HOME_PAGE),
    
    path("show_icon_user/",SHOW_ICON_USER,name='show_icon_user'),#Hiển thị ảnh cá nhân và tên
    path("show_permission/",SHOW_PERMISSION_USER),#Phân quyền người dùng
    path("change_lang/",CHANGE_LANGUAGE,name='change_lang'),#Đổi ngôn ngữ
    path("get_lang/",GET_LANGUAGE,name='get_lang'),#Lấy thông tin ngôn ngữ trong db
    path("manual/",Manual_Show,name='manual'),# Hướng dẫn sử dụng
    path("change_image/",ChangeImage,name='change_image'),#Thay đổi hình nền cá nhân
    path("get_userlogin/",GET_USER_LOGIN),#Lấy tên và mã thẻ người đăng nhập

]
