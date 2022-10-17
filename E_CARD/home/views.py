#----------------------------KHai báo thư viện---------------------------------------------------------------
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from API.API_LANG import CHANGE_LANG,GET_LANG
from API.API_USER import GET_ICON_USER,PERMISSION_USER
from API.is_ajax import is_ajax
import json
from django.contrib.auth import login,authenticate
from API.API_USER import *
from API.API_download_File import download_exel, download_file
from API.API_upload_files import upload_exel
from API.xlsxToJson import *
from django.views.decorators.csrf import csrf_exempt#Bỏ qua csrftocken
from API.API_GET_SIGN import GET_TAINI_SIGN
from API.API_sendMail import *
from API.API_upload_files import UPLOAD_PHOTO
from API.XlsxWriter_ import *
from django.contrib.auth.decorators import login_required
from API.ECARD import *
from login.decorator import Check_login_byAjax
from django.contrib.auth.models import User
from API.IP_REQUEST import get_client_ip


#----------------------------Trang chủ---------------------------------------------------------------

#@decorators.login_required(login_url="/login/")
#@staff_member_required
@login_required(login_url="/login/")
def get_homeindex(request):
    user=request.user.get_username().upper()
    return render(request,template_name="home/index.html")








#------------------------------LIÊN KẾT TỚI TRANG HTML---------------------------------------------------------------


#Trang thêm xóa user quyền hạn trong phòng máy chủ
@login_required(login_url="/login/")
def THEM_XOA_USER(request):
    ADMIN='hidden'
    if CHECK_ADMIN(request):ADMIN=''
    sql=LIST_FGATE()
    return render(request,template_name="home/SERVERROOM/themxoauser.html",context={"ADMIN":ADMIN,"FACTORYCODE":sql})

#trang tra cứu nhatky thao tác
@login_required(login_url="/login/")
def TRA_CUU(request):
    user=request.user.get_username()   
    selectbox=LIST_FGATE()
    return render(request,template_name="home/SERVERROOM/tracuu.html",context={"sql":'sql',"select":selectbox})


#trang tra cứu thông tin nhật ký đi lại phòng máy chủ
@login_required(login_url="/login/")
def WEB_LOG_DI_LAI(request):
    selectbox=LIST_FGATE()
    status= GET_STATUS_CARD()
    return render(request,template_name="home/SERVERROOM/tracuuravao.html",context={"select":selectbox,"status":status})



@login_required(login_url="/login/")
def Check_login(request):
    pass

######------------------------------------------QUẢN LÝ PHÒNG MÁY CHỦ SERVER ROOM----------###########_###################################

#Thực hiện tìm kiếm nhật ký thao tác
def TRA_CUU_LICHSU(request):
    data=request.GET
    sql=SEARCH_HISTORY(data)
    return JsonResponse({'returndata':sql},status=200)



#Thực hiện tìm kiếm quyền vào phòng máy
def TRA_CUU_QUYEN_PHONG_MAY(request):
    data=request.GET
    sql=SEARCH_INFO_ROOM(data)    
    return JsonResponse({'returndata':sql},status=200)



#Xóa 1 người trong phòng máy
def DELETE_PERSON_ROOM(request):
    data=request.GET
    data=Convert_QueryDict_ToDict(data)
    data.update({"IPADD":get_client_ip(request),"action":"DELETE","logip":get_client_ip(request),"user":request.user.get_username()})
    sql=REMOVE_PERSON_SVREMPDATA(data)
    if sql==False:return JsonResponse({'error':"Không xóa được mã thẻ. Có thể mã thẻ không tồn tại trong CSDL"},status=400)
    return JsonResponse({'returndata':sql},status=200)



#Thêm 1 người trong phòng máy
def ADD_PERSON_ROOM(request):
    if CHECK_USER_COUNT_ADD_RECORD_SERVERROOM(request)==False: return JsonResponse({"returndata":"Bạn chỉ được phép thêm 5 người vào phòng máy chủ, Hãy xóa những người khác để thêm lại"},status=400);
    data=request.GET
    data=Convert_QueryDict_ToDict(data)
    data.update({"IPADD":get_client_ip(request),"action":"INSERT","logip":get_client_ip(request),"user":request.user.get_username()})
    sql=ADD_PERSON_SVREMPDATA(data)   
    return JsonResponse({'returndata':sql},status=200)



