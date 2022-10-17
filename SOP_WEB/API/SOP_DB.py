
from tabnanny import check
from API.API_MSSQL import QuerySQL2_SOP, QuerySQL_SOP, SelectSQL3_SOP
from datetime import date
import hashlib
from django.http import HttpResponse,JsonResponse


#Xử lý cắt chuỗi có dấu , ở cuối chuỗi
def Remove_comma_LastString(stringText):
    if stringText[len(stringText)-1:]==",":
        stringText=stringText[0:-1]
    return stringText


#Chuyển đổi QueryDict từ request về dictionary
def Convert_QueryDict_ToDict(data):
    return {x:data.get(x) for x in data.keys()} 

#------------------------------------------------------------------------------------------------------------------------------------------
#Lấy toàn bộ thông tin của 1 bảng bất kỳ theo điều kiện
def SELECT_TABLE(table_name,col_name,value_compare):
    query='''SELECT * FROM {} WHERE {} = '{}' '''.format(table_name,col_name,value_compare)
    return SelectSQL3_SOP(query)



#Phân tách chuối SQL khi dữ liệu truyền lên server là ''
def GET_CHUOI_SQL(data,tb):
    if tb!='': tb=str(tb)+'.'
    chuoi=''
    for item in data:
        tam=''
        if item=='StartDate' or item=='EndDate':continue
        if 'btn' in item:continue
        if data[item]=='':
            #tam='and {}.{} is not null '.format('d',item)
            tam=''
            chuoi+=tam  
        else: 
            tam= "and {}{} like '%{}%' ".format(tb,item,data[item])  
            chuoi+=tam

    if data['StartDate']=='' or data['EndDate']=='':pass
    else:chuoi+=" and {}CreatedDate between '{}:00.000' and '{}:00.000' ".format(tb,data['StartDate'],data['EndDate'])
    return chuoi;



#Lấy danh sách phòng ban bộ phận
def Get_Department(user):   
    query="exec sp_ListDepartmentInUser '{}' ".format(user)
    #print(query)
    return SelectSQL3_SOP(query)




#Lấy tên đơn tự động exec sp_CreatedCodeAuto 'Code','Roles'
def CreatedCodeAuto(NameCol,NameTable):
    query="SELECT [Number],[Start],[Length] FROM AutoCode WHERE [NameCol] ='{}' and [NameTable] = '{}' ".format(NameCol,NameTable)
    number=SelectSQL3_SOP(query)
    today =str(date.today().strftime("%Y"))
    today = str(date.today().year)
    if len(number)>0:
        start=number[0]['Start']
        code=number[0]['Number']
        length=number[0]['Length']
        for x in range(int(length)-len(str(code))):code='0'+str(code)   
    QuerySQL2_SOP("UPDATE [AutoCode] set [Number]=[Number]+1 where [NameCol] ='{}' and [NameTable] = '{}'".format(NameCol,NameTable))
    if "Document" in NameCol or  "RenewalCode" in NameCol:    return start+today+code
    else:    return start+code




# #Lấy tên đơn tự động exec sp_CreatedCodeAuto 'Code','Roles'
def CreatedCodeAuto1(NameCol,NameTable):
    query="SELECT [Code],[Start] FROM AutoCode WHERE [NameCol] ='{}' and [NameTable] = '{}' ".format(NameCol,NameTable)
    number=SelectSQL3_SOP(query)
    today =str(date.today().strftime("%Y%m%d"))+'000'
    if len(number)>0:
        try:
            start=number[0]['Start']
            code=number[0]['Code']
            length=number[0]['Length']
            
            if int(code)<int(today):number= today
            if int(code)>=int(today):number=str(int(code)+1)           
        except Exception as ex:number=today
        
    QuerySQL2_SOP("UPDATE [AutoCode] set [Code]= '{}' where [NameCol] ='{}' and [NameTable] = '{}'".format(number,NameCol,NameTable))

    return start+code



#Tạo dơn đăng ký mã hoặc cập nhật đơn đăng ký mã
def InsertRegisterCode(data):
    query='''exec sp_InsertRegisterCode '{}',N'{}',N'{}','{}',
                                        N'{}',N'{}',N'{}',N'{}','{}' 
        '''.format(data['CodeDocument'],data['CreatedBy'],data['ApplicationSite'],data['EffectiveDate'],
                    data['ReasonApplication'],data['ApplicableSite'],'',data['Department'],data['action'])
    # print(query)
    # return True
    return QuerySQL2_SOP(query)



#Tạo danh sách document Ref 
def InsertDocRef(data):
    QuerySQL2_SOP("DELETE DocumentRef WHERE CodeDocument='{}' ".format(data['CodeDocument']))
    data1=[]
    for i in range(0,int(data['list_docref_length'])):           
        data2={
            'OrderBy':data['list_docref[{}][OrderBy]'.format(i)],
            'DocumentName':data['list_docref[{}][DocumentName]'.format(i)],
            'FileName':data['list_docref[{}][FileName]'.format(i)],
            'EstimatedCloseDate':data['list_docref[{}][EstimatedCloseDate]'.format(i)],
        }
        data1.append(data2)
        
    for item in data1:
        query='''exec sp_InsertDocRef '{}',N'{}',N'{}','{}',N'{}','{}' 
            '''.format(data['CodeDocument'],item['DocumentName'],item['FileName'],item['EstimatedCloseDate'],data['CreatedBy'],item['OrderBy'])
        # print(query)
        sql=QuerySQL2_SOP(query)
        if sql!=True: return sql
    return True

    
    
    
#Chèn lưu trình ký
def InsertApprovalSection(data):
    query='''exec sp_InsertApprovalSection '{}',N'{}','{}' '''.format(data['CodeDocument'],data['CreatedBy'],data['Department'])
    # print(query)
    # return True
    return QuerySQL2_SOP(query)


#Lấy vị trị cấp nhân viên đang chờ ký
def GetTypeOrdersApprover(CodeDocument):
    query='''select top 1 Orders from ApprovalSection
            where CodeDocument='{}' and UpdatedDate is null
            order by Orders
            '''.format(CodeDocument)  
   # print(query)
    return SelectSQL3_SOP(query)



#Lấy giá trị chờ ký
def GET_Orders_Appro(number):
    list={
        '1':'A01',
        '5':'A03',#Chủ quản bộ phận
        '30':'A05',#Chủ quản phòng
        '31':'A05',#Chủ quản phòng
        '50':'A15',#DCC xác nhận
        '':"A20"#A20 = làm lại đơn
    }
    #Trả tiến lên 1 bước
    if int(number)<=5: return 'A05'
    if int(number)<=31: return 'A05'
    if int(number)==50: return 'A15'
    if int(number)<1: return 'A20'

   


