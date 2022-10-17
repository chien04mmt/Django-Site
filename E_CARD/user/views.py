
from django.shortcuts import render
from API.API_MSSQL import *
from API.API_MYSQL import *
from API.API_USER import *
from API.is_ajax import is_ajax

# from home.security_pass import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from urllib.parse import unquote # Decode URL value key
from django.http import HttpResponse, JsonResponse # AJAX RESPONSE AND REQUEST
import json

from django.contrib.auth import login
from django.contrib.auth.models import User

from API.API_upload_files import *

# Create your views here.


#----------------------------------------------------User Modify Pass Start-------------------------------------------------------------------



@login_required(login_url='/login/')
def modifypass(request):    
    user_name=request.user.username
    strquery= "SELECT * FROM Users Where [UserID]='"+  user_name + "'"
    sql= SelectSQL(strquery)
    sql1=SelectSQL("SELECT * FROM Dept")
    sql2=SelectSQL("SELECT * FROM Site")
    if sql[0]:
        password=Decript_Pass(sql[0]['PassWord'])  
        return render(request,"home/modified_pass.html",{'sql': sql[0],'sql1':sql1,'sql2':sql2,'username':username,'pass':password})
    else:
        return render(request,"home/modified_pass.html")




#Show modified pass2 (profiles)
from API.MD5_HASH import *
@login_required(login_url='/login/')
def ShowModifyProfile(request):
    if is_ajax(request=request) and request.method == "GET":
        user_name=request.user.username
        strquery= "SELECT * FROM Users Where [UserID]='"+  user_name + "'"
        try:
            sql= SelectSQL(strquery)
            password=Decript_Pass(sql[0]['PassWord'])
            return JsonResponse({"returndata":sql,'pass':password}, status = 200)
        except:
           pass
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)




#Lưu thông tin  tài khoản view
@login_required(login_url='/login/')
def SaveProfile_User(request):
    try:
        if is_ajax(request=request) and request.method == "GET":
            data =request.GET
            user_ID=data['userID']
            password1=data['Password1']
            password=Encript_Pass(data['Password1'])
            if password!='' and password1!='':
                strquery="UPDATE  Users SET [UserID]='"+user_ID+"',[DFSite]=N'"+ data['DFSite'] +"',[division]=N'"+ data['division']+"',[UserName]=N'"+ data['UserName'] +"',[Emp_NO]='"+ data['Emp_NO'] +"',[Dept]=N'"+ data['Dept'] +"',[CostNo]='"+ data['CostNo'] +"',[Telephone]='"+ data['Telephone'] +"',[mailbox]='"+ data['mailbox'] +"',[PassWord]='"+str(password)+"' WHERE [UserID]='"+user_ID+"' "
                QuerySQL(strquery)
    
                u =  User.objects.get(username=user_ID)
                u.first_name=''
                u.last_name=data['UserName']
                u.set_password(data['Password1'])
                u.save()
                request.user==u
                login(request, u)
                
            else:
                strquery="UPDATE  Users SET [UserID]='"+user_ID+"',[DFSite]=N'"+ data['DFSite'] +"',[division]=N'"+ data['division']+"',[UserName]=N'"+ data['UserName'] +"',[Emp_NO]='"+ data['Emp_NO'] +"',[Dept]=N'"+ data['Dept'] +"',[CostNo]='"+ data['CostNo'] +"',[Telephone]='"+ data['Telephone'] +"',[mailbox]='"+ data['mailbox'] +"' WHERE [UserID]='"+user_ID+"' "
                QuerySQL(strquery)
                u =  User.objects.get(username=user_ID)
                u.first_name=''
                u.last_name=data['UserName']
                u.save()
                
            return JsonResponse({'returndata':"ok"}, status = 200)
    except Exception as ex: return JsonResponse({"error":str(ex)}, status = 400)




#Hiển thị thông tin người dùng
@login_required(login_url='/login/')
def ShowModifyProfile_User(request):
    if is_ajax(request=request) and request.method == "GET":
        ID=request.GET.__getitem__('data')
        strquery= "SELECT * FROM Users Where [ID]='"+  ID + "'"
        sql= SelectSQL(strquery)
        password=Decript_Pass(sql[0]['PassWord'])
        return JsonResponse({"returndata":sql,'pass':password}, status = 200)
        
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)