#Thực hiện thêm xóa quyền
def THEM_XOA_QUYEN(request):
    data=request.GET
    data=Convert_QueryDict_ToDict(data)
    data.update({"IPADD":get_client_ip(request),"action":"","logip":get_client_ip(request),"user":request.user.get_username()})
    sql=REMOVE_PERSON_SVREMPDATA(data)
    return JsonResponse({'returndata':sql},status=200)



#Tra cứu nhật ký đi lại phòng máy chủ
def TRACUU_LOG_DI_LAI(request):
    try:
        data=request.GET
        data=Convert_QueryDict_ToDict(data)   
        sql=GET_LOG_VIEW_SERVERRECORDS(data)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({"returndata":str(ex)},status=400);




#Tải file template imoport danh sách người 
@Check_login_byAjax
def DOWNLOAD_TEMPLATE_PERSON(request):
    if is_ajax(request) and request.method=="GET":
        data=request.GET
        filename=data["filename"]
        # print(filename)
        download =download_exel(filename)
        return download 
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)




#UPLOAD FILE EXEL danh sách file cấp quyền vào phòng máy chủ
@Check_login_byAjax
@csrf_exempt
def UPLOAD_EXEL(request):
    try:
        data=request.POST
        user=request.user.get_username()
        IP=get_client_ip(request)

        if request.method == 'POST' and request.FILES['myfile']:
            myfile=request.FILES['myfile']
            if "ImportPerson" in myfile.name:            
                upload=upload_exel(request,"UPLOAD_ImportPerson.xlsx")
            
                sql=XLSX_TO_JSON2(upload['filename'])

                if len(sql)>0:sql=ADD_MULTI_PERSON_SVREMPDATA(sql,user,IP,data['Action'])
                return JsonResponse({"returndata": sql},status= 200)
           
            return JsonResponse({"error":"Không thể upload do lỗi file, chọn file ImportPerson.xlsx để upload"}, status = 400)
    except Exception as ex: return JsonResponse({"error":str(ex)}, status = 400)
    



#In xuất danh sách quyền hạn ra file exel
@Check_login_byAjax
def PRINT_EXEL_PERMISS_SERVER(request):
    #try:
        data=Convert_QueryDict_ToDict(request.GET)   
        sql=SEARCH_INFO_ROOM(data)
        if len(sql)<=0:return JsonResponse({'error':"Không có dữ liệu"},status=400)
        namefile=request.user.get_username()+"_Table.xlsx"
        list_columes=['emp_no','cname','yname','deptname','FACTORYCODE','FREMARK','FBDATE','CreatedBy']
        title_table="QUYỀN RA VÀO PHÒNG MÁY"
        link_file=WRITE_EXEL_(sql,namefile,list_columes,title_table)       
        return JsonResponse({'returndata':link_file},status=200)
    #except Exception as ex: return JsonResponse({'error':str(ex)},status=400)



#In xuất danh sách log vào ra server
@Check_login_byAjax
def PRINT_EXEL_LOG_INOUT_SERVER(request):
    try:
        data=Convert_QueryDict_ToDict(request.GET)   
        sql=GET_LOG_VIEW_SERVERRECORDS(data)

        if len(sql)<=0:return JsonResponse({'error':"Không có dữ liệu"},status=400)
        namefile=request.user.get_username()+"_Table.xlsx"
        list_columes=['CARD_NO','EMP_NO','EMP_NAME','GRP','TYPES','DEPT','INTIME','MAC','POS','IP','STATUS']
        title_table="THÔNG TIN VÀO RA PHÒNG MÁY CHỦ"
        link_file=WRITE_EXEL_(sql,namefile,list_columes,title_table)       
        return JsonResponse({'returndata':link_file},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)




#In xuất danh sách log thao tác phòng server
@Check_login_byAjax
def PRINT_EXEL_LOG_ACTION_SERVER(request):
    try:
        data=Convert_QueryDict_ToDict(request.GET)   
        sql=SEARCH_HISTORY(data)
        if len(sql)<=0:return JsonResponse({'error':"Không có dữ liệu"},status=400)
        namefile=request.user.get_username()+"_Table.xlsx"
        list_columes=['emp_no','cname','yname','deptname','FACTORYCODE','logip','action','CreatedDate','CreatedBy']
        title_table="THÔNG TIN VÀO RA PHÒNG MÁY CHỦ"
        link_file=WRITE_EXEL_(sql,namefile,list_columes,title_table)        
        return JsonResponse({'returndata':link_file},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)