#Lấy danh sách lưu trình ký
def ListApprovalSection(CodeDocument):
    query="""
        --Tạo bảng nháp
        IF OBJECT_ID(N'tempdb..#Temp') IS NOT NULL BEGIN DROP TABLE  #Temp END
        
            BEGIN
                declare @CodeDocument varchar(50)='{}'       
                declare @Department varchar(50)
                declare @ColName varchar(100)
                declare @TableName varchar(100)
                declare @sql nvarchar(max)
                
                if @CodeDocument like '%SOP-A%' begin set @TableName=' [RegisterCodeDocument]' set @ColName='[CodeDocument]' end
                if @CodeDocument like '%SOP-B%' begin set @TableName=' [RegisterEditDocument]' set @ColName='[EditDocument]' end
                if @CodeDocument like '%SOP-C%' begin set @TableName=' [RegisterPublishDocument]' set @ColName='[PublishDocument]' end
                if @CodeDocument like '%SOP-D%' begin set @TableName=' [ApplicationObsoletedDocument]' set @ColName='[ObsoletedDocument]' end
                if @CodeDocument like '%SOP-G%' begin set @TableName=' [RegisterCancelDocument]' set @ColName='[CancelDocument]' end
                			

                set @sql=N'
                  SELECT t.*,c1.CatName
                    FROM
                    (
                    select  ROW_NUMBER() Over(order by a.orders) STT,a.Status as Status1,
                        (case when DATEDIFF(HOUR,a.CreatedDate,a.UpdatedDate) > 0
                            then  DATEDIFF(HOUR,a.CreatedDate,a.UpdatedDate)
                            else 0 end ) Times,
                        a.CreatedDate,a.Station,(select top 1 Department from UserInDepartment WHERE UserName=a.UserName) Dept,a.UserName,u.HoTen Name,u.SoDienThoai Ext,
                        c.CatName Status,ISNULL(a.Comment,'''') Comment,a.UpdatedDate,a.Orders
                        from ApprovalSection a
                        inner join Users u on a.UserName = u.TenDangNhap
                        inner join Categorys c on a.Status = c.CatCode
                        where a.CodeDocument ='''+@CodeDocument+''') as t  
                    inner join Categorys c1 on t.Dept=c1.CatCode
                    Order by t.Orders'

                exec(@sql)
             
            END
            

        """.format(CodeDocument)
    # print(query)       
    # query='''exec sp_ListApprovalSection '{}' '''.format(CodeDocument)
    return SelectSQL3_SOP(query)



#Lấy danh sách file đính kèm
def ListDocRef(CodeDocument):
    query="SELECT * FROM [DocumentRef] WHERE [CodeDocument]='{}'".format(CodeDocument)
    
    if 'SOP-A' in CodeDocument:
        query="SELECT * FROM [DocumentRef] WHERE [CodeDocument]='{}'".format(CodeDocument)
     
    if 'SOP-B' in CodeDocument:
        query='''SELECT *   FROM [PublishReff] 
                    where PublishDocument='{}'
                    '''.format(CodeDocument)                    
    if 'SOP-C' in CodeDocument:
        query='''SELECT * FROM  [RegisterPublishDocument] as ed
                    inner JOIN PublishReff as pf on ed.PublishDocument=pf.PublishDocument
                    WHERE ed.PublishDocument='{}' order by pf.OrderBy
                    '''.format(CodeDocument)       
    if 'SOP-D' in CodeDocument:
        query='''SELECT * FROM  RenewalsDocument as ed
                    RIGHT JOIN DocumentRef as df on ed.DocumentNo=df.CodeDocument
                    WHERE ed.RenewalCode='{}'
                    '''.format(CodeDocument)
    if 'SOP-G' in CodeDocument:
        query='''SELECT * FROM  RegisterCancelDocument as ed
                    RIGHT JOIN DocumentRef as df on ed.ApplicationNo_Code=df.CodeDocument
                    WHERE ed.CancelDocument='{}'
                    '''.format(CodeDocument)    
                    
    return SelectSQL3_SOP(query)
        

        
#Hiển thị thông tin đơn văn kiện
def Detail_CodeDocument(table_Document,col_CodeDocument,CodeDocument):
            
    query="SELECT * FROM [{}] WHERE [{}]='{}'".format(table_Document,col_CodeDocument,CodeDocument)
                        
    if 'SOP-G' in CodeDocument:
        query='''SELECT rd.*,dr.EstimatedCloseDate,dr.DocumentName
                    FROM [RegisterCancelDocument] as rd
                    INNER JOIN DocumentRef as dr on rd.ApplicationNo_Code=dr.CodeDocument
                    where rd.CancelDocument='{}' 
                    '''.format(CodeDocument)
                
    if "SOP-D" in CodeDocument:
        query='''SELECT ad.*,rd.DocumentNo,rd.DocumentName,rd.EffectiveDate as EffectiveDate1,rd.Rev,rd.ApplicationSite,dp.Department,u1.Hoten as Applicant,
                (SELECT top 1 u.Hoten FROM UserInPosition as p 
                    inner join UserInDepartment as d on p.UserName=d.UserName and d.Department=dp.Department 
                    inner join Users as u on p.UserName=u.TenDangNhap
                    where Position='C-00004' ) as Hoten
                FROM [ApplicationObsoletedDocument] as ad
                INNER JOIN RegisterPublishDocument as rd on ad.PublishDocument=rd.PublishDocument
                left outer JOIN UserInDepartment as dp on ad.CreatedBy=dp.UserName
                left outer JOIN Users as u1 on ad.CreatedBy=u1.TenDangNhap
                where  ad.ObsoletedDocument='{}'
                    '''.format(CodeDocument)                    
    return SelectSQL3_SOP(query)




#Lấy thông tin người chờ ký: trả về 1 recode: UserName
def Get_waiting_approver(CodeDocument):
    query='''select top 1 UserName from ApprovalSection
            where CodeDocument='{}' and UpdatedDate is null
            order by Orders
            '''.format(CodeDocument)  
    return SelectSQL3_SOP(query)



#Lấy mã thẻ người làm đơn: trả về 1 recode: UserName
def Get_Applicant(CodeDocument):
    query='''select top 1 UserName from ApprovalSection
            where CodeDocument='{}' and Orders='1'
            order by Orders
            '''.format(CodeDocument)  
    return SelectSQL3_SOP(query)



