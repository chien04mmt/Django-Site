from API.API_MSSQL import *
from API.MD5_HASH import Decript_Pass, Encript_Pass



# tìm Tên USER_NAME của 1 User_ID nào đó
def GET_USERNAME(empno):
    sql= SelectSQL3("SELECT [UserName] FROM  "+table_Users+"  WHERE [UserID]='"+str(empno)+"'") 
    if(len(sql)>0): 
        # print(sql[0]['UserName'])
        return sql[0]['UserName']
    else: return ''
  
  
  
# tìm Tên Mail của 1 User_ID nào đó
def GET_Email(empno):
    sql= SelectSQL3("SELECT [mailbox] FROM  "+table_Users+"  WHERE [UserID]='"+str(empno)+"'") 
    if(len(sql)>0): 
        # print(sql[0]['UserName'])
        return sql[0]['mailbox']
    else: return ''
  
  
# trả về toàn bộ thông tin của user thông qua Empno
def GET_USER_Info(empno):
    sql= SelectSQL3("SELECT * FROM  "+table_Users+"  WHERE [UserID]='"+str(empno)+"'")      
    return sql
    
    
# trả về toàn bộ thông tin của user thông qua email
def GET_USER_Info_Email(email):
    sql= SelectSQL3("SELECT * FROM  "+table_Users+"  WHERE [mailbox]='"+str(email)+"'") 
    if(len(sql)>0):       
        return sql[0]
    else: return ''
    
    
    
# tạo Tài khoản trên DB MSSQL Users
def Creat_Users(UserID,PassWord,Emp_NO,email):
    PassWord=Encript_Pass(PassWord)
    strcreate="INSERT INTO "+table_Users+"([UserID],[PassWord],[Emp_NO],[mailbox]) VALUES ('"+str(UserID)+"','"+str(PassWord)+"','"+str(Emp_NO)+"','"+str(email)+"')"
    QuerySQL(strcreate)
      
      
      

# tạo Tài khoản trên DB MSSQL Users
def Creat_Users1(UserID,DFSite,division,UserName,Emp_NO,Dept,CostNo,Telephone,mailbox,PassWord):
    PassWord=Encript_Pass(PassWord)
    query='''  INSERT INTO Users
                (UserID,DFSite,division,UserName,Emp_NO,Dept,CostNo,Telephone,mailbox,PassWord)
                VALUES(N'{}',N'{}',N'{}',N'{}','{}',N'{}','{}','{}','{}','{}')
            '''.format(UserID,DFSite,division,UserName,Emp_NO,Dept,CostNo,Telephone,mailbox,PassWord)
    sql=QuerySQL2(query)
    return sql

      
        
# cập nhật mật khẩu Users
def Update_Passw(UserID,PassWord,email):
    PassWord=Encript_Pass(PassWord)
    strupdate="UPDATE "+table_Users+" SET [PassWord]='"+str(PassWord)+"',[mailbox]='"+str(email)+"' WHERE  [UserID]='"+str(UserID)+"'" 
    QuerySQL(strupdate)    



#lấy địa chỉ mail từ Users
def Get_Acount_Info(username,passw):
    passw=Encript_Pass(passw)
    strquery="Select * FROM  "+table_Users+" WHere [UserID]='"+str(username)+"' AND [PassWord]='"+str(passw)+"'" 
    sql=SelectSQL3(strquery)

    if (len(sql)>0):
        return sql[0]
    else: return ''





# kiểm tra tài khoản trong DB MSSQL Users 
def Check_Acount(username,passw):
    passw=Encript_Pass(passw)
    strquery="Select * FROM  "+table_Users+" WHere [UserID]='"+str(username)+"' AND [PassWord]='"+str(passw)+"'" 
    if (len(SelectSQL3(strquery))>0):
        return True
    else: return False




# kiểm tra tài khoản trong DB MSSQL Users 
def Check_UserName(username):
    strquery="Select * FROM  "+table_Users+" WHere [UserID]='"+str(username)+"'" 
    if (len(SelectSQL3(strquery))>0):
        return True
    else: return False




#THêm tài khoản USSER
def Add_new_User(DFSite,UserID,UserName,PassWord,Dept,Emp_NO,Telephone,mailbox,division,CostNo):
    PassWord=Encript_Pass(PassWord)
    strinsert=''' INSERT INTO Users(
                        [DFSite]
                        ,[UserID]
                        ,[UserName]
                        ,[PassWord]
                        ,[Dept]
                        ,[Emp_NO]
                        ,[Telephone]
                        ,[mailbox]
                        ,[division]
                        ,[CostNo])
    VALUES('''+"'"+str(DFSite)+"','"+str(UserID)+"','"+str(UserName)+"','"+str(PassWord)+"','"+str(Dept)+"','"+str(Emp_NO)+"','"+str(Telephone)+"','"+str(mailbox)+"','"+str(division)+"','"+str(CostNo)+"')"
    QuerySQL(strinsert)




