
from API.API_MSSQL import SelectSQL3,QuerySQL2,QuerySQL
from API.API_USER import GET_PERMISSION_USER


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Xử lý cắt chuỗi có dấu , ở cuối chuỗi
def Remove_comma_LastString(stringText):
    if stringText[len(stringText)-1:]==",":
        stringText=stringText[0:-1]
    return stringText


#Chuyển đổi QueryDict từ request về dictionary
def Convert_QueryDict_ToDict(data):
    return {x:data.get(x) for x in data.keys()} 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]






#-------------------------------------------THÊM SỬA XÓA QUYỀN NGƯỜI RA VÀO PHÒNG MÁY CHỦ------------------------------------------------------------------------------------------------]

#Kiểm check quyền hạn nếu không phải admin sẽ chỉ được thêm 5 người vào phòng máy chủ
#Muốn thêm tiếp thì phải xóa người khác đi
def CHECK_USER_COUNT_ADD_RECORD_SERVERROOM(request):
    user=request.user.get_username()
    query="""SELECT [CreatedBy] FROM [SVREMPDATA] WHERE [CreatedBy]='{}' """.format(user)
    sql=SelectSQL3(query)
    if len(sql)>=5:return False
    return True
     

#Kiểm tra xem mã thẻ có tồn tại trong table SVREMPDATA hay không
def Check_Empno_SVREMPDATA(Empno):
    query="""SELECT * FROM SVREMPDATA WHERE [emp_no]= '{}' """.format(Empno)
    sql=SelectSQL3(query)
    if len(sql)>0: return True
    else :return False
    
        
#Thêm 1 người vào phòng máy chử
def ADD_PERSON_SVREMPDATA(data):
    query="""
            INSERT INTO [SVREMPDATA]([emp_no],[cname],[yname],[deptname],[FACTORYCODE],[FBDATE],[IPADD],[FREMARK],[CreatedBy])
            VALUES(N'{}',N'{}',N'{}',N'{}',N'{}',GETDATE(),N'{}',N'{}',N'{}')
            
        """.format(data['emp_no'].upper(),data['cname'],data['yname'],data['deptname'].upper(),data['FACTORYCODE'].upper(),data['IPADD'],data['FREMARK'],data['user'])
        
    #chèn log   
    query+="""INSERT INTO [SVROOM_log]([emp_no],[cname],[yname],[deptname],[FACTORYCODE],[logip],[action],[CreatedBy],[CreatedDate])
                VALUES(N'{}',N'{}',N'{}',N'{}',N'{}',N'{}',N'INSERT',N'{}',GETDATE())                
    """.format(data['emp_no'].upper(),data['cname'],data['yname'],data['deptname'].upper(),data['FACTORYCODE'].upper(),
                data['logip'],data['user'])
    
    sql=QuerySQL2(query) 
    return sql


#Xóa 1 người trong phòng máy
def REMOVE_PERSON_SVREMPDATA(data):
    #Kiểm tra tồn tại của thẻ
    sql=Check_Empno_SVREMPDATA(data['emp_no'].upper())
    if sql==False:return sql
    FACTORYCODE=data['FACTORYCODE']
    if FACTORYCODE!='' :FACTORYCODE=" and FACTORYCODE='{}' ".format(FACTORYCODE)
    
    query="""INSERT INTO [SVROOM_log]([emp_no],[cname],[yname],[deptname],[FACTORYCODE],[logip],[action],[CreatedBy],[CreatedDate])
             SELECT [emp_no],[cname],[yname],[deptname],[FACTORYCODE],'{}' as [logip],'DELETE' as [action],'{}' as [CreatedBy],GETDATE() as [CreatedDate] 
             FROM [SVREMPDATA] WHERE [emp_no]='{}' {} 
             ORDER BY CreatedDate desc
             
             """.format(data['logip'],data['user'].upper(),data['emp_no'],FACTORYCODE) 
               
    query+="""DELETE [SVREMPDATA] WHERE [emp_no]='{}' {} 
            """.format(data['emp_no'].upper(),FACTORYCODE)

    sql=QuerySQL2(query)  
    return sql