#Kiểm tra user có phải là DCC
def Check_IsDCC(TenDangNhap):
    query="""SELECT * FROM Users WHERE TenDangNhap='{}' and DCC ='1' """.format(TenDangNhap)
    sql=SelectSQL3_SOP(query)
    if len(sql)>0:return True
    else: return False
    
    
    

#Thủ tục Ký duyệt hoặc hủy đơn CodeDocument,Comment,States,User,Action
def sp_ApproOrCancelApprovalSection(data):
    query="""
        BEGIN
            declare @CodeDocument varchar(50)='{}'
            declare @Comment varchar(500)=N'{}'
            declare @States varchar(20)='{}'
            declare @User varchar(50)='{}'
            declare @Action varchar(50)='{}'  
            
            declare @DocNo varchar(50)='{}'  
            declare @DocName varchar(500)=N'{}'

            declare @sql as nvarchar(max)
            declare @TableName varchar(100)
            declare @ColName varchar(100)
            declare @Status varchar(50)  
            
            --Thao tác ký đơn
            if @Action='APPRO'	begin set @Status='C-00010'	end
            
            --Thao tác hủy đơn
            if (@Action='CANCEL') begin set @Status='C-00011' end
            
            
            --Thưc hiện cập nhật tình trạng ký hoặc hủy đơn	
            set @sql=''
            if @CodeDocument like '%SOP-A%' begin set @TableName=' [RegisterCodeDocument]' set @States='A'+SUBSTRING(@States,2,2) set @ColName='[CodeDocument]' end
            if @CodeDocument like '%SOP-B%' begin set @TableName=' [RegisterEditDocument]' set @States='B'+SUBSTRING(@States,2,2) set @ColName='[EditDocument]' end
            if @CodeDocument like '%SOP-C%' begin set @TableName=' [RegisterPublishDocument]' set @States='C'+SUBSTRING(@States,2,2) set @ColName='[PublishDocument]' end
            if @CodeDocument like '%SOP-D%' begin set @TableName=' [ApplicationObsoletedDocument]' set @States='D'+SUBSTRING(@States,2,2) set @ColName='[ObsoletedDocument]' end
            if @CodeDocument like '%SOP-G%' begin set @TableName=' [RegisterCancelDocument]' set @States='G'+SUBSTRING(@States,2,2) set @ColName='[CancelDocument]' end			
            
            -- Cập nhật trạng thái  ký cho bảng lưu trình ký
            UPDATE [ApprovalSection]
            		SET Comment=@Comment,Status=@Status,UpdatedDate=GETDATE(),UpdatedBy=@User
            		WHERE CodeDocument=@CodeDocument and UserName=@User

            --Nếu là DCC và đơn là SOP-A và người ký hêt thì thực hiện chèn mã văn bản DCC cấp cho đơn
            declare @IsDCC varchar(2)='0'
            SELECT @IsDCC=DCC FROM Users WHERE TenDangNhap=@User            
            if (@CodeDocument like '%SOP-A%' and  @IsDCC ='1') begin exec [InsertDCC_Ref] @DocNo,@DocName,@User,@CodeDocument end
            
            -- Cập nhật State cho đơn theo bảng của mỗi loại đơn
            set @sql+=N'UPDATE'+ @TableName +'
                    SET [States] ='''+@States+''',[UpdatedBy]='''+@User+''',[UpdatedDate]=GETDATE()
                    WHERE '+@ColName+' ='''+@CodeDocument+''''
                --print(@sql)
            exec(@sql)
            
        END
        """.format(data['CodeDocument'],data['Comment'],data['States'],data['User'],data['Action'],data['DocNo'],data['DocName'])
    print(query)
        # .format(CodeDocument,Comment,States,User,Action)
    # print(query)
    sql=QuerySQL2_SOP(query)
    return sql
        

