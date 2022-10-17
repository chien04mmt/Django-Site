
from django.shortcuts import render,redirect
from API.API_MSSQL import *
from API.API_MYSQL import *
from API.API_USER import *

from API.is_ajax import is_ajax
from API.API_upload_files import *
from API.SOP_DB import ACTION_USER,ADD_POISISION_USER,ADD_DEPARTMENT_USER,ADD_MANAGER_ROOM,CreatedCodeAuto,SELECT_TABLE

# from home.security_pass import *
from django.contrib.auth.decorators import login_required
from USER.decorator import Check_login_byAjax
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse # AJAX RESPONSE AND REQUEST
from django.contrib.auth import login
from django.contrib.auth.models import User
import hashlib
from django.contrib.auth import authenticate,login
# Create your views here.






#----------------------------Quản lý tài khoản---------------------------------------------------------------

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
    

@login_required(login_url='/login/')


#----------------------------------------------------QUẢN LÝ HỆ THỐNG-------------------------------------------------------------------


#-----------Quản lý tài khoản


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
    

#User Manager
# @Check_login_byAjax
def ShowSearchInfo(request):
    try:
        data=request.GET   
        col=data['Column']
        value=data['ValueFind']
        query='''SELECT u.*,ul.CodeRole,r.Name FROM Users as u 
                LEFT JOIN UsersInRoles as ul on u.TenDangNhap=ul.UserName
                LEFT JOIN Roles as r on ul.CodeRole=r.Code
                WHERE u.{} like '%{}%'  order by u.TenDangNhap'''.format(col,value)
        # query='''SELECT * FROM Users WHERE {} like '%{}%' '''.format(col,value)      
        sql= SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    




# Hàm Lưu quyền hạn PERMISSION View User
@Check_login_byAjax
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
@Check_login_byAjax
def UserManager(request):
    if request.method=="GET":
        user_ID= request.user.username
        strquery= "SELECT TOP 10 * FROM Users Order by ID"
        sql=SelectSQL(strquery)
        struser= "SELECT img FROM Users Where [UserID]='"+  user_ID + "'"
        sql1= SelectSQL(struser)
        sql2=SelectSQL("SELECT * FROM Site")
        sql3=SelectSQL("SELECT * FROM Dept")
        return render(request,"HOME/quanlyhethong/quanlytaikhoan.html",{'sql': sql,'sql1':sql1[0],'sql2':sql2,'sql3':sql3})
    return render(request,"HOME/quanlyhethong/quanlytaikhoan.html")




#Xóa Thông tin người dùng chỉnh sửa
@Check_login_byAjax
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
@Check_login_byAjax
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




#Hành động thao tác với tài khoản người dùng
def ACTION_ACOUNT_USER(request):
    try:
        data =request.GET
        user= request.user.get_username()
        if data['Action']=='CREATE':
                sql=SELECT_TABLE('Users','TenDangNhap',data['TenDangNhap'])
                if len(sql)>0: return JsonResponse({'error':"賬款已存在請登入別的賬款 / Tài khoản đã tồn tại vui lòng nhập tài khoản khác"},status=400)
                
        sql=ACTION_USER(data,user)
        if sql and (data['Action']=='CREATE' or data['Action']=='UPDATE'):            
            ADD_POISISION_USER(data,user)
            ADD_DEPARTMENT_USER(data,user)
            ADD_MANAGER_ROOM(data,user)
        return JsonResponse({'returndata':'sql'},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)

    
    
    
    
#Hàm lưu thông tin tài khoản
@Check_login_byAjax
def SaveProfile_UserManager(request):
    try:
        data =request.GET
        user= request.user.get_username()
        password=data['pass1id']
        passw = hashlib.md5(password.encode()).hexdigest().upper()
        query='''
            declare @TenDangNhap nvarchar(50)='{}'
            declare @MatKhau nvarchar(50)='{}'
            declare @HoTen nvarchar(50)='{}'
            declare @NguoiSua nvarchar(50)='{}'
            declare @Email nvarchar(100)='{}'
            declare @SoDienThoai nvarchar(50)='{}'
            UPDATE Users set [MatKhau]=@MatKhau,[HoTen]=@HoTen,[NgaySua]=GETDATE(),[NguoiSua]=@NguoiSua
                        ,[Email]=@Email,[SoDienThoai]=@SoDienThoai
            WHERE [TenDangNhap]=@TenDangNhap
        '''.format(data['TenDangNhap'],passw,data['HoTen'],user,data['Email'],data['SoDienThoai'])
        sql=QuerySQL_SOP(query)

        if request.user.username==data['TenDangNhap']:
            u =  User.objects.get(username=user)
            u.first_name=''
            u.last_name=data['HoTen']
            u.email=data['Email']           
            u.save()
            my_user= authenticate(request, username=user, password= passw)
            login(request, my_user, backend='django.contrib.auth.backends.ModelBackend') 
            
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    