#Thêm nhiều người vào phòng máy 
def ADD_MULTI_PERSON_SVREMPDATA(sql,CreatedBy,IP,Action):
    query=''
    list_emp=''
    
    #Thao tác thêm danh sách người vào phòng máy chủ
    if Action=="INSERT":
        for data in sql:
            emp_no=data['emp_no'].upper().replace(" ","")
            FACTORYCODE=data['FACTORYCODE'].upper().replace(" ","")
            if emp_no=="" or FACTORYCODE=="":continue
            list_emp+="'"+emp_no+"',"
            #Thêm người
            query="""
                    INSERT INTO [SVREMPDATA]([emp_no],[cname],[yname],[deptname],[FACTORYCODE],[FBDATE],[IPADD],[FREMARK],[CreatedBy])
                    VALUES(N'{}',N'{}',N'{}',N'{}',N'{}',GETDATE(),N'{}',N'{}',N'{}')
                    
                """.format(data['emp_no'].upper(),data['cname'],data['yname'],data['deptname'].upper(),data['FACTORYCODE'].upper(),IP,data['FREMARK'],CreatedBy)
                
            #chèn log thêm
            query+="""INSERT INTO [SVROOM_log]([emp_no],[cname],[yname],[deptname],[FACTORYCODE],[logip],[action],[CreatedBy],[CreatedDate])
                        VALUES(N'{}',N'{}',N'{}',N'{}',N'{}',N'{}',N'INSERT',N'{}',GETDATE())                
            """.format(data['emp_no'].upper(),data['cname'],data['yname'],data['deptname'].upper(),data['FACTORYCODE'].upper(),IP,CreatedBy)
        
    #Xóa danh sách người vào phòng máy chủ      
    elif Action=='DELETE':
        for data in sql:
            emp_no=data['emp_no'].upper().replace(" ","")
            FACTORYCODE=data['FACTORYCODE'].upper().replace(" ","")
            if emp_no=="" or FACTORYCODE=="":continue
            list_emp+="'"+emp_no+"',"
            query+=""" INSERT INTO [SVROOM_log]([emp_no],[cname],[yname],[deptname],[FACTORYCODE],[logip],[action],[CreatedBy],[CreatedDate])
                        SELECT [emp_no],[cname],[yname],[deptname],[FACTORYCODE],'{}' as [logip],'DELETE' as [action],'{}' as [CreatedBy],GETDATE() as [CreatedDate] 
                        FROM [SVREMPDATA] WHERE [emp_no]='{}' and FACTORYCODE='{}'
                        DELETE [SVREMPDATA] WHERE [emp_no]='{}' and FACTORYCODE='{}'
                
                """.format(IP,CreatedBy,emp_no,FACTORYCODE,emp_no,FACTORYCODE)

    sql=QuerySQL(query) 
    
    list_emp=Remove_comma_LastString(list_emp)
    query="""SELECT * FROM [SVREMPDATA] WHERE  [emp_no] in ({}) """.format(list_emp)
    sql=SelectSQL3(query)
    return sql


#Tìm kiếm thông tin quyền vào phòng máy chủ
def SEARCH_INFO_ROOM(data):
    emp_no=data['emp_no'].upper()
    cname=data['cname']
    deptname=data['deptname'].upper()
    FACTORYCODE=data['FACTORYCODE'].upper()
    START_TIME=data['START_TIME']
    END_TIME=data['END_TIME']      
    CreatedBy=data['CreatedBy']      
    FBDATE=''
    
    if emp_no!='':emp_no=" and emp_no like '%{}%' ".format(emp_no)
    if deptname!='':deptname=" and deptname like '%{}%' ".format(deptname)
    if cname!='':cname=" and cname like '%{}%' ".format(cname)
    if FACTORYCODE!='':FACTORYCODE=" and FACTORYCODE like '%{}%' ".format(FACTORYCODE)
    if CreatedBy!='':CreatedBy=" and CreatedBy like '%{}%' ".format(CreatedBy)
    if START_TIME!='' and END_TIME!='':FBDATE=" and FBDATE between '{}' and '{}' ".format(START_TIME,END_TIME)

    query="""SELECT * FROM [SVREMPDATA] WHERE [emp_no] is not null  {}""".format(emp_no+deptname+FACTORYCODE+FBDATE+CreatedBy)
   
    sql=SelectSQL3(query)
    return sql