#---------------------------------------------THAO TÁC USER--------------------------------------------------------
#Thêm sửa xóa User
def ACTION_USER(data,EditBy): 
    passreset=hashlib.md5('foxconn168!!'.encode()).hexdigest().upper()   
    Action=''
    TenDangNhap=''
    passw=''
    HoTen=''
    Email=''
    SoDienThoai=''
    DCC=''
    IsLocked=''
    CodeRole=''
    try:TenDangNhap=data['TenDangNhap'].replace(" ","").upper()
    except:TenDangNhap=''
    try:
        password=data['pass1id']
        password1=data['pass2id']
        if password!='' : passw = hashlib.md5(password.encode()).hexdigest().upper()        
    except: passw =''
    try:
        Action=data['Action']
        if Action=='RESET':passw=passreset
        elif Action=='CREATE' and password=='': passw=passreset
        elif Action=='CREATE' and password!='': passw = hashlib.md5(password.encode()).hexdigest().upper()
        elif Action=='UPDATE' and password=='': passw=password
        elif Action=='UPDATE' and password!='': passw = hashlib.md5(password.encode()).hexdigest().upper()    
    except:Action=''
    try:HoTen=data['HoTen'] 
    except:HoTen=''
    try:Email=data['Email'] 
    except:Email=''
    try:SoDienThoai=data['SoDienThoai'] 
    except:SoDienThoai=''
    try:
        DCC=data['DCC']        
    except:DCC='0'
    try:IsLocked=data['IsLocked'] 
    except:IsLocked='0'
    try:CodeRole=data['CodeRole'] 
    except:CodeRole=''

    query="""
        -- Khai báo biến
        declare @Action nvarchar(50)='{}'
        declare @TenDangNhap nvarchar(50)=N'{}'
        declare @MatKhau nvarchar(50)=N'{}'
        declare @HoTen nvarchar(50)=N'{}'
        declare @NguoiSua nvarchar(50)=N'{}'
        declare @Email nvarchar(100)=N'{}'
        declare @SoDienThoai nvarchar(50)='{}'
        declare @DCC nvarchar(50)='{}'
        declare @IsLocked nvarchar(50)='{}'
        declare @CodeRole nvarchar(50)='{}'
        declare @Quyen nvarchar(50)=''
        declare @sql nvarchar(max)=N'DELETE Users WHERE [TenDangNhap]='''+@TenDangNhap+'''
                                DELETE UserInDepartment WHERE [UserName]='''+@TenDangNhap+'''
                                DELETE [UserInPosition] WHERE [UserName]='''+@TenDangNhap+'''
                                DELETE [UsersInRoles] WHERE [UserName]='''+@TenDangNhap+''''
                    
        -- Phân biệt quyền hạn
        IF @CodeRole='R-00001' begin set @Quyen='Admin' end
        ELSE IF @CodeRole='R-00022' begin set @Quyen='DCC' end
        ELSE IF @CodeRole='R-00039' begin set @Quyen='Visitor' end
        ELSE IF @CodeRole='R-00002' begin set @Quyen='Staff' end
        ELSE IF @CodeRole='R-00030' begin set @Quyen='Test' end
        ELSE IF @CodeRole='R-00014' begin set @Quyen='Manager' end
                        
        --Thêm tài khoản người dùng
        IF (@Action = 'CREATE')
            BEGIN
                -- Kiểm tra nếu password  trống thì cho pass mặc định
                -- Xóa toàn bộ thông tin user trong các bảng
                exec(@sql)
                
                -- Chèn dữ liệu vào bảng Users
                INSERT INTO [Users]([ID],[TenDangNhap],[MatKhau],[HoTen],[Quyen],[NgayTao],[NguoiTao],[NgaySua],[NguoiSua],[NgayXoa],[NguoiXoa]
                            ,[IsDeleted],[IsLocked],[TrangThai],[NguoiLamThay],[Email],[SoDienThoai],[DCC])
                VALUES(NEWID(),@TenDangNhap,@MatKhau,@HoTen,@Quyen,GETDATE(),@NguoiSua,null,null,null,null,'0','0',null,null,@Email,@SoDienThoai,@DCC)
            
                -- Chèn quyền hạn người dùng
                INSERT INTO [UsersInRoles]([ID],[UserName],[CodeRole],[CreatedBy],[CreatedDate])
                VALUES(NEWID(),@TenDangNhap,@CodeRole,@NguoiSua,GETDATE())
            END
        
        --Cập nhật thông tin tài khoản người dùng bao gồm khóa và thay đổi
        ELSE IF (@Action = 'UPDATE')
            BEGIN
                if @MatKhau=''
                    BEGIN
                        UPDATE Users set [HoTen]=@HoTen,[Quyen]=@Quyen,[NgaySua]=GETDATE(),[NguoiSua]=@NguoiSua
                                    ,[IsLocked]=@IsLocked,[Email]=@Email,[SoDienThoai]=@SoDienThoai,[DCC]=@DCC
                        WHERE [TenDangNhap]=@TenDangNhap
                    END
                if  @MatKhau!=''
                    BEGIN
                        UPDATE Users set [MatKhau]=@MatKhau,[HoTen]=@HoTen,[Quyen]=@Quyen,[NgaySua]=GETDATE(),[NguoiSua]=@NguoiSua
                                    ,[IsLocked]=@IsLocked,[Email]=@Email,[SoDienThoai]=@SoDienThoai,[DCC]=@DCC
                        WHERE [TenDangNhap]=@TenDangNhap
                    END
                
                -- Chèn quyền hạn người dùng
                DELETE [UsersInRoles]  WHERE [Username]=@TenDangNhap
                INSERT INTO [UsersInRoles]([ID],[UserName],[CodeRole],[CreatedBy],[CreatedDate])
                VALUES(NEWID(),@TenDangNhap,@CodeRole,@NguoiSua,GETDATE())                
            END
        
        -- Reset Password
        ELSE IF (@Action = 'RESET') BEGIN UPDATE Users set [MatKhau]=@MatKhau END
        
        --Xóa thông tin tài khoản
        ELSE IF (@Action = 'DELETE') BEGIN exec(@sql) END
    
    """.format(Action,TenDangNhap,passw,HoTen,EditBy,
               Email,SoDienThoai,DCC,IsLocked,CodeRole)
    # print(query)
    return QuerySQL2_SOP(query)


#Cài đặt chức vụ vị trí (truyền vào Poision="a,b,c,d,")
def ADD_POISISION_USER(data,EditBy):
    sql=QuerySQL2_SOP("DELETE [UserInPosition] WHERE [UserName]='{}' ".format(data['TenDangNhap']))
    Poisition=''
    for item in data:
        if 'Poisition' in item:Poisition=Poisition+data[item]+","   
    Poisition=Poisition[0:-1].split(',')
    for poisitio in Poisition:
        query="""
            declare @Username varchar(50)='{}'
            declare @Position varchar(50)='{}'
            declare @NguoiSua varchar(50)='{}'
            
            -- Chèn dữ liệu vào bảng [UserInPosition] 
            INSERT INTO [UserInPosition]([ID],[UserName],[Position],[CreatedBy],[CreatedDate])
            VALUES (NEWID(),@Username,@Position,@NguoiSua,GETDATE())
            """.format(data['TenDangNhap'],poisitio,EditBy)
        # print(query)
        sql=QuerySQL_SOP(query)
        
        
#Cài đặt bộ phận UserInDepartment(truyền vào Department="a,b,c,d,")
def ADD_DEPARTMENT_USER(data,EditBy):
    sql=QuerySQL2_SOP("DELETE [UserInDepartment] WHERE [UserName]='{}' ".format(data['TenDangNhap']))
    Department=''
    for item in data:
        if 'Department' in item:Department=Department+data[item]+","    
    Department=Department[0:-1].split(',')
    for dept in Department:
        query="""
            declare @Username varchar(50)='{}'
            declare @Department varchar(50)='{}'
            declare @NguoiSua varchar(50)='{}'
            
            -- Chèn dữ liệu vào bảng [UserInDepartment]
            INSERT INTO [UserInDepartment]([ID],[UserName],[Department],[CreatedBy],[CreatedDate])
            VALUES (NEWID(),@Username,@Department,@NguoiSua,GETDATE())
            """.format(data['TenDangNhap'],dept,EditBy)
        sql=QuerySQL_SOP(query)


#Cài đặt chủ quản phòng
def ADD_MANAGER_ROOM(data,EditBy):
    QuerySQL2_SOP("DELETE Manager_Room WHERE Username='{}' ".format(data['TenDangNhap']))
    if data['Manager_Room']=='': return False
    Manager_Room=data['Manager_Room'][0:-1].split(',')
    for manager in Manager_Room:
        manager=manager[0:manager.rindex('_')].replace(" ",'')
        
        query="""
            declare @Username nvarchar(50)='{}'
            declare @Username_Manager nvarchar(50)='{}'
            declare @NguoiSua nvarchar(50)='{}'
            
            -- Chèn dữ liệu vào bảng [Manager_Room]
            INSERT INTO [Manager_Room]([ID],[UserName],[Username_Manager],[CreatedBy],[CreatedDate])
            VALUES (NEWID(),@Username,@Username_Manager,@NguoiSua,GETDATE())
            """.format(data['TenDangNhap'],manager,EditBy)
        print(query)
        sql=QuerySQL_SOP(query)

    