#-----------Quản lý quyền hạn

#Load danh sách role quyền hạn
def Load_Roles(request):
    try:
        query="SELECT [Code],[Name],[IsDeleted] FROM [Roles] where IsDeleted!='1' "
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    
    
#Load danh sách menus
def Load_Menus(request):
    try:
        query="""SELECT m.[Code],m.[Name],m.[Orders],m.[Groups],c.CatName as Groups1
                    FROM [SOP_V2].[dbo].[Menus] as m
                    left join Categorys as c on m.Groups = c.CatCode  
                    where m.IsDeleted!='1' order by m.Groups """
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    

#Load quyền hạn của nhóm quyền hạn
def Load_Group_Permiss(request):
    try:
        data=request.GET
        query="""select m.CodeRole,m.Code,mn.Name as Menuname,mn.Groups,r.Name as Permissname 
                from Modules as m
                left join Menus as mn on m.Code=mn.Code
                left join Roles as r on m.CodeRole=r.Code
                where mn.IsDeleted!='1' and m.CodeRole='{}' order by mn.Groups
                """.format(data['CodeRole'])
        print(query)
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
        
        

#lưu cấu hình nhóm quyền hạn
def Save_Group_Permiss(request):
    try:
        data=request.GET
        sql=QuerySQL2_SOP("DELETE [Modules] WHERE CodeRole='{}' ".format(data['CodeRole']))
        user=request.user.get_username()

        for item in data:
            if 'check_' in item: 
                Code=item[item.rindex('_')+1:] 
                query="""INSERT INTO Modules( [ID],[Code],[Xem],[ThemMoi],[Sua],[Xoa],[BaoCao],[TimKiem],[NgayTao],[NguoiTao],[ResetPass],[CodeRole])
                            VALUES(NEWID(),'{}','0','0','0','0','0','0',GETDATE(),'{}','1','{}')
                        """.format(Code,user,data['CodeRole'])
                # print(query)
                sql=QuerySQL_SOP(query)
        return JsonResponse({'returndata':'OK'},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
                
        
  
#Thêm sửa xóa nhóm quyền hạn
def ACTION_GROUP_PERMISS(request):
    try:
        data=request.GET
        CreatedBy=request.user.get_username()
        query=''
        if data['Action']=='CREATE':
            query="""DELETE [Roles] WHERE [Code]='{}' 
                    INSERT INTO [Roles]( [ID],[Code],[Name],[CreatedBy],[CreatedDate],[IsDeleted]) VALUES(NEWID(),'{}',N'{}','{}',GETDATE(),'0')
                    """.format(data['Code'],data['Code'],data['Name'],CreatedBy)            
        if data['Action']=='UPDATE':
            query="""UPDATE [Roles] SET [Name]=N'{}',[UpdatedBy]='{}',[UpdatedDate]=GETDATE()
                     WHERE [Code]='{}'
                    """.format(data['Name'],CreatedBy,data['Code'])
        if data['Action']=='DELETE':
            query="DELETE [Roles] WHERE [Code]='{}' ".format(data['Code'])
        sql=QuerySQL2_SOP(query)  
        return JsonResponse({'returndata':'OK'},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
                
              
 #Sinh mã tự động
def Get_AutoCode(request):
    try:
        data=request.GET
        Autocode=CreatedCodeAuto(data['NameCol'],data['NameTable'])
        # print(Autocode)
        return JsonResponse({'Autocode':Autocode},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
                
          
        
#Lấy danh sách các danh mục
#CT-00002:Phòng ban
#CT-00003:Nhà xưởng
#CT-00010:Loại văn bản
#CT-00005:Trạng thái thẩm duyệt
#CT-00006:Nhóm menu
#CT-00007:Kết án
#CT-00008:Cài đặt Email
#CT-00009:Thời gian lưu trữ
#CT-00010:Loại văn kiện
def Load_OptionsCategorys(request):
    try:       
        data=request.GET
        
        #Lấy danh sách các menu đang sử dụng
        if data['CatTypeCode']=='MN':#Load danh sách menu nếu là MN           
            query="""SELECT g.[Code],g.[Name] ,g. Groups,c.CatName as Groups1
                        FROM [Menus]  as g
                        inner join Categorys as c on g.Groups=c.CatCode
                        WHERE g.IsDeleted!='1'
                        order by Groups """
            sql=SelectSQL3_SOP(query)           
            query="""SELECT CatCode,CatName,CatTypeCode,Code FROM Categorys  WHERE CatTypeCode='CT-00006' and IsDeleted!='1' """
            sql1=SelectSQL3_SOP(query)
            return JsonResponse({'returndata':sql,'returndata1':sql1,},status=200)
        
        #Lấy danh sách menu đã bị xóa
        if data['CatTypeCode']=='LIST-DEL-MENUS':
            query="""SELECT g.[Code],g.[Name] ,g. Groups,c.CatName as Groups1
                        FROM [Menus]  as g
                        inner join Categorys as c on g.Groups=c.CatCode
                        WHERE g.IsDeleted='1'
                        order by Groups """
            sql=SelectSQL3_SOP(query)
            query="""select CatCode,CatName,CatTypeCode,Code from Categorys  where CatTypeCode='CT-00006' and IsDeleted!='1' """
            sql1=SelectSQL3_SOP(query)
            return JsonResponse({'returndata':sql,'returndata1':sql1,},status=200)
        
        #Lấy danh sách các Categorys
        query="SELECT CatCode,CatName,CatTypeCode,Code from Categorys WHERE CatTypeCode='{}'  and IsDeleted!='1' order by CatCode".format(data['CatTypeCode'])
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)




#Thêm sửa xóa danh mục Categorys
def Action_Categorys(request):   
    try:  
        data=request.GET      
        CreatedBy=request.user.get_username()        
        query=''
        if data['Action']=="CREATE":
            CatCode=CreatedCodeAuto('CatCode','Categorys')
            query="""INSERT INTO Categorys([ID],[CatCode],[CatName],[CatTypeCode],
                                                    [CreatedBy],[CreatedDate],[IsDeleted],[Code])
                    VALUES(NEWID(),'{}',N'{}','{}',N'{}',GETDATE(),'0',N'{}')
                """.format(CatCode,data['CatName'],data['CatTypeCode'],CreatedBy,data['Code'])
        elif data['Action']=="UPDATE":
            query="""UPDATE Categorys SET [CatName]=N'{}',[UpdatedBy] =N'{}',[UpdatedDate]=GETDATE(),[Code]=N'{}'
                    WHERE [CatCode]='{}' AND  [CatTypeCode]='{}' """.format(data['CatName'],CreatedBy,data['Code'],data['CatCode'],data['CatTypeCode'])
        elif data['Action']=="DELETE":
            query="DELETE Categorys WHERE [CatCode]='{}' AND  [CatTypeCode]='{}' ".format(data['CatCode'],data['CatTypeCode'])
            
        sql=QuerySQL_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    
    
    
#Thao tác thêm sửa xóa Menu
def Action_Menus(request):
    try:
        data=request.GET
        CreatedBy=request.user.get_username()        
        query=''
        if data['Action']=="CREATE":
            Code=CreatedCodeAuto('Code','Menus')
            query="""INSERT INTO [Menus]([ID],[Code],[Name],[CreatedDate],[CreatedBy],[IsDeleted],[Groups])
                        VALUES(NEWID(),'{}',N'{}',GETDATE(),'{}','0','{}')
                        """.format(Code,data['Name'],CreatedBy,data['Groups'])
        elif data['Action']=="UPDATE":
             query="""UPDATE [Menus] SET [Name]=N'{}',[UpdatedDate]=GETDATE(),[UpdatedBy]='{}',[Groups]='{}' WHERE [Code]='{}'
                    """.format(data['Name'],CreatedBy,data['Groups'],data['Code'])
        elif data['Action']=="DELETE":
            query="""UPDATE [Menus] SET IsDeleted='1',[DeletedDate]=GETDATE(),[DeletedBy]='{}' WHERE [Code]='{}' and [Groups]='{}'""".format(CreatedBy,data['Code'],data['Groups'])
        elif data['Action']=="RESTORE":
            query="""UPDATE [Menus] SET IsDeleted='0',[UpdatedDate]=GETDATE(),[UpdatedBy]='{}' WHERE [Code]='{}' and [Groups]='{}'""".format(CreatedBy,data['Code'],data['Groups'])
        sql=QuerySQL_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)



#Thêm sửa xóa đơn vị quản lý phòng ban
def Action_Dept_Arrive(request):
    try:
        data=request.GET
        user=request.user.get_username()
        query1="""SELECT d.*,c.CatName as Department1
                    FROM Dept_Arrive as d
                    INNER JOIN Categorys as c on d.Department=c.CatCode"""
        query2="""SELECT * FROM Dept_Arrive WHERE Department='{}' """.format(data['Department'])
        query=''
        
        if data['Action']=='INSERT':#Thêm mới quản lý phòng ban
            if len(SelectSQL3_SOP(query2))>0: return JsonResponse({'error':"Mã thẻ hoặc phòng ban đã được thêm trước đó, kiểm tra lại"},status=400)
            query="""INSERT INTO [Dept_Arrive]
                        ([ID],[Department],[UserName],[Manager],[CreatedBy],[CreatedDate])
                    VALUES(NEWID(),'{}','{}','{}','{}',GETDATE())
                """.format(data['Department'],data['UserName'],data['Manager'],user)
        elif data['Action']=='UPDATE':#Chỉnh sửa thông tin quản lý phòng ban
            query="""UPDATE [Dept_Arrive] 
                       SET [UserName]='{}',[Manager]='{}',[CreatedBy]='{}',[CreatedDate]=GETDATE()
                    WHERE Department='{}'               
                """.format(data['UserName'],data['Manager'],user,data['Department'])
        elif data['Action']=='DELETE':#Xóa cài đặt 
            query="""DELETE Dept_Arrive WHERE Department='{}' AND UserName='{}' """.format(data['Department'],data['UserName'])
        elif data['Action']=='SELECT':#Lấy danh sách cài đặt người đảm nhiệm trong phòng ban công văn đến
            query1=""" SELECT d.*,c.CatName as Department1
                        FROM Dept_Arrive as d
                        INNER JOIN Categorys as c on d.Department=c.CatCode"""
        #print(query)
         
        
        sql=QuerySQL_SOP(query)
        sql=SelectSQL3_SOP(query1)
        #print(sql)
        return JsonResponse({"returndata":sql},status=200)
    except Exception as ex: return JsonResponse({"error":str(ex)},status=400)
    
    
    
    
    
#Thêm sửa xóa Tổng giám đốc Action_TGD
def Action_TGD(request):   
    try:  
        data=request.GET         
        sql=''
        if data['Action']=="SELECT":            
            query="""SELECT z.TongGiamDoc,u.HoTen,z.HoTroGiamDoc,u1.HoTen as HoTen1 
                        FROM [Zongjingli] as z 
                        LEFT JOIN Users as u on z.TongGiamDoc=u.TenDangNhap 
                        LEFT JOIN Users as u1 on z.HoTroGiamDoc=u1.TenDangNhap """
            sql=SelectSQL3_SOP(query)
            
        elif data['Action']=="UPDATE":
            
            query_="SELECT * FROM Users WHERE TenDangNhap='{}' ".format(data['TongGiamDoc'])
            sql_=SelectSQL3_SOP(query_)
            if len(sql_)<1:return JsonResponse({'error':"Mã thẻ giám đốc chưa tồn tại trong bảng tài khoản người dùng, vui lòng kiểm tra lại hoặc tạo tài khoản cho mã thẻ: "+str(data['TongGiamDoc'])},status=400)
            
            query_="SELECT * FROM Users WHERE TenDangNhap='{}' ".format(data['HoTroGiamDoc'])
            sql_=SelectSQL3_SOP(query_)
            if len(sql_)<1:return JsonResponse({'error':"Mã thẻ người hỗ trợ chưa tồn tại trong bảng tài khoản người dùng, vui lòng kiểm tra lại hoặc tạo tài khoản cho mã thẻ: "+str(data['HoTroGiamDoc'])},status=400)
            
            query="""UPDATE [Zongjingli] SET [TongGiamDoc]=N'{}', [HoTroGiamDoc]=N'{}' """.format(data['TongGiamDoc'],data['HoTroGiamDoc'])
            sql=QuerySQL_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    