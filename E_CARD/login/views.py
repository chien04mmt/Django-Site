
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from API.API_AUTOLOGIN import SAVE_LOG_LOGIN

from API.API_MSSQL import *
from API.API_MYSQL import *
from API.API_USER import *
from API.MD5_HASH import *
from API.Write_Cookie import set_cookie

from API.API_sendMail import SEND_PASSWORD
from API.is_ajax import is_ajax

# from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib.auth.hashers import *

from django.views.decorators.csrf import csrf_exempt
from API.MD5_HASH import Decript_Pass
import urllib
from ipware import get_client_ip

#đăng xuất trang web
def logout_view(request):
    logout(request)
    # Check_login_byAjax
    # # print("Log out")
    return redirect('home')
    # return render(request,"login/login.html")      
 
 
#đăng nhập
@csrf_exempt
def LOGIN_USER1(request):
    if request.method=="POST":
        user= request.POST.__getitem__("username")
        passw= request.POST.__getitem__("password")
     
        if Check_Acount(user,passw):#Kiểm tra nếu tài khoản đã tồn tại trong db table Users
            # my_user = authenticate(request, username=username, password=password)
            my_user= authenticate(request, username=user, password= passw)
            if my_user is None:# Nếu chưa tồn tại thì tạo mới trong dbsqlite
                try:                  
                    email=Get_Acount_Info(user,passw)['mailbox']
                    fullname=Get_Acount_Info(user,passw)['UserName']
                    usersave=User.objects.create_user(user,email,passw,last_name=fullname,is_staff=True) 
                    usersave.save()
                    request.user==user
                    login(request, my_user, backend='django.contrib.auth.backends.ModelBackend') 
                except:
                    return HttpResponse("<h3  style='color:Blue;'>Acount created sucessful,Please Login Again...<h3>")         
            request.user==user
            login(request, my_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        return HttpResponse("<h3 style='color:red;'>User not existing...<h3>")           
    return render(request,"login/login.html")     

#đăng nhập
@csrf_exempt
def LOGIN_USER(request): 
    # request.session.set_expiry(10000)
    if request.method=="POST":
        url=request.get_full_path()
        url=url.replace('/login/?next=','')
        url=url.replace('login/','')
        url=urllib.parse.unquote(url)
        # print(url)
        user= request.POST.__getitem__("username").upper()
        passw= request.POST.__getitem__("password")
        if Check_Acount(user,passw):#Kiểm tra nếu tài khoản đã tồn tại trong db table Users
            # my_user = authenticate(request, username=username, password=password)
            my_user= authenticate(request, username=user, password= passw)
            if my_user is None:# Nếu chưa tồn tại thì tạo mới trong dbsqlite
                try:
                    sql=Get_Acount_Info(user,passw)          
                    email=sql['mailbox']
                    fullname=sql['UserName']
                    usersave=User.objects.create_user(user,email,passw,last_name=fullname,is_staff=True) 
                    usersave.save()
                    request.user==user
                    if not SET_PERMISSION_USER(user) :return HttpResponse("<h3  style='color:Blue;'>Not Set Permission for User<h3>")  
                    # if CHECK_PERMISSION(user)!=1 :return HttpResponse("<h3 style='color:red;'>User has expired<h3>")   
                    login(request, my_user, backend='django.contrib.auth.backends.ModelBackend') 
                    # login(request, my_user)
                    return redirect(url)
                except:
                    return HttpResponse("<h3  style='color:Blue;'>Please push key F5 on keyboard or Login Again by click link... <a href='#' onclick='location.reload();' > Click me</a><h3>")         
            request.user==user
            # if CHECK_PERMISSION(user)!=1 :return HttpResponse("<h3 style='color:red;'>User has expired<h3>")   
            login(request, my_user)

            SAVE_LOG_LOGIN(user,request)
            
            return redirect(url)
        return HttpResponse("<h3 style='color:red;'>Error Username or password... <hr/> <a href='/login/'>Back</a><h3>")           
    return render(request,"login/login.html")     



#Đăng ký
@csrf_exempt
def REGISTER_USER2(request):
    if request.method=="POST":    
        username= request.POST.get("username")
        username=username.upper()
        password1= request.POST.get("password1")
        password2= request.POST.get("password2")  
        email= request.POST.get("email")
        
        if password1!= password2 : return HttpResponse("Not the same password") 
        try:
            associated_users = User.objects.filter(Q(email=email))
            user=associated_users[0] 
            return HttpResponse("Email already existing...") 
        except: pass
        
        try:
            associated_users = User.objects.filter(Q(username=username))
            user=associated_users[0] 
            return HttpResponse("User already existing...") 
        except: pass
        
        my_user= authenticate(username=username, password= password1)        
        if my_user is None:
            try:
                User.objects.create_user(username,email,password1,is_staff=True)
                if Check_UserName(username): Update_Passw(username,password1,email)
                else: Creat_Users(username,password1,username,email)
                return HttpResponse("<h3>Created Acount Successful, Plese Login...<a href='/home/'>Login</a></h3>") 
                #User.objects.create_user(username,email,password1,is_staff=True, is_superuser=True)
            except: return  render(request,"login/register.html")
        return HttpResponse("User already existing...") 
    
    return render(request,"login/register.html")
      
      
      


def REGISTER_USER(request):
    if request.method=="POST":
        data=request.POST
        password1= data['PassWord']
        password2= data['PassWord2']
        username=data['UserID'].lower()
        email=data['mailbox']
        
        if password1!= password2 : return HttpResponse("Not the same password") 
        query= "Select [UserID],[mailbox] FROM Users WHere [UserID]='"+str(username)+"'"
        sql=SelectSQL3(query)
        if len(sql)>0:
            return HttpResponse("<h1 style='color:#2196f3'>Tài khoản đã tồn tại !<br>(Account already exists)</h1><hr/><h3><a href='/home/'>Login</a></h3>")
        try:
            associated_users = User.objects.filter(Q(username=data['UserID'].lower()))
            user=associated_users[0]
            user.delete()
            return HttpResponse("<h1 style='color:#2196f3'>Tài khoản đã tồn tại !<br>(Account already exists)</h1><hr/><h3><a href='/home/'>Login</a></h3>")
        except: pass       
       
        
        my_user= authenticate(username=data['UserID'].lower(), password= password1)        
        if my_user is None:
            try:
                User.objects.create_user(data['UserID'].lower(),data['mailbox'], data['PassWord'],last_name=data['UserName'],is_staff=True)
                sql=Creat_Users1(data['UserID'],data['DFSite'],data['division'],data['UserName'],
                                 data['Emp_NO'],data['Dept'],data['CostNo'],data['Telephone'],
                                 data['mailbox'],data['PassWord'] )
                return HttpResponse("<h1 style='color:#2196f3'>Tạo tài khoản thành công !<br>Vui lòng liên hệ để cấp quyền hạn:<br>(Created Acount Successful, lease contact)</h1><hr/><h3><p>Trần Nết Thơm<br>Ext: 32050<br>Email: idsbg-hr-vnga09@mail.foxconn.com</p></h3> <hr/><h3><a href='/home/'>Login</a></h3>") 
              
            except Exception as ex: return  HttpResponse("Lỗi tạo tài khoản:"+str(ex))
        return HttpResponse("<h1 style='color:#2196f3'>Tài khoản đã tồn tại !<br>(Account already exists)</h1><hr/><h3><a href='/home/'>Login</a></h3>") 
    
    return render(request,"login/register.html")
      
      
      
      

#Quên mật khẩu sử dụng gửi mail với tài khoản đã đăng nhập
@csrf_exempt
def FORGOT_PASSWORD1(request):
    if request.method=="POST":
        
        email= request.POST.get("email")
        email=email.replace(" ",'') 
        try:
            match = User.objects.get(email=email)
            associated_users = User.objects.filter(Q(email=email))
            user=associated_users[0] 
            password=GET_USER_Info(user)

            if len(password)>0:
                password=password['PassWord']
                SEND_PASSWORD(email,'',password,request)
                return HttpResponse("Your password sent to mail: %s " %email) 
        except User.DoesNotExist:#Kiểm tra sự tồn tại của Email 
            return HttpResponse("Email: %s không tồn tại" %email)  # Unable to find a user, this is fine  
    
    return render(request,'login/forgot_pass.html')  


#Quên mật khẩu khi chưa đăng nhập lần nào
@csrf_exempt
def FORGOT_PASSWORD(request):
    if request.method=="POST":       
        email= request.POST.get("email")
        email=email.replace(" ",'') 
        
        sql=GET_USER_Info_Email(email)
        if len(sql)>0:
                password=Decript_Pass(sql['PassWord'])
                send=SEND_PASSWORD(email,'',password,request)
                if send: INSERT_LOG_SENDMAIL('SendPass','SYSTEM',email,'',send,'Gửi mật khẩu cho người dùng: '+email)
                return HttpResponse("Your password sent to mail: %s " %email) 
        return HttpResponse("Email: %s không tồn tại" %email)  # Unable to find a user, this is fine  
    
    return render(request,'login/forgot_pass.html')  