#Hàm hiển thị Quyền người Đăng nhập
def ShowPermissionMe(request):
    if is_ajax(request=request) and request.method=="GET":
        userID=request.user.username
        strquery="SELECT * FROM EPERMISSION_USER WHERE [USER_ID]='"+userID+"'"
        sql= SelectSQL(strquery)
        if(len(sql)>0):
            return JsonResponse({"returndata":sql}, status = 200)
        else:
            return JsonResponse({'returndata':"NOT EXCUTE DB"}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)   




#Hàm thay đổi hình nền cá nhân
@login_required(login_url='/login/')
@csrf_exempt
def ChangeImage(request):
    if is_ajax(request=request) and request.method=='POST':
        try:
            userID= request.user.username            
            filename=change_image(request)
            
            strquery="UPDATE [Users] SET [img]=N'"+str(filename['filename'])+"' WHERE [UserID]='"+str(userID)+"'"
            QuerySQL(strquery)
        
            return JsonResponse({"returndata":filename}, status = 200)    
        except NameError:  JsonResponse({"error":NameError}, status = 400)   
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)   



#----------------------------------------------------User Modify Pass End-------------------------------------------------------------------







#----------------------------------------------------Creat User start-------------------------------------------------------------------


#Gọi trang hiển thị tạo user POSMENT cho bảng user trong MYSQL
@login_required(login_url='/login/')
def Creat_User_MYSQL(request):
    return render(request,"home/update_user_MYSQL.html")




#Tạo mới 1 user
@login_required(login_url='/login/')
def ADD_USER_API(request):
    if is_ajax(request=request) and request.method == "GET":
        rq=request.GET  
        USER_ID= rq['USER_ID']
        USER_NAME= rq['USER_NAME']
        USER_NAME_EXT=rq['USER_NAME_EXT']
        CURRENT_OU_CODE= rq['CURRENT_OU_CODE']
        CURRENT_OU_NAME= rq['CURRENT_OU_NAME']
        JOB_TITLE= rq['JOB_TITLE']
        JOB_TYPE= rq['JOB_TYPE']
        EMAIL= rq['EMAIL']
        ADD_USER(USER_ID,USER_NAME,USER_NAME_EXT,JOB_TITLE,CURRENT_OU_CODE,CURRENT_OU_NAME,JOB_TYPE,EMAIL)
        return JsonResponse({"returndata":'OK'}, status = 200)
       
    return JsonResponse({"error":"Can't add user MYSQL"}, status = 400)




#CHỈNH sửa thông tin user
@login_required(login_url='/login/')
def UPDATE_USER_API(request):
    if is_ajax(request=request) and request.method == "GET":
        rq=request.GET  
        USER_ID= rq['USER_ID']
        USER_NAME= rq['USER_NAME']
        USER_NAME_EXT=rq['USER_NAME_EXT']
        CURRENT_OU_CODE= rq['CURRENT_OU_CODE']
        CURRENT_OU_NAME= rq['CURRENT_OU_NAME']
        JOB_TITLE= rq['JOB_TITLE']
        JOB_TYPE= rq['JOB_TYPE']
        EMAIL= rq['EMAIL']
        UPDATE_USER(USER_ID,USER_NAME,USER_NAME_EXT,JOB_TITLE,CURRENT_OU_CODE,CURRENT_OU_NAME,JOB_TYPE,EMAIL)
        return JsonResponse({"returndata":'OK'}, status = 200)
       
    return JsonResponse({"error":"Can't update user MYSQL"}, status = 400)




#Xóa thông tin user
@login_required(login_url='/login/')
def DELETE_USER_API(request):
    if is_ajax(request=request) and request.method == "GET":
        rq=request.GET  
        USER_ID= rq['USER_ID']
        DELETE_USER(USER_ID)
        return JsonResponse({"returndata":'OK'}, status = 200)
       
    return JsonResponse({"error":"Can't delete user MYSQL"}, status = 400)