#Lấy danh sách Department(CatCode	CatName	CatTypeCode	Code :C-00012	越南工務  / cong vu TW	CT-00002	CVTW)
def Load_Dept(request):
    query="""select CatCode,CatName,CatTypeCode,Code from Categorys where [CatTypeCode]='CT-00002'  and IsDeleted=0 order by  CatCode"""
    sql=SelectSQL3_SOP(query)
    return JsonResponse({'returndata':sql},status=200)


#Lấy danh sách Chức vụ  quyền hạn(CatCode	CatName	CatTypeCode	Code :CatCode	CatName	CatTypeCode	Code	Orders :C-00003	員工 Nhân Viên	CT-00001	NULL	1)
def Load_permissgroup(request):
    try:
        query="""select CatCode,CatName,CatTypeCode,Code from Categorys where [CatTypeCode]='CT-00001'  and IsDeleted=0 order by  CatCode"""
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex:    return JsonResponse({"error":str(ex)}, status = 400)


#Lấy danh sách quản lý phòng ban cho 1 tài khoản
def Load_manager_room(request):
    try:
        data=request.GET
        query=""" select m.Username,m.Username_Manager,u.HoTen
                    from Manager_Room as m
                    left join Users as u on m.Username_Manager=u.TenDangNhap
                    where m.Username='{}' """.format(data['TenDangNhap'])
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex:    return JsonResponse({"error":str(ex)}, status = 400)
     

#Lấy danh sách quản lý phòng ban
def Load_list_manager_room(request):   
    try:
        query="""  select d.UserName,d.Department,c1.CatName as Department1,u.HoTen,p.Position,c.CatName as Poisition1
                    from UserInDepartment as d
                    inner join Users as u on d.UserName=u.TenDangNhap
                    inner join UserInPosition as p on d.UserName=p.UserName
                    inner join Categorys as c on p.Position=c.CatCode
                    inner join Categorys as c1 on d.Department=c1.CatCode
                    where p.Position in ('C-00053','C-00004') order by Poisition1 """
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex:    return JsonResponse({"error":str(ex)}, status = 400)


#Lấy thông tin tài khoản hiển thị modal
def Show_TendangnhapInfo(request):
    try:
        data=request.GET
        sql1=SelectSQL3_SOP("""SELECT u.*,r.CodeRole,c.Name as CodeRole1  FROM Users as u
                            left join UsersInRoles as r on u.TenDangNhap=r.UserName
                            left join Roles as c on r.CodeRole=c.Code
                            WHERE TenDangNhap='{}' """.format(data['TenDangNhap']))#Thông tin người dùng
        sql2=SelectSQL3_SOP("SELECT * FROM [UserInDepartment] WHERE [UserName]='{}' ".format(data['TenDangNhap']))#Thông tin phòng ban
        sql3=SelectSQL3_SOP("""select p.UserName,p.Position,c.CatName
                            from UserInPosition as p 
                            inner join Categorys as c on p.Position=c.CatCode
                            where p.UserName='{}' """.format(data['TenDangNhap']))#Thông tin chức vụ
        sql4=SelectSQL3_SOP("""SELECT m.*,u.HoTen FROM [Manager_Room] as m
                            left join Users as u on m.[Username_Manager]=u.TenDangNhap
                            WHERE [UserName]='{}' """.format(data['TenDangNhap']))#Thông tin quản lý phòng
        data={'sql1':sql1,'sql2':sql2,'sql3':sql3,'sql4':sql4}    
        return JsonResponse({'returndata':data},status=200)
    except Exception as ex:    return JsonResponse({"error":str(ex)}, status = 400)




#Tạo yêu cầu công văn [RegisterDocumentArrive]
def Insert_RegisterDocumentArrive(data,user):
    current_year = date.today().year
    #print(current_year)
    Sodon='SOP-H-'+ CreatedCodeAuto('ArriveDocument','RegisterArriveDocumnet')    
    query="""INSERT INTO [RegisterDocumentArrive](ID,[Loaicongvan],[Sodon],[Nguoitrinhdon],[Ngaynhanvankien],[Sobiennhan]
      ,[NgaytrinhkyGD],[Sovankien],[Noidungcongvan],[Donvichusu],[Donvihopban],[Vanbanphuluc]
      ,[Ghichu],[Chondvkhac],[Donvikhac],[TepscanPDF],[Tepvbtraloi]
      ,[Dongsauhop],[Traloivanban],[Thoigianxuly],[Ykienkhac],[Status])
      VALUES(NEWID(),N'{}',N'{}',N'{}',N'{}',N'{}',
        GETDATE(),N'{}',N'{}',N'{}',N'{}',N'{}',
                N'{}',N'{}',N'{}',N'{}',N'{}',
                N'{}',N'{}',null,N'{}','Waiting')
      """.format(data['Loaicongvan'],Sodon,user,data['Ngaynhanvankien'],
                 data['Sobiennhan'],data['Sovankien'],data['Noidungcongvan'],data['Donvichusu'][0:-1],data['Donvihopban'][0:-1],
                 data['Vanbanphuluc'],data['Ghichu'],data['Chondvkhac'],data['Donvikhac'],data['TepscanPDF'],data['Tepvbtraloi'],data['Dongsauhop'],data['Traloivanban'],
                 data['Ykienkhac'])
    #print(query)
    sql= QuerySQL_SOP(query)
    return Sodon
    