#----------------------------QUẢN LÝ HỆ THỐNG---------------------------------------------------------------

#----------------------------Quản lý nhóm quyền hạn--------------------------------------------------------------

#Select,insert,update, delete quyền hạn Permission
def ACTION_Permission(request):
    try:
        data=Convert_QueryDict_ToDict(request.GET)
        data.update({'user':request.user.get_username()})
        if data['Action']=="SELECT":sql=GET_LIST_PERMISSION(data)
        if data['Action']=="INSERT":sql=INSERT_PERMISSION(data)
        if data['Action']=="UPDATE":sql=UPDATE_PERMISSION(data)
        if data['Action']=="DELETE":sql=DEL_PERMISSION(data)
        return JsonResponse({"returndata":sql}, status=200)        
    except Exception as ex: return JsonResponse({"error":str(ex)}, status=400)




#Select,insert,update, delete Menus
def ACTION_Menus(request):
    try:
        data=Convert_QueryDict_ToDict(request.GET)
        data.update({'user':request.user.get_username()})
        if data['Action']=="SELECT":sql=GET_LIST_MENUS(data)
        if data['Action']=="INSERT":
            if Check_Menu_Exist(data)==True: return JsonResponse({"error":"Menu đã tồn tại, hãy kiểm tra lại !"}, status=400)
            sql=INSERT_MENUS(data)
        if data['Action']=="UPDATE":sql=UPDATE_MENUS(data)
        if data['Action']=="DELETE":sql=DEL_MENUS(data)
        return JsonResponse({"returndata":sql}, status=200)        
    except Exception as ex: return JsonResponse({"error":str(ex)}, status=400)





#Select,insert,update, delete Modules
def ACTION_Modules(request):
    try:       
        data=Convert_QueryDict_ToDict(request.GET)
        data.update({'user':request.user.get_username()})
       
        if data['Action']=="SELECT":sql=SELECT_Modules(data)
        if data['Action']=="INSERT":sql=INSERT_Modules(data)
        return JsonResponse({"returndata":sql}, status=200)        
    except Exception as ex: return JsonResponse({"error":str(ex)}, status=400)








#----------------------------Quản lý tài khoản---------------------------------------------------------------
#Tìm kiếm tài khoản
@Check_login_byAjax
def TIM_TAIKHOAN(request):
    try:    
        data=request.GET          
        sql=GET_USER_Info(data['UserID'])
        password=''
        if len(sql)==1: 
            password=sql[0]['PassWord']
            password=Decript_Pass(password)
        context={"returndata":sql,"password":password}
        return JsonResponse(context, status=200)
    except Exception as ex: return JsonResponse({"error":str(ex)}, status=400)

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
    
    
#Tìm kiếm tài khoản
@Check_login_byAjax
def ShowSearchInfo(request):
    if is_ajax(request=request) and request.method == "GET":
        rq=request.GET.__getitem__('data')
        # field=number_to_string(request.GET.__getitem__('field'))
        field=swich_case_find(request.GET.__getitem__('field'))
        ID=''
        strquery= "SELECT * FROM Users Where "+field+" like N'%"+  rq + "%'"
        sql= SelectSQL3(strquery)
        if len(sql)>0:
            for item in sql:
                ID=str(ID)+ "'"+str(item['ID'])+"',"
            ID=ID[0:-1]
            query=("SELECT * FROM Users Where ID IN ("+str(ID)+")")
            sql= SelectSQL3(query)
        if (sql):
            return JsonResponse({"returndata":sql}, status = 200)
        else:
            return JsonResponse({'returndata':"NOT EXCUTE DB"}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)



#Hiển thị thông tin người dùng
@Check_login_byAjax
def ShowModifyProfile_User(request):
    try:
        if is_ajax(request=request) and request.method == "GET":
            ID=request.GET.__getitem__('data')
            strquery= "SELECT * FROM Users Where [ID]='"+  ID + "'"
            sql= SelectSQL3(strquery)
            # print(sql)
            password=Decript_Pass(sql[0]['PassWord'])
            return JsonResponse({"returndata":sql,'pass':password}, status = 200)
            
        return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)
    except Exception as ex:    return JsonResponse({"error":str(ex)}, status = 400)



# Quản lý tài khoản
@login_required(login_url="/login/")
def QUANLY_TAIKHOAN(request):
    sql=GET_LIST_MENUS('data')
    return render(request,template_name="home/ADMIN/QUANLYHETHONG/quanlytaikhoan.html",context={"listMenu":sql})
    pass

