
from django.urls import path

from .views import UserManager,ShowSearchInfo,SaveProfile_User,ShowModifyProfile_User,DeleteModifyProfile_user,ShowPermissionViewUser,SavePermissionViewUser #Quản lý phần chức năng user management
from .views import  modifypass,ShowModifyProfile,ShowPermissionMe #Quản lý phần chức năng Modify password
from .views import ChangeImage
from .views import Creat_User_MYSQL,ADD_USER_API,UPDATE_USER_API,DELETE_USER_API,SEARCH_USER_API
from .views import SaveProfile_UserManager,create_profile_user



urlpatterns = [
    
    #Quản lý phần chức năng Modify password
    path("modifypassword/",modifypass,name='modifypassword'),
    path("saveprofile/",SaveProfile_User,name='saveprofile'), # Lưu thông tin tài khoản với AJAX GET
    path("showprofile/",ShowModifyProfile,name='showprofile'),# Hiện thị thông tin tài khoản với AJAX GET
    path("showpermission_me/",ShowPermissionMe,name='showpermissionme'),
    path("change_image/",ChangeImage,name='change_image'),#Thay đổi hình nền cá nhân
    
    
    
    #QTạo tài khoản user trong MYSQL
    path("creat_user_mysql/",Creat_User_MYSQL,name='creat_user_mysql'),
    path("add_user_mysql/",ADD_USER_API,name='add_user_mysql'),
    path("update_user_mysql/",UPDATE_USER_API,name='update_user_mysql'),
    path("del_user_mysql/",DELETE_USER_API,name='del_user_mysql'),
    path("search_user_mysql/",SEARCH_USER_API,name='search_user_mysql'),
       
       
    #Quản lý phần chức năng user management
    path("showsearchinfo/",ShowSearchInfo,name='showsearchinfo'),
    path("usermanager/",UserManager,name='usermanager'),
    path("showprofile_user/",ShowModifyProfile_User,name='showprofileuser'),
    path("saveprofile_user/",SaveProfile_UserManager,name='saveprofile_user'),
    path("DeleteModifyProfileUser/",DeleteModifyProfile_user,name='deletemodifyprofileuser'),
    path("showpermission_view_user/",ShowPermissionViewUser,name='showpermissionviewuser'),
    path("savepermission_view_user/",SavePermissionViewUser,name='savepermissionviewuser'),
    path("create_profile_user/",create_profile_user,name='create_profile_user'),
    
    
]