#Lấy danh sách công văn
def Search_SOP_H(data):
    Sodon=data['Sodon']
    Sovankien=data['Sovankien']
    Nguoitrinhdon=data['Nguoitrinhdon']
    Donvichusu=data['Donvichusu']
    StartDate=data['StartDate']
    FromDate=data['FromDate']
    NgaytrinhkyGD=''
    if Sodon!='':Sodon=" and Sodon='{}' ".format(Sodon)
    if Sovankien!='':Sovankien=" and Sovankien='{}' ".format(Sovankien)
    if Nguoitrinhdon!='':Nguoitrinhdon=" and Nguoitrinhdon='{}' ".format(Nguoitrinhdon)
    if Donvichusu!='':Donvichusu=" and Donvichusu='{}' ".format(Donvichusu)
    if StartDate!='' and  FromDate!='':NgaytrinhkyGD=" and [NgaytrinhkyGD] between '{}' and '{}' ".format(StartDate,FromDate)
    elif StartDate!='' and  FromDate=='':NgaytrinhkyGD=" and [NgaytrinhkyGD] = '{}' ".format(StartDate)
    elif StartDate=='' and  FromDate!='':NgaytrinhkyGD=" and [NgaytrinhkyGD] = '{}' ".format(FromDate)
    
    query="""SELECT * FROM [RegisterDocumentArrive] 
                WHERE Sodon is not null {}
          """.format(str(Sodon)+str(Sovankien)+str(Nguoitrinhdon)+str(Donvichusu)+str(StartDate)+str(FromDate))
    sql=SelectSQL3_SOP(query)
    # print(sql)
    return sql


#Chi tiết 1 công văn
def Detail_HOC_H(data):
    query="""SELECT * FROM [RegisterDocumentArrive] WHERE Sodon='{}' """.format(data['Sodon'])
    sql=SelectSQL3_SOP(query)
    return sql


#Lấy danh sách đơn đang chờ ký cho tài khoản đăng nhập
def Get_ListWaiting_ForAppro(request):
    user=request.user.get_username()
    query="""SELECT * FROM [RegisterDocumentArrive] WHERE [Next_appro]='{}' and [Status]='Waiting' """.format(user)
    #print(query)
    sql=SelectSQL3_SOP(query)
    return sql



#Lấy thông tin mail hệ thống
def Get_MailSystem():
    return SelectSQL3_SOP("Select CatCode,CatName from Categorys where CatCode='C-00041'")[0]['CatName']
    
    
    
#Tạo lưu trình ký của công văn
def Create_SectionApproArr(request,Sodon):
    user=request.user.get_username()
    query="""
        DECLARE @CodeDocument as nvarchar(20)='{}'
        DECLARE @TongGiamDoc as nvarchar(20)=''
        DECLARE @HoTroGiamDoc as nvarchar(20)=''
        DECLARE @UserName as nvarchar(20)='{}'
        
        --Xóa toàn bộ chữ ký nếu lỗi
        DELETE [ApprovalSection_Arr] WHERE CodeDocument=@CodeDocument
        
        --Chèn người ký tạo đơn
        INSERT INTO [ApprovalSection_Arr]
            ([ID],[CodeDocument],[UserName],[Station],[IsCheck],[Comment],[CreatedBy],[CreatedDate],[Orders],[Time],[Status])
            VALUES(NEWID(),@CodeDocument,@UserName,N'申請人','Y','',@UserName,GETDATE(),'0',GETDATE(),'Passed')
        
        --Chèn chữ ký hỗ trợ chủ quản
        SELECT TOP 1 @HoTroGiamDoc=[HoTroGiamDoc]  FROM [Zongjingli]
        if @HoTroGiamDoc<>'' 
            Begin
                INSERT INTO [ApprovalSection_Arr]
                ([ID],[CodeDocument],[UserName],[Station],[IsCheck],[Comment],[CreatedBy],[CreatedDate],[Orders],[Status])
                VALUES(NEWID(),@CodeDocument,@HoTroGiamDoc,N'主管審核','N','',@UserName,GETDATE(),'1','')
                UPDATE [RegisterDocumentArrive] SET [Next_appro]=@HoTroGiamDoc Where Sodon=@CodeDocument
            End
        else 
            begin
                --Cập nhật người ký tiếp theo trong bảng chi tiết đơn
                UPDATE [RegisterDocumentArrive] SET [Next_appro]=@TongGiamDoc Where Sodon=@CodeDocument
            end
            
        --Chèn chữ ký giám đốc
        SELECT TOP 1 @TongGiamDoc=[TongGiamDoc]  FROM [Zongjingli]
        INSERT INTO [ApprovalSection_Arr]
            ([ID],[CodeDocument],[UserName],[Station],[IsCheck],[Comment],[CreatedBy],[CreatedDate],[Orders],[Status])
            VALUES(NEWID(),@CodeDocument,@TongGiamDoc,N'主管核准','N','',@UserName,GETDATE(),'2','')   
    """.format(Sodon,user)
    sql=QuerySQL2_SOP(query)
    if sql:
        #Lấy Email người ký tiếp theo (chủ quản phê duyệt)
        query="""SELECT TOP 1 a.CodeDocument,a.UserName,u.HoTen,u.Email,a.IsCheck,a.Orders FROM [ApprovalSection_Arr] as a
                INNER JOIN Users as u on a.UserName=u.TenDangNhap
                WHERE CodeDocument='{}' and IsCheck!='Y'
                Order by Orders
                """.format(Sodon)
        return SelectSQL3_SOP(query)
    return []



#Kiểm tra người ký có phải là Tổng giám đốc
def Check_WaitngAppro_TGD(request):
    data=request.GET
    user=request.user.get_username()
    query=""" --Lấy thông tin mã thẻ tổng giám đốc
            Declare @TongGiamDoc as nvarchar(10)='' 
            Declare @UserName as nvarchar(10)='{}'
            SELECT TOP 1 @TongGiamDoc=[TongGiamDoc]  FROM [Zongjingli]
            if @TongGiamDoc=@UserName
                Begin
                    SELECT [Next_appro] FROM [RegisterDocumentArrive] 
                    WHERE [Sodon]='{}' and [Status]='Waiting' and [Next_appro]=LTRIM(RTRIM(@TongGiamDoc))
                End
            else
                Begin
                    SELECT [Next_appro] FROM [RegisterDocumentArrive] WHERE [Sodon]=''
                End
        
        """.format(user,data['Sodon'])
  
    Check=SelectSQL3_SOP(query)    
    if len(Check)>0: return True
    else : return False



#Lấy danh sách chữ ký
def Get_ListApproSection(data):
    CodeDocument=data['Sodon']
    query="""SELECT a.*,u.HoTen,u.SoDienThoai,d.Department,c.CatName as Department1
                FROM [ApprovalSection_Arr] as a
                LEFT JOIN Users as u on a.UserName=u.TenDangNhap
                LEFT JOIN [UserInDepartment] as d on a.UserName=d.UserName
                LEFT JOIN Categorys as c on d.Department=c.CatCode
                WHERE [CodeDocument]='{}'
            """.format(CodeDocument)
    return SelectSQL3_SOP(query)