# Quản lý nhóm quyền hạn 
@login_required(login_url="/login/")
def QUANLY_NHOMQUYENHAN(request):
    return render(request,template_name="home/ADMIN/QUANLYHETHONG/nhomquyenhan.html")
    pass

#Hàm lưu thông tin User manager
@Check_login_byAjax
def SaveProfile_UserManager(request):
    try:
        if is_ajax(request=request) and request.method == "GET":
            data =request.GET
            user_ID=data['userID']
            Update_User_Manager( data['DFSite'],data['division'],data['UserName'],data['Emp_NO'],data['Dept'],data['CostNo'],data['Telephone'],data['mailbox'],user_ID)
        
            try:
                u =  User.objects.get(username=user_ID)
                u.first_name=''
                u.last_name=data['UserName']
                u.email=data['mailbox']           
                u.save()
                if request.user.username==user_ID:
                    request.user==u
                    login(request, u)
            except: pass
            
            
            return JsonResponse({'returndata':"ok"}, status = 200)
    except Exception as ex:return JsonResponse({"error":str(ex)}, status = 400)




#Lưu quyền hạn tài khoản người dùng
@Check_login_byAjax
def SAVE_PERMISSION(request):
    try:
        data =request.GET
        sql=SAVE_PERMISSION_USER(data['UserID'],data['Code_Permission'])        
        return JsonResponse({'returndata':sql}, status = 200)
    except Exception as ex:return JsonResponse({"error":str(ex)}, status = 400)


#Lấy thông tin quyền của tài khoản
@Check_login_byAjax
def GET_INFO_PERMISSION(request):
    try:
        data =request.GET
        sql=GET_PERMISSION_USER(data['UserID'])
        return JsonResponse({'returndata':sql}, status = 200)
    except Exception as ex:return JsonResponse({"error":str(ex)}, status = 400)


#Tải modules được cấp quyền cho tài khoản đang đăng nhập
@Check_login_byAjax
def SHOW_PERMISSION(request):
    try:
        user=request.user.get_username()
        sql=PERMISSION_USER(user)
        if len(sql)>0:return JsonResponse({'returndata':sql}, status = 200)
        return JsonResponse({"error":"Bạn chưa được cấp quyền sử dụng hệ thống. Liên hệ quản trị.."}, status = 400)
    except Exception as ex:return JsonResponse({"error":str(ex)}, status = 400)



#----------------------------Thông tin của tôi---------------------------------------------------------------

# Thông tin cá nhân
@login_required(login_url="/login/")
def THONGTIN_CANHAN(request):
    sql=GET_USER_Info(str(request.user.get_username()))[0]
    passw=Decript_Pass(sql['PassWord'])
    return render(request,template_name="home/ADMIN/QUANLYHETHONG/thongtincuatoi.html",context={"sql":sql,"pass":passw})
    pass



#----------------------------DỮ LIỆU HOẠT ĐỘNG---------------------------------------------------------------


#in danh sách mẫu đơn ra exel
@Check_login_byAjax
def PRINT_EXEL_MAUDON(request):
    if is_ajax(request) and request.method=='GET':
        data=request.GET

        query='''
            SELECT d.*,f.* FROM [DOC_DETAIL] as d
            left JOIN [DOC_PEOPLE] as f ON d.DOC_NO=f.DOC_NO
            WHERE d.DOC_NO='{}'
        '''
        sql=SelectSQL3_DIEUXE(query)

        return JsonResponse({'datareturn':'ok'},status=200)
    return JsonResponse({'error':''},status=400)



#In xuất danh sách thông tin đơn ra file exel
@Check_login_byAjax
def PRINT_EXEL_REPORT(request):
    if is_ajax(request) and request.method=='GET':
        user=request.user.get_username()
        data=request.GET
        DOC_NO=data['DOC_NO'].split(',')
        sql2=[]
        arrLength=[]
            
        query='''SELECT d.[DOC_NO],[CAR_NUMCARD],[TOTAL_PEOPLE],[LEAVE_TIME],[ARRIVE_TIME],[LEAVE_LOCAL],[ARRIVE_LOCAL],u.[UserName],u.[Telephone]
                FROM [DOC_DETAIL] as d
                LEFT JOIN [Users] as u ON d.[NguoiLamDon]=u.[UserID]
                WHERE d.[DOC_NO]='{}'
                '''.format(data['DOC_NO'])
        sql=SelectSQL3_DIEUXE(query)
        
        for item in DOC_NO:
            query2='''SELECT [PASSENGER],[MOBILE] FROM [DOC_PEOPLE] WHERE [DOC_NO]={} '''.format(item)
            sql3=SelectSQL3_DIEUXE(query2)
            sql2+=sql3
            arrLength.append(len(sql3))

        WRITE_DATA_PRINT_EXEL(sql,arrLength,sql2,user)
        response=download_exel(user+'_Detail_bus.xlsx')
        return response
        return JsonResponse({'datareturn':''},status=200)
    return JsonResponse({'error':''},status=400)