#Tìm kiếm thông tin lịch sử
def SEARCH_HISTORY(data):
    emp_no=data['emp_no'].upper()
    deptname=data['deptname'].upper()
    FACTORYCODE=data['FACTORYCODE'].upper()
    CreatedBy=data['CreatedBy'].upper()
    if emp_no!='':emp_no=" and emp_no ='{}' ".format(emp_no)
    if deptname!='':deptname=" and deptname like '%{}%' ".format(deptname)
    if FACTORYCODE!='':FACTORYCODE=" and FACTORYCODE = '{}' ".format(FACTORYCODE)
    if CreatedBy!='':CreatedBy=" and CreatedBy = '{}' ".format(CreatedBy)
        
    query="""SELECT * FROM [SVROOM_log] WHERE [emp_no]is not null {}""".format(emp_no+deptname+FACTORYCODE+CreatedBy)
    print(query)
    sql=SelectSQL3(query)
    return sql




#------------------------------------------------VIEW_SERVERRECORDS Nhật ký đi lại phòng máy chủ-----------------------------------------------------
#Lấy danh sách [FGATE]
def LIST_FGATE():
    query="""SELECT [FGATE],[FFACTORYCODE],[FBIP],[FBMAC] FROM [SVRMACHINE] """
    sql=SelectSQL3(query)
    return sql

#Lấy danh sách STATUS CARD
def GET_STATUS_CARD():
    query="SELECT DISTINCT [STATUS] FROM VIEW_SERVERRECORDS"
    return SelectSQL3(query)
    
    
#Lấy thông tin nhật ký vào ra
def GET_LOG_VIEW_SERVERRECORDS(data):
    query0=""
    for item in data:
        if data[item]!='' and 'INTIME' not in str(item):query0+=" and "+ str(item)+" like '%{}%' ".format(data[item])
   
    INTIME1=data['INTIME1']
    INTIME2=data['INTIME2']
    if INTIME1!='' and INTIME2!='':query0+="and INTIME between '{}' and '{}' ".format(INTIME1,INTIME2)  
    query="""SELECT * FROM [VIEW_SERVERRECORDS] WHERE [CARD_NO] is not null {} """.format(query0)
    sql=SelectSQL3(query)
    return sql

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------]








#----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------TỰ ĐỘNG SINH MÃ-------------------------------------------------------------------

#Lấy tên đơn tự động 
def CreatedCodeAuto(NameCol,NameTable):
    query="SELECT [Number],[Start],[Length] FROM AutoCode WHERE [NameCol] ='{}' and [NameTable] = '{}' ".format(NameCol,NameTable)
    number=SelectSQL3(query)
    #today =str(date.today().strftime("%Y"))
    #today = str(date.today().year)
    if len(number)>0:
        start=number[0]['Start']
        code=number[0]['Number']
        length=number[0]['Length']
        for x in range(int(length)-len(str(code))):code='0'+str(code)
    QuerySQL("UPDATE [AutoCode] set [Number]=[Number]+1 where [NameCol] ='{}' and [NameTable] = '{}'".format(NameCol,NameTable))
    return start+code


#----------------------------------------------------------------------------------------------------------------------------
#------------------------------------------Quản lý quyền hạn-------------------------------------------------------------------

#Lấy danh sách quyền hạn
def GET_LIST_PERMISSION(data):
    Code_Permission=data['Code_Permission']
    if Code_Permission!='':Code_Permission=" and Code_Permission='{}' ".format(Code_Permission)
    query="""SELECT * FROM [ListPermission] WHERE [Code_Permission] is not null {} """.format(Code_Permission)
    sql=SelectSQL3(query)
    return sql



#Kiểm tra nhóm quyền hạn đã tồn tại
def Check_PermissGroup_Exist(data):
    query="SELECT * FROM [ListPermission] WHERE Code_Permission='{}' ".format(data['Code_Permission'])
    sql=SelectSQL3(query)
    return sql



#Thêm mới danh sách nhóm quyền hạn
def INSERT_PERMISSION(data):
    #ListPermission=CreatedCodeAuto('Code','ListPermission')
    ListPermission=data['Code_Permission']
    query="""INSERT INTO [ListPermission]([Code_Permission],[Name_Permission],[Detail_Permission],[CreatedBy],[CreatedDate]) 
                VALUES(N'{}',N'{}',N'{}',N'{}',GETDATE()) 
    """.format(ListPermission,data['Name_Permission'],data['Detail_Permission'],data['user'])
    sql=QuerySQL(query)
    return sql