#Lấy danh sách người nhận mail sau khi giám đốc ký phê duyệt
def Get_List_Mail_Send(data):
    Donvichusu=Remove_comma_LastString(data['Donvichusu'])
    Donvihopban=Remove_comma_LastString(data['Donvihopban'])
    
    Donvichusu=Donvichusu.split(',')
    Donvihopban=Donvihopban.split(',')
    
    #Lấy danh sách mail đơn vị chủ sự
    chusu=''
    for item in Donvichusu:
        chusu+="'"+item+"',"
    chusu=Remove_comma_LastString(chusu)
    query_mail_chusu="""SELECT '{}' as CodeDocument,d.UserName,u.Email,d.Manager,u1.Email as Email1,
                            CASE WHEN u.Email is not null and u1.Email is not null Then (u.Email+','+u1.Email)
                                    WHEN u.Email is null and u1.Email is not null Then u1.Email
                                    WHEN u.Email is not null and u1.Email is null Then u.Email
                            END as MailTo 
                        FROM Dept_Arrive as d
                        LEFT JOIN Users as u on d.UserName=u.TenDangNhap
                        LEFT Join Users as u1 on d.Manager =u1.TenDangNhap
                        WHERE d.Department in ({})
            """.format(data['Sodon'],chusu)
    #print(query_mail_chusu)
    Mail_Chusu=SelectSQL3_SOP(query_mail_chusu)
    MailTo=''    
    if len(Mail_Chusu)>0:        
        for item in Mail_Chusu:
            MailTo+=item['MailTo']+','
    MailTo=Remove_comma_LastString(MailTo)
    print(MailTo)    
    
    #Lấy danh sách mail đơn vị hỗ trợ
    hotro=''
    for item in Donvihopban:
        hotro+="'"+item+"',"
    hotro=Remove_comma_LastString(hotro)     
    query_mail_hotro="""SELECT '{}' as CodeDocument,d.UserName,u.Email,d.Manager,u1.Email as Email1,
                            CASE WHEN u.Email is not null and u1.Email is not null Then (u.Email+','+u1.Email)
                                    WHEN u.Email is null and u1.Email is not null Then u1.Email
                                    WHEN u.Email is not null and u1.Email is null Then u.Email
                            END as MailCC 
                        FROM Dept_Arrive as d
                        LEFT JOIN Users as u on d.UserName=u.TenDangNhap
                        LEFT Join Users as u1 on d.Manager =u1.TenDangNhap
                        WHERE d.Department in ({})
            """.format(data['Sodon'],hotro)
    Mail_Hotro=SelectSQL3_SOP(query_mail_hotro)
    MailCC=''    
    if len(Mail_Hotro)>0:
        for item in Mail_Hotro:
            MailCC+=item['MailCC']+','
    MailCC=Remove_comma_LastString(MailCC)
    
    if Mail_Chusu!='' or Mail_Hotro!='':
        context={'MailTo':MailTo,'MailCC':MailCC}
        print(context)
        return context
    else: return False
    
    
    