#In xuất danh sách thông tin các đơn ra file exel
@Check_login_byAjax
def PRINT_EXEL_ALLREPORT(request):
    #try:
        data=request.GET
        user=request.user.get_username()       
                
        data1={}
        
        for item in data:
            tam=''
            if len(data[item])<1: tam=' is not null '
            else: tam= " like '%"+data[item]+"%' "

            if item=='CREATE_AT_START': tam=data[item].replace("T"," ")
            if item=='CREATE_AT_END': tam= data[item].replace("T"," ")
            if item=='LEAVE_TIME': tam= data[item].replace("T"," ")
            if item=='ARRIVE_TIME': tam= data[item].replace("T"," ")
            if item=='TinhTrang':
                if data[item]=='':tam= "!= 'Waiting'"
            if item=='CAR_NUMCARD':
                if data[item]=='':tam=''
                else:tam=" and [CAR_NUMCARD] LIKE '%"+data[item]+"%' "
            if item=='COST_NO':
                if data[item]=='':tam=''
                else:tam=" and [COST_NO] LIKE '%"+data[item]+"%' "
                
            data1.update({item:tam})

        CREATE_AT=" and ([NgayTao] BETWEEN (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 23:59:00')) ".format(data1['CREATE_AT_START'],data1['CREATE_AT_END'])        
        if data1['CREATE_AT_START']=='' and data1['CREATE_AT_END']=='':CREATE_AT=""
        elif data1['CREATE_AT_START']!='' and data1['CREATE_AT_END']=='': CREATE_AT=" and [NgayTao] between (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and GETDATE() ".format(data1['CREATE_AT_START'])
        elif data1['CREATE_AT_END']!='' and data1['CREATE_AT_START']=='': CREATE_AT=" and [NgayTao] between (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and GETDATE() ".format(data1['CREATE_AT_END'])
       
        WAITING_TIME=" and ([WAITING_TIME] BETWEEN  (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00')) ".format(data1['LEAVE_TIME'],data1['ARRIVE_TIME'])        

        if data1['LEAVE_TIME']=='' and  data1['ARRIVE_TIME']=='':WAITING_TIME=""
        elif data1['LEAVE_TIME']!='' and  data1['ARRIVE_TIME']!='':WAITING_TIME=" and [WAITING_TIME] BETWEEN (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and  ( CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 23:59:00') ".format(data1['LEAVE_TIME'],data1['ARRIVE_TIME'])    
        else:
            if data1['LEAVE_TIME']!='': WAITING_TIME=" and ([WAITING_TIME] BETWEEN  (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and getdate()) ".format(data1['LEAVE_TIME'])    
            if data1['ARRIVE_TIME']!='':  WAITING_TIME=" and ([WAITING_TIME] BETWEEN  (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and getdate()) ".format(data1['ARRIVE_TIME'])    


        query='''    select d.[DOC_NO],d.LEAVE_TIME,d.ARRIVE_TIME,t.[DATACODE_CN] as TYPE_USECAR,d.NguoiLamDon,u.UserName,d.PERSON_USECAR,d.CREATE_AT, TinhTrang
                        from [DOC_DETAIL] as d '''+'''
                        LEFT JOIN [Users] as u ON d.NguoiLamDon=u.UserID 
                        LEFT JOIN [DOC_TYPEDATA] as t ON d.[TYPE_USECAR]=t.[DATATYPE] AND t.[DATA_TYPE]='TYPE_USECAR'
                        WHERE [TinhTrang] {}
                        '''.format(data1['TinhTrang'])+CREATE_AT+'''
                        '''+WAITING_TIME+'''
                        {}
                        and [NguoiLamDon] {}
                        {} order by [NgayTao] desc
                '''.format(data1['CAR_NUMCARD'],data1['NguoiLamDon'].upper(),data1['COST_NO'].upper())
        sql=SelectSQL3_DIEUXE(query)#Lấy thông tin đơn chi tiết
        
        DOC_NO1=''
        DOC_NO=''
        for item in sql:
            DOC_NO1+="'"+item["DOC_NO"]+"',"
            DOC_NO+=item["DOC_NO"]+","
            
        if ',' in DOC_NO1:DOC_NO1=DOC_NO1[0:-1]
        if ',' in DOC_NO:DOC_NO=DOC_NO[0:-1]
        
        query='''
        select [DOC_NO],t1.[DATACODE_CN] as [CAR_TYPE],[LEAVE_TIME],[ARRIVE_TIME],[LEAVE_LOCAL],
        [ARRIVE_LOCAL],t.[DATACODE_CN] as [TYPE_USECAR],[UserName],t2.DATACODE_CN as [ROUTE],t3.[DATACODE_CN] as [TinhTrang]
            FROM [DOC_DETAIL] as d
            LEFT JOIN [Users] as u ON d.[NguoiLamDon]=u.[UserID]
            LEFT JOIN [DOC_TYPEDATA] as t ON d.[TYPE_USECAR]=t.[DATATYPE] AND t.[DATA_TYPE]='TYPE_USECAR'
            LEFT JOIN [DOC_TYPEDATA] as t1 ON d.[CAR_TYPE]=t1.[DATATYPE] AND t1.[DATA_TYPE]='CAR_TYPE'
            LEFT JOIN [DOC_TYPEDATA] as t2 ON d.[ROUTE]=t2.[DATATYPE] AND t2.[DATA_TYPE]='ROUTE'
            LEFT JOIN [DOC_TYPEDATA] as t3 ON d.[TinhTrang]=t3.[DATATYPE] AND t3.[DATA_TYPE]='STATUS'
            WHERE d.[DOC_NO] in ({})'''.format(DOC_NO1)
        
        # print(query)       
        sql=SelectSQL3_DIEUXE(query)
       
        
        sql2=[]
        sql4=[]
        arrLength=[]
        arrLength1=[]
        DOC_NO=DOC_NO.split(',')
        for item in DOC_NO:
            query2='''SELECT [PASSENGER],[CODE_NO],[NUM_PEOPLE],[MOBILE] FROM [DOC_PEOPLE] WHERE [DOC_NO]={} '''.format(item)
            sql3=SelectSQL3_DIEUXE(query2)
            sql2+=sql3
            arrLength.append(len(sql3))
            
            query='''SELECT [CARNUM],[KILOMET],[OVERTIME] FROM [CAR_KM_LOG] WHERE [DOC_NO]={} '''.format(item)
            sql3=SelectSQL3_DIEUXE(query)
            sql4+=sql3
            arrLength1.append(len(sql3))
        # print(arrLength)

       
        
        WRITE_ALL_DATA_PRINT_EXEL(sql,arrLength,sql2,arrLength1,sql4,user)
        response=download_exel(user+'_Detail_bus.xlsx')
        return response
        return JsonResponse({'datareturn':''},status=200)
    #except Exception as ex: return JsonResponse({'error':str(ex)},status=400)





