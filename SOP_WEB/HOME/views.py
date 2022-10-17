
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse # AJAX RESPONSE AND REQUEST
from API.API_LANG import CHANGE_LANG,GET_LANG
from API.API_MSSQL import SelectSQL3_SOP
from API.API_USER import GET_ICON_USER
from API.is_ajax import is_ajax
from API.API_USER import *
from API.API_LANG import CHANGE_LANG,GET_LANG
from django.views.decorators.csrf import csrf_exempt
from API.API_upload_files import *
from USER.decorator import Check_login_byAjax


@Check_login_byAjax
def GET_USER_LOGIN(request):
    try: 
        user=request.user.get_username()
        sql=SelectSQL3_SOP("SELECT TenDangNhap,HoTen FROM Users where TenDangNhap='{}' ".format(user))
        return JsonResponse({"returndata":sql[0]}, status = 200)
    except Exception as ex: return JsonResponse({"error":str(ex)}, status = 400)
    



@login_required(login_url="/login/")
def HOME_PAGE(request):
    userlogin=request.user.get_username()
    #print(userlogin)    
    CVD=SelectSQL3_SOP("SELECT COUNT(*) as Sum_WaitingArr FROM [RegisterDocumentArrive] where Next_appro='{}' and Status='Waiting' ".format(userlogin))
    sql=SelectSQL3_SOP("exec sp_GetMail")
    sql_=SelectSQL3_SOP("SELECT COUNT(*) as SumMyDoc FROM ApprovalSection WHERE UserName='{}' and Orders='1'".format(userlogin))
    SumMyDoc=0
    Sum_Waiting=0
    Sum_WaitingArr=0
    
    if len(sql_)>0:SumMyDoc=sql_[0]['SumMyDoc']
    for item in sql:
        if item['UserName']==userlogin: Sum_Waiting=item['SUMWAITNG']   
   
    if len(CVD)>0:Sum_WaitingArr=CVD[0]['Sum_WaitingArr']
    return render(request,'HOME/index.html',context={"userlogin":userlogin,'Sum_Waiting':Sum_Waiting,'Sum_WaitingArr':Sum_WaitingArr,'SumMyDoc':SumMyDoc})





    
# hiển thị icon user và tên
def SHOW_ICON_USER(request):
    if is_ajax(request=request) and request.method == "GET": 
        info=GET_ICON_USER(request) 
        return JsonResponse({"returndata":info}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)



# quyền hạn
def SHOW_PERMISSION_USER(request):
    try:   
        user_ID= request.user.get_username()
        query="""SELECT TOP 1 [CodeRole] FROM [UsersInRoles] WHERE [UserName]='{}' """.format(user_ID)
        CodeRole=SelectSQL3_SOP(query)

        if len(CodeRole)>0:
            CodeRole=CodeRole[0]['CodeRole']          
            query="""SELECT * FROM [Modules] WHERE [CodeRole]='{}' """.format(CodeRole)
            query="""SELECT md.Code,md.CodeRole,mn.Name from Modules as md
                        left join [Menus] as mn on md.Code=mn.Code
                        where md.CodeRole = '{}' and mn.IsDeleted!='1' """.format(CodeRole)
            # print(query)
            sql=SelectSQL3_SOP(query)
            return JsonResponse({"returndata":sql}, status = 200)

        else: return HttpResponse("<h1>Can Not get Permission User.....</h1>")
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)



# Thay đổi ngôn ngữ
def CHANGE_LANGUAGE(request):
    if is_ajax(request=request) and request.method == "GET": 
        user_ID= request.user.get_username()
        lang= request.GET.__getitem__('lang')
        sql=CHANGE_LANG(lang,user_ID)
        if sql:return JsonResponse({"data":'ok'}, status = 200)
    return JsonResponse({"error":"Cant not change Language"}, status = 400)



#Lấy thông tin ngôn ngữ trên db
def GET_LANGUAGE(request):
    if is_ajax(request=request) and request.method == "GET": 
        user_ID= request.user.get_username()
        sql=GET_LANG(user_ID)
        if len(sql)>0:return JsonResponse({"returndata":sql}, status = 200)
    return JsonResponse({"error":"Cant not get Language"}, status = 400)




#Hướng dẫn sử dụng
def Manual_Show(request):
    # print("OK")
    return render(request,template_name="home/Manual.html")



#Hàm thay đổi hình nền cá nhân
@login_required(login_url='/login/')
@csrf_exempt
def ChangeImage(request):    
    if request.method=='POST' and request.FILES['myfile']:
        Error=''
        try:
            userID= request.user.get_username()
            filename=change_image(request)
            # print(filename)
            Error=filename
            Error="UPDATE [Users] SET [img]=N'"+str(filename['filename'])+"' WHERE [UserID]='"+str(userID)+"'"
            QuerySQL(Error)
            return JsonResponse({"returndata":filename}, status = 200)    
        except Exception as ex:  
            chuoi=str(Error) +"Exeption:"+str(ex)
            return JsonResponse({"error":chuoi}, status = 400)   
    return JsonResponse({"error":"Method error, POST Please"}, status = 400)   