#Cập nhật chữ ký người ký đơn
def Update_ApproSection(request):
    user=request.user.get_username()
    data=request.GET
    Donvichusu=data['Donvichusu']
    Donvihopban=data['Donvihopban']    
    if ',' in Donvichusu:Donvichusu=Donvichusu[0:-1]
    if ',' in Donvihopban:Donvihopban=Donvihopban[0:-1]    
   
    TGD_Check= Check_WaitngAppro_TGD(request)
    
    query="""            
            Declare @CodeDocument as nvarchar(20) ='{}'
            Declare @UserName as nvarchar(20) =N'{}'
            Declare @TongGiamDoc as nvarchar(20) =''
            Declare @Donvichusu as nvarchar(500) =N'{}'
            Declare @Donvihopban as nvarchar(500) =N'{}'
            
            Declare @Ghichu as nvarchar(max) =N'{}'
            Declare @Chondvkhac as nvarchar(max) =N'{}'
            Declare @Donvikhac as nvarchar(max) =N'{}'
            Declare @Action as nvarchar(20) ='{}'
            
            Declare @Dongsauhop as nvarchar(20) ='{}'
            Declare @Traloivanban as nvarchar(20) ='{}'
            Declare @file_vbtraloi as nvarchar(200) ='{}'
            Declare @Thoigianxuly as datetime = CONVERT(VARCHAR(19),'{}', 120)
            Declare @Ykienkhac as nvarchar(500) ='{}'
            Declare @Comment as nvarchar(max) =N'{}'
            
            Declare @Status as nvarchar(20) ='Waiting'
            if @Action='Canceled' begin set @Status=@Action end
            
            --Lấy thông tin mã thẻ tổng giám đốc
            SELECT TOP 1 @TongGiamDoc=[TongGiamDoc]  FROM [Zongjingli]
            
        """.format(data['Sodon'],user,Donvichusu,Donvihopban,
                   data['Ghichu'],data['Chondvkhac'],data['Donvikhac'],data['Action'],
                   data['Dongsauhop'],data['Traloivanban'],data['file_vbtraloi'],
                   data['Thoigianxuly'],data['Ykienkhac'],data['Comment'])
   
    #Chèn người ký tiếp the0
    query_Next=query+"""--Lấy thông tin người ký tiếp theo
                --Nếu còn thì cho ký tiếp , nếu hết thì thì hoàn thành đơn
                Declare @NextUser as nvarchar(10) =''
                select TOP 1 @NextUser=[UserName] FROM [ApprovalSection_Arr] Where [CodeDocument]=@CodeDocument and  IsCheck='N' Order by Orders            
                if @NextUser<>'' Begin UPDATE [RegisterDocumentArrive] SET [Status]=@Status,[Next_appro]= @NextUser Where Sodon=@CodeDocument End
                if @NextUser=''  Begin UPDATE [RegisterDocumentArrive] SET [Status]='Completed',[Next_appro]= @NextUser Where Sodon=@CodeDocument End"""
                
                
    #Nếu người đang chờ ký là tổng giảm đốc
    if TGD_Check:    
        query_TGM=query+"""
                --Thực hiện cập nhật đơn với thông tin đơn vị phụ trách công văn và đơn vị hỗ trợ
                UPDATE [RegisterDocumentArrive] SET [Ghichu]=@Ghichu,[Donvichusu]=@Donvichusu,
                    [Donvihopban]=@Donvihopban,[Chondvkhac]=@Chondvkhac,[Donvikhac]=@Donvikhac  
                Where Sodon=@CodeDocument 
                
                --Chèn lưu trình ký cho đơn vị chủ sự phụ trách
                if  @Donvichusu<>''
                    Begin
                        Declare @Department1 as nvarchar(10)='' --Phòng ban trong đơn vị chủ sự
                        Declare @UserName1 as nvarchar(10)='' --Người đảm nhiệm chính của phòng ban
                        DELETE [ApprovalSection_Arr] WHERE [CodeDocument]=@CodeDocument and [Orders]='3'
                        WHILE (@Donvichusu like '%,%')
                            BEGIN
                                Set @Department1=SUBSTRING(@Donvichusu,0,CHARINDEX(',',@Donvichusu, 0))
                                Set @Donvichusu=SUBSTRING(@Donvichusu,CHARINDEX(',',@Donvichusu, 0)+1,len(@Donvichusu))
                                Set @UserName1=''
                                Select TOP 1  @UserName1=[UserName] FROM [Dept_Arrive] WHERE [Department]=@Department1
                                if @UserName1<>''
                                    Begin
                                        INSERT INTO [ApprovalSection_Arr]
                                            ([ID],[CodeDocument],[UserName],[Station],[IsCheck],[Comment],[CreatedBy],[CreatedDate],[Orders])
                                            VALUES(NEWID(),@CodeDocument,@UserName,N'實施組','N','',@UserName1,GETDATE(),'3') 
                                    End
                            END
                        
                        Set @Department1=@Donvichusu
                        Set @UserName1=''
                        Select TOP 1  @UserName1=[UserName] FROM [Dept_Arrive] WHERE [Department]=@Department1
                        if @UserName1<>'' 
                            Begin 
                                INSERT INTO [ApprovalSection_Arr]
                                    ([ID],[CodeDocument],[UserName],[Station],[IsCheck],[Comment],[CreatedBy],[CreatedDate],[Orders])
                                    VALUES(NEWID(),@CodeDocument,@UserName1,N'實施組','N','',@UserName,GETDATE(),'3') 
                            End
                    End
                
                --Cập nhật chữ ký
                UPDATE [ApprovalSection_Arr] SET [IsCheck]='Y',[Time]=GETDATE(),[Status]=@Action,[Comment]=@Comment
                WHERE [UserName]=@UserName and [IsCheck]='N' and [CodeDocument]=@CodeDocument   
        """
        sql=QuerySQL_SOP(query_TGM)
        #Chèn chữ ký người tiếp theo    
        sql=QuerySQL_SOP(query_Next)

        return True
    
    else:#Nếu không phải giám đốc
        query_Appro=query+"""
                --Kiểm tra tổng giám đốc ký chưa
                DECLARE @checkTGDky as nvarchar(15)=''
                SELECT @checkTGDky=UserName FROM ApprovalSection_Arr
                    WHERE (UserName=@TongGiamDoc or UserName=@TongGiamDoc) and CodeDocument=@CodeDocument and IsCheck='Y'
                
                --Nếu chủ quản phê duyệt chưa phê duyệt
                if @checkTGDky=''
                    Begin
                        --Thực hiện cập nhật đơn với thông tin đơn vị phụ trách công văn và đơn vị hỗ trợ
                        UPDATE [RegisterDocumentArrive] SET [Ghichu]=@Ghichu,[Donvichusu]=@Donvichusu,
                                [Donvihopban]=@Donvihopban,[Chondvkhac]=@Chondvkhac,[Donvikhac]=@Donvikhac
                        Where Sodon=@CodeDocument
                    End
                
                --Nếu người phê duyệt phê rồi
                else
                    Begin
                        --Nếu người ký không phải tổng giám đốc thực hiện chèn thông tin đơn vị phụ trách trả lời
                        UPDATE [RegisterDocumentArrive] SET [Dongsauhop]=@Dongsauhop,[Traloivanban]=@Traloivanban,
                        [file_vbtraloi]=@file_vbtraloi,[Thoigianxuly]=@Thoigianxuly,[Ykienkhac]=@Ykienkhac
                        Where Sodon=@CodeDocument
                    End
                
                --Cập nhật chữ ký
                UPDATE [ApprovalSection_Arr] SET [IsCheck]='Y',[Time]=GETDATE(),[Status]=@Action,
                    [Comment]=@Comment  WHERE [UserName]=@UserName and [IsCheck]='N' and [CodeDocument]=@CodeDocument
        """
        sql=QuerySQL_SOP(query_Appro)
        
        #Chèn chữ ký người tiếp theo
        sql=QuerySQL_SOP(query_Next)
    
    return True




#Lưu log gửi mail
def Save_Log_SendMail(Sodon,ToEmail,ToCC,Status,Contents,CreatedBy,Title):    
    query="""INSERT INTO HistorySendMail
                ([ID],[Code],[ToEmail],[BCC],[Status],
                    [Contents],[CreatedBy],[CreatedDate],[Title])
            VALUES(NEWID(),'{}','{}',N'{}',N'{}',
                    N'{}',N'{}',GETDATE(),N'{}')
      """.format(Sodon,ToEmail,ToCC,Status,Contents,CreatedBy,Title)
    sql=QuerySQL2_SOP(query)
    return sql




#Lấy email từ 1 tài khoản
def Get_Email_From_Employe(Empno):
    query="SELECT Email From Users Where TenDangNhap='{}' ".format(Empno)
    return SelectSQL3_SOP(query)



#Lấy thông tin người chờ ký
def Check_Next_Approver(request):
    data=request.GET
    user=request.user.get_username()
    query="SELECT [Next_appro] FROM [RegisterDocumentArrive] WHERE [Sodon]='{}' and [Status]='Waiting' and [Next_appro]='{}' ".format(data['Sodon'],user)
    return SelectSQL3_SOP(query)


#Lấy Thông tin người chờ ký tiếp theo
def Get_NextApprover(Sodon):
    query="""SELECT r.[Next_appro],u.Email FROM [RegisterDocumentArrive] as r
             LEFT JOIN Users as u on r.[Next_appro]=u.TenDangNhap
            WHERE [Sodon]='{}' and [Status]='Waiting' """.format(Sodon)
    sql=SelectSQL3_SOP(query)
    return sql


#Lấy thông tin người làm đơn
def Get_Application_Document(Sodon):
    query="""SELECT r.[Nguoitrinhdon],u.Email FROM [RegisterDocumentArrive] as r
             LEFT JOIN Users as u on r.[Nguoitrinhdon]=u.TenDangNhap
            WHERE [Sodon]='{}' """.format(Sodon)
    sql=SelectSQL3_SOP(query)
    return sql





