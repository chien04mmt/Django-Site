

from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse # AJAX RESPONSE AND REQUEST
from django.db.models.query_utils import Q
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from API.API_USER_SOP import *
from API.API_MSSQL import *
from API.API_MYSQL import *
from API.SOP_DB import ACTION_USER

from django.contrib.auth import logout
from django.contrib.auth.hashers import *
from django.views.decorators.csrf import csrf_exempt
import urllib
from ipware import get_client_ip

#đăng xuất trang web
def logout_view(request):
    logout(request)
    # print("Log out")
    return redirect('home')
    return render(request,"login/login.html")      
 


#đăng nhập
@csrf_exempt
def LOGIN_USER(request): 

    if request.method=="POST":
        
        url=request.get_full_path()
        url=url.replace('/login/?next=','')
        url=url.replace('login/','')
        url=urllib.parse.unquote(url)

        user= request.POST.__getitem__("username").replace(" ","").upper()
        passwd= request.POST.__getitem__("password")  
        passw = hashlib.md5(passwd.encode()).hexdigest().upper()      
        # print(passwd)        
        sql=Check_Acount(user,passwd)
        
        if len(sql)>0:#Kiểm tra nếu tài khoản đã tồn tại trong db table Users           
            my_user= authenticate(request, username=user, password= passw)
            if my_user is None:# Nếu chưa tồn tại thì tạo mới trong dbsqlite
                try:
                    associated_users = User.objects.filter(Q(username=user))
                    user=associated_users[0]
                    user.delete()                   
                except: pass
                
                try:
                    email=sql[0]['Email']
                    fullname=sql[0]['HoTen']
                    usersave=User.objects.create_user(user,email,passw,last_name=fullname,is_staff=True) 
                    usersave.save()
                  
                    my_user= authenticate(request, username=user, password= passw)                  
                    login(request, my_user, backend='django.contrib.auth.backends.ModelBackend') 
                    return redirect(url)
                except:
                    redirect("/home/")
                    return HttpResponse("<h3  style='color:Blue;'>Please push key F5 on keyboard or Login Again by click link... <a href='#' onclick='location.reload();' > Click me</a><h3>")         
            
                     
            login(request, my_user)
            # SAVE_LOG_LOGIN(user,request)
            
            return redirect(url)
        return HttpResponse("<h3 style='color:red;'>Error Username or password... <hr/> <a href='/login/'>Back</a><h3>")           
    return render(request,"login/login.html")     





#Đăng ký
def REGISTER_ACOUNT(request):
    try:
        data=request.GET
        sql=ACTION_USER(data,data['TenDangNhap'])
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)






#Quên mật khẩu khi chưa đăng nhập lần nào
@csrf_exempt
def FORGOT_PASSWORD(request):
    if request.method=="POST":

        return render(request,'login/forgot_pass.html')  