#Sửa danh sách nhóm quyền hạn
def UPDATE_PERMISSION(data):  
    query="""UPDATE [ListPermission] SET [Name_Permission]=N'{}',[Detail_Permission]=N'{}',[UpdatedBy]=N'{}',[UpdatedDate]=GETDATE() WHERE [Code_Permission]='{}'             
    """.format(data['Name_Permission'],data['Detail_Permission'],data['user'],data['Code_Permission'])
    sql=QuerySQL(query)
    return sql



#Xóa danh sách nhóm quyền hạn
def DEL_PERMISSION(data):  
    query="""DELETE [ListPermission] WHERE [Code_Permission]='{}'  """.format(data['Code_Permission'])
    sql=QuerySQL(query)
    return sql


#Check user log in is admin
def CHECK_ADMIN(request):
    user=request.user.get_username()
    sql=GET_PERMISSION_USER(user)
    if len(sql)>0:
        permiss=sql[0]['Name_Permission'].replace(" ",'').upper()
        if 'ADMIN' in permiss:return True
    return False
    
    
    
    
#--------------------------------------------Thao tác với [Modules] phân quyền sử dụng Menu----------------------------------------------------------

#Select Menu từ [Modules]
def SELECT_Modules(data):
    Code_Permission=data['Code_Permission']  
    query="""SELECT * FROM [Modules] WHERE [Code_Permission]='{}' """.format(Code_Permission)
    sql=SelectSQL3(query)
    return sql


#Insert [Modules]
def INSERT_Modules(data):  
    query="DELETE [Modules] WHERE [Code_Permission]='{}' ".format(data['Code_Permission'])   
    for item in data:
        if 'checkbox_' in str(item):                
            Code_Menu=str(item).replace("checkbox_","")                
            query+="""INSERT INTO [Modules]([Code_Permission],[Code_Menu],[CreatedDate],[CreatedBy])
                        VALUES(N'{}',N'{}',GETDATE(),N'{}')
                """.format(data['Code_Permission'],Code_Menu,data['user'])
    sql=QuerySQL(query)
    sql=SelectSQL3("SELECT * FROM [Modules] WHERE [Code_Permission]='{}' ".format(data['Code_Permission']))
    return sql


#--------------------------------------------Thao tác với [Menus] danh sách menu----------------------------------------------------------

#Lấy danh sách [Menus]
def GET_LIST_MENUS(data):    
    query="""SELECT * FROM [Menus] WHERE [Code_Menu] is not null"""
    sql=SelectSQL3(query)
    return sql


#Kiểm tra menu đã tồn tại
def Check_Menu_Exist(data):
    query="SELECT * FROM [Menus] WHERE [Code_Menu]='{}' ".format(data['Code_Menu'])
    sql=SelectSQL3(query)
    if len(sql)>0: return True
    else: return False


#Thêm mới [Menus]
def INSERT_MENUS(data):
    #Code_Menu=CreatedCodeAuto('Code','Menus')
    Code_Menu=data['Code_Menu']
    query="""INSERT INTO [Menus]([ID],[Code_Menu],[Name_Menu],[Url],[CreatedBy],[CreatedDate],[Groups_Menu])
                VALUES(NEWID(),N'{}',N'{}',N'',N'{}',GETDATE(),N'{}')
    """.format(Code_Menu,data['Name_Menu'],data['user'],data['Groups_Menu'])
    sql=QuerySQL(query)
    sql=SelectSQL3("SELECT * FROM [Menus]")
    return sql


#Sửa [Menus]
def UPDATE_MENUS(data):
    query="""UPDATE [Menus] SET [Name_Menu]='{}',[Url]='',[UpdatedDate]=GETDATE(),[UpdatedBy]=N'{}',[Groups_Menu]='{}'
                WHERE  [Code_Menu]='{}'
    """.format(data['Name_Menu'],data['user'],data['Code_Menu'],data['Groups_Menu'])
    sql=QuerySQL(query)
    sql=SelectSQL3("SELECT * FROM [Menus]")
    return sql


#Xóa [Menus]
def DEL_MENUS(data):  
    query="""DELETE [Menus] WHERE  [Code_Menu]='{}' """.format(data['Code_Menu'])
    sql=QuerySQL(query)
    sql=SelectSQL3("SELECT * FROM [Menus]")
    return sql