# TÌM kiếm thông tin user
@login_required(login_url='/login/')
def SEARCH_USER_API(request):
    if is_ajax(request=request) and request.method == "GET":
        rq=request.GET  
        USER_ID= rq['USER_ID']
        sql=SelectMYSQL(USER_ID)

        if sql is None:return JsonResponse({"returndata":''}, status = 200)
        else:return JsonResponse({"returndata":sql}, status = 200)
        
    return JsonResponse({"error":"Can't delete user MYSQL"}, status = 400)


#----------------------------------------------------Create user End-------------------------------------------------------------------



#----------------------------------------------------User Management Funtion Start-------------------------------------------------------------------

def swich_case_find(data):
    switcher={
            'ID':'[ID]',
            'UserID':'[UserID]',
            'Name':'[UserName]',
            'Department':'[Dept]',
            'Telephone':'Telephone',
            'Email':'[mailbox]'
            }
    return switcher.get(data,"Invalid") 
    



# def number_to_string(agr):
#     match agr:
#         case 'ID':
#             return '[ID]'
#         case 'UserID':
#             return '[UserID]'
#         case 'Name':
#             return  '[UserName]'
#         case 'Department':
#             return '[Dept]'
#         case 'Telephone':
#             return '[Dept]'
#         case 'Email':
#             return '[mailbox]'
    




#User Manager
@login_required(login_url='/login/')
def ShowSearchInfo(request):
    if is_ajax(request=request) and request.method == "GET":
        rq=request.GET.__getitem__('data')
        # field=number_to_string(request.GET.__getitem__('field'))
        field=swich_case_find(request.GET.__getitem__('field'))
        ID=''
        strquery= "SELECT TOP 10 * FROM Users Where "+field+" like N'%"+  rq + "%'"
        sql= SelectSQL3(strquery)
        if len(sql)>0:
            for item in sql:
                ID=str(ID)+ "'"+str(item['ID'])+"',"
            ID=ID[0:-1]
            query=("SELECT TOP 10 * FROM Users Where ID IN ("+str(ID)+")")
            sql= SelectSQL(query)
        if (sql):
            return JsonResponse({"returndata":sql}, status = 200)
        else:
            return JsonResponse({'returndata':"NOT EXCUTE DB"}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)




# Hàm Lưu quyền hạn PERMISSION View User
@login_required(login_url='/login/')
def SavePermissionViewUser(request):
    if is_ajax(request=request) and request.method=="GET":
        data=request.GET
        userID=data['USER_ID']
        strquery="SELECT * FROM EPERMISSION_USER WHERE [USER_ID]='"+userID+"'"
        sql= SelectSQL(strquery)
        if(len(sql)>0):#Nếu tồn tại user trong bảng rồi thì cập nhật
            strquery3="UPDATE EPERMISSION_USER SET PERMISS_TYPE='"+data['PERMISS_TYPE']+"',APPROVAL='"+data['APPROVAL']+"',NEW_APP_CREAT='"+data['NEW_APP_CREAT']+"',API_CREATE_USER='"+data['API_CREATE_USER']+"',QUERY_DOC='"+data['QUERY_DOC']+"',FLOW_SET='"+data['FLOW_SET']+"',FORM_SET='"+data['FORM_SET'] +"',APPROVER_SET='"+data['APPROVER_SET']+"',USER_MANAGE='"+data['USER_MANAGE']+"',PASS_MODIFY='"+data['PASS_MODIFY']+"' WHERE [USER_ID]='"+userID+"'"
            sql=QuerySQL2(strquery3)
            if(sql):                
                return JsonResponse({"returndata":sql}, status = 200)
            else:
                return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)              
        else:# Nếu không có user thì Chèn thêm vào
            str1='''
                INSERT INTO EPERMISSION_USER ([USER_ID]
                    ,[PERMISS_TYPE]
                    ,[APPROVAL]
                    ,[NEW_APP_CREAT]
                    ,[API_CREATE_USER]
                    ,[QUERY_DOC]
                    ,[FLOW_SET]
                    ,[FORM_SET]
                    ,[APPROVER_SET]
                    ,[USER_MANAGE]
                    ,[PASS_MODIFY]
                    ,[CREATED_BY]
                    ,[CREATED_AT]
                    ,[EXPIRATION_DATE])'''
            str2= " Values('"+ data['USER_ID']+"','"+data['PERMISS_TYPE']+"','"+data['APPROVAL']+"','"+data['NEW_APP_CREAT'] +"','"+data['API_CREATE_USER']+"','"+data['QUERY_DOC']+"','" +data['FLOW_SET']+"','"+data['FORM_SET'] +"','"+data['APPROVER_SET']+"','" + data['USER_MANAGE'] +"','"+data['PASS_MODIFY'] +"','"+request.user.username +"',SYSDATETIME(),DATEADD(month,12, SYSDATETIME()))"
            sql=QuerySQL2(str1+str2)                    
            if(sql):                
                return JsonResponse({"returndata":sql}, status = 200)
            else:
                return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)          
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)   