# -----------------------------------------------------------------------------------------------------------------------------
    
# hiển thị icon user và tên
@Check_login_byAjax
def SHOW_ICON_USER(request):
    try: 
        info=GET_ICON_USER(request) 
        return JsonResponse({"returndata":info}, status = 200)
    except Exception as ex: return JsonResponse({"error":str(ex)}, status = 400)


# Thay đổi ngôn ngữ
@Check_login_byAjax
def CHANGE_LANGUAGE(request):
    if is_ajax(request=request) and request.method == "GET": 
        user_ID= request.user.get_username()
        lang= request.GET.__getitem__('lang')
        sql=CHANGE_LANG(lang,user_ID)
        if sql:return JsonResponse({"data":'ok'}, status = 200)
    return JsonResponse({"error":"Cant not change Language"}, status = 400)


#Lấy thông tin ngôn ngữ trên db
@Check_login_byAjax
def GET_LANGUAGE(request):
    if is_ajax(request=request) and request.method == "GET": 
        user_ID= request.user.get_username()
        lang=GET_LANG(user_ID)
        return JsonResponse({"returndata":lang}, status = 200)
    return JsonResponse({"error":"Cant not get Language"}, status = 400)


#Hướng dẫn sử dụng
def Manual_Show(request):
    # print("OK")
    return render(request,template_name="home/Manual.html")