# cập nhật thông tin User Manager
def Update_User_Manager(DFSite,division,UserName,Emp_NO,Dept,CostNo,Telephone,mailbox,user_ID):
    strquery='''UPDATE '''+table_Users+''' SET [DFSite]'''+"=N'"+ DFSite +"',[division]=N'"+ division+"',"+'''
    [UserName]'''+"=N'"+ UserName +"',[Emp_NO]='"+ Emp_NO+"',[Dept]=N'"+ Dept +"',"+'''
    [CostNo]'''+"='"+CostNo +"',[Telephone]='"+ Telephone +"',[mailbox]='"+ mailbox +"' WHERE [UserID]='"+str(user_ID)+"'"
    
    QuerySQL(strquery)




#Lấy User ID  từ ID
def Get_UserID(id):
    query="SELECT * FROM  "+table_Users+" WHERE ID='"+str(id)+"'"
    sql=SelectSQL3(query)
    if len(sql)>0 :return sql[0]
    else : return ""





#Lấy icon ảnh và tên user
def GET_ICON_USER(request):
     userID= request.user.username
     query="SELECT [UserName],[img] FROM "+table_Users+" WHERE [UserID]='"+str(userID)+"'"  
     sql=SelectSQL3(query)
     if len(sql)>0:return sql[0] 
     else : return ''




#  trả về quyền hạn hiển thị các module
def PERMISSION_USER(user):   
    query="""Declare @Code_Permission as nvarchar(100)=''
             SELECT @Code_Permission=Code_Permission FROM {} WHERE UserID='{}'
             
             SELECT m.*,mn.Groups_Menu FROM Modules as m 
             LEFT join Menus as mn on m.Code_Menu=mn.Code_Menu
             WHERE [Code_Permission]=@Code_Permission
             """.format(table_Users,user)              
    sql=SelectSQL3(query)
    return sql




#Thiết lập quyền hạn cho người dùng
def SAVE_PERMISSION_USER(userID,Code_Permission):
    query="UPDATE "+table_Users+" SET Code_Permission='{}' WHERE UserID='{}' ".format(Code_Permission,userID.replace(" ",""))
    sql=QuerySQL(query)
    return True
    
    
#Lấy thông tin quyền của người dùng
def GET_PERMISSION_USER(userID):
    query="""SELECT u.UserID,u.UserName,u.Code_Permission,lp.Name_Permission  
                FROM {} as u 
                LEFT JOIN [ListPermission] as lp on u.Code_Permission=lp.Code_Permission 
                WHERE UserID='{}' 
    """.format(table_Users,userID.replace(" ",""))
    sql=SelectSQL3(query)
    return sql
    
    

#THiết lập quyền cho user mới
def SET_PERMISSION_USER(user):
    insert='''INSERT INTO [EPERMISSION_USER] ([USER_ID]
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
                ,[EXPIRATION_DATE])
      '''+" VALUES('"+ str(user)+"','USER','1','1','0','1','0','0','0','0','1','E-Sign',SYSDATETIME(),DATEADD(year,1, SYSDATETIME()))"
    sql=QuerySQL2(insert) 
    return sql




#Kiểm tra hiệu lực tài khoản
def CHECK_PERMISSION(user):
    query='''  SELECT CASE
                    WHEN EXPIRATION_DATE>= SYSDATETIME()
                    THEN 1
                    ELSE 0
                END as PERMMISSION FROM [EPERMISSION_USER] WHERE USER_ID='''+"'"+str(user)+"'"
    sql=SelectSQL3(query)
    if len(sql)>0: return sql[0]['PERMMISSION']
    else: return ''
    
    
    
#Chèn log gửi mail
def INSERT_LOG_SENDMAIL(DocNo,CreatedBy,MailTo,Mailcc,Status,Subject):
    insert="""INSERT INTO LOG_SENDMAIL([DocNo],[CreatedBy],[MailTo],[Mailcc],[Status],[Subject],[CreatedDate])
              VALUES('{}','{}','{}','{}','{}',N'{}',GETDATE())
          """.format(DocNo,CreatedBy,MailTo,Mailcc,Status,Subject)
    sql=QuerySQL2(insert)
    return sql
    
    
    
    
    
    
    
    
    