#Vào trang giao diện usermanagement
@login_required(login_url='/login/')
def UserManager(request):
    if request.method=="GET":
        user_ID= request.user.username
        strquery= "SELECT TOP 10 * FROM Users Order by ID"
        sql=SelectSQL(strquery)
        struser= "SELECT img FROM Users Where [UserID]='"+  user_ID + "'"
        sql1= SelectSQL(struser)
        sql2=SelectSQL("SELECT * FROM Site")
        sql3=SelectSQL("SELECT * FROM Dept")
        return render(request,"home/user_manage.html",{'sql': sql,'sql1':sql1[0],'sql2':sql2,'sql3':sql3})
    return render(request,"home/user_manage.html")




#Xóa Thông tin người dùng chỉnh sửa
@login_required(login_url='/login/')
def DeleteModifyProfile_user(request):
    if is_ajax(request=request) and request.method == "GET":
        ID=request.GET.__getitem__("ID")
        strquery= "DELETE Users Where [ID]='"+  ID + "'"
        userid=Get_UserID(ID)
        if userid!="":        
            try:
                u = User.objects.get(username = userid)
                u.delete()  
            except User.DoesNotExist:pass
            
        sql= QuerySQL2(strquery)
        if (sql):
            return JsonResponse({"returndata":'OK'}, status = 200)
        else:
            return JsonResponse({'returndata':"NOT EXCUTE DB"}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)

#Hàm hiển thị quyền hạn View User
@login_required(login_url='/login/')
def ShowPermissionViewUser(request):
    if is_ajax(request=request) and request.method=="GET":
        userID=request.GET.__getitem__('data')
        strquery="SELECT * FROM EPERMISSION_USER WHERE [USER_ID]='"+userID+"'"
        sql= SelectSQL(strquery)
        if(len(sql)>0):
            return JsonResponse({"returndata":sql}, status = 200)
        else:
            return JsonResponse({'returndata':"NOT EXCUTE DB"}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)   

#Hàm lưu thông tin User manager
@login_required(login_url='/login/')
def SaveProfile_UserManager(request):
    if is_ajax(request=request) and request.method == "GET":
        data =request.GET
        user_ID=data['userID']
        Update_User_Manager( data['DFSite'],data['division'],data['UserName'],data['Emp_NO'],data['Dept'],data['CostNo'],data['Telephone'],data['mailbox'],user_ID)
      
        u =  User.objects.get(username=user_ID)
        u.first_name=''
        u.last_name=data['UserName']
        u.email=data['mailbox']           
        u.save()
        if request.user.username==user_ID:
            request.user==u
            login(request, u)
        return JsonResponse({'returndata':"ok"}, status = 200)
    return JsonResponse({"error":"Not Save user"}, status = 400)

@login_required(login_url='/login/')
def create_profile_user(request):
    if is_ajax(request=request) and request.method == "GET":
        data =request.GET

        #Kiểm tra xem có trên hệ thống chưa
        if Check_UserName(data['userID']) == True: 
            return HttpResponse("This Acount Already Existing in system. Please check again...") 
        else:   
            #Nếu chưa thì thêm mới vào hệ thống
            Add_new_User(data['DFSite'],data['userID'],data['UserName'], '',data['Dept'],data['Emp_NO'] , data['Telephone'],data['mailbox'] ,data['division'], data['CostNo'])
               
            return JsonResponse({'returndata':"ok"}, status = 200)
    return JsonResponse({"error":"Not Save user"}, status = 400) 

#----------------------------------------------------User Management Funtion End-------------------------------------------------------------------
