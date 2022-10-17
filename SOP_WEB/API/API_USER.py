
from API.API_MSSQL import *
from API.MD5_HASH import Decript_Pass, Encript_Pass



# tìm Tên USER_NAME của 1 User_ID nào đó
def GET_USERNAME(empno):
    sql= SelectSQL3("SELECT [UserName] FROM Users  WHERE [UserID]='"+str(empno)+"'") 
    if(len(sql)>0): 
        # print(sql[0]['UserName'])
        return sql[0]['UserName']
    else: return ''
  
  
  
# tìm Tên Mail của 1 User_ID nào đó
def GET_Email(empno):
    sql= SelectSQL3("SELECT [mailbox] FROM Users  WHERE [UserID]='"+str(empno)+"'") 
    if(len(sql)>0): 
        # print(sql[0]['UserName'])
        return sql[0]['mailbox']
    else: return ''
  
  
# trả về toàn bộ thông tin của user thông qua Empno
def GET_USER_Info(empno):
    sql= SelectSQL3("SELECT * FROM Users  WHERE [UserID]='"+str(empno)+"'") 
    if(len(sql)>0):       
        return sql[0]
    else: return ''
    
    
# trả về toàn bộ thông tin của user thông qua email
def GET_USER_Info_Email(email):
    sql= SelectSQL3("SELECT * FROM Users  WHERE [mailbox]='"+str(email)+"'") 
    if(len(sql)>0):       
        return sql[0]
    else: return ''
    
# trả về toàn bộ thông tin của user thông qua email và tài khoản
def GET_USER_Info_Email_User(email,username):
    sql= SelectSQL3("SELECT * FROM Users  WHERE [mailbox]='"+str(email)+"' And UserID='"+str(username)+"'") 
    if(len(sql)>0):       
        return sql[0]
    else: return ''

    
    
    
# tạo Tài khoản trên DB MSSQL Users
def Creat_Users(UserID,PassWord,Emp_NO,email):
    PassWord=Encript_Pass(PassWord)
    query='''INSERT INTO [Users]([UserID],[PassWord],[Emp_NO],[mailbox])
    VALUES ('{}','{}','{}','{}') '''.format(UserID,PassWord,Emp_NO,email)
    # print(query)
    sql=QuerySQL2(query)
    # print(sql)



# cập nhật mật khẩu Users
def Update_Passw(UserID,PassWord,email):
    PassWord=Encript_Pass(PassWord)
    strupdate="UPDATE [Users] SET [PassWord]='"+str(PassWord)+"',[mailbox]='"+str(email)+"' WHERE  [UserID]='"+str(UserID)+"'" 
    QuerySQL(strupdate)    



#lấy địa chỉ mail từ Users
def Get_Acount_Info(username,passw):
    passw=Encript_Pass(passw)
    strquery="Select * FROM Users WHere [UserID]='"+str(username)+"' AND [PassWord]='"+str(passw)+"'" 
    sql=SelectSQL3(strquery)

    if (len(sql)>0):
        return sql[0]
    else: return ''
    
    
    
# kiểm tra tài khoản trong DB MSSQL Users 
def Check_Acount(username,passw):
    passw=Encript_Pass(passw)
    strquery="Select * FROM Users WHere [UserID]='"+str(username)+"' AND [PassWord]='"+str(passw)+"'" 
    if (len(SelectSQL3(strquery))>0):
        return True
    else: return False



# kiểm tra tài khoản trong DB MSSQL Users 
def Check_UserName(username):
    strquery="Select * FROM Users WHere [UserID]='"+str(username)+"'" 
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
    strquery='''UPDATE  Users SET [DFSite]'''+"=N'"+ DFSite +"',[division]=N'"+ division+"',"+'''
    [UserName]'''+"=N'"+ UserName +"',[Emp_NO]='"+ Emp_NO+"',[Dept]=N'"+ Dept +"',"+'''
    [CostNo]'''+"='"+CostNo +"',[Telephone]='"+ Telephone +"',[mailbox]='"+ mailbox +"' WHERE [UserID]='"+str(user_ID)+"'"
    sql=QuerySQL2(strquery)
    # print(sql)
  
  
#Lấy User ID  từ ID
def Get_UserID(id):
    query="SELECT * FROM Users WHERE ID='"+str(id)+"'"
    sql=SelectSQL3(query)
    if len(sql)>0 :return sql[0]
    else : return ""
  
  
        
#Lấy icon ảnh và tên user
def GET_ICON_USER(request):
     userID= request.user.username
     query="SELECT [UserName],[img] FROM [Users] WHERE [UserID]='"+str(userID)+"'"  
     sql=SelectSQL3(query)
     if len(sql)>0:return sql[0] 
     else : return ''
   
        
        
#  trả về quyền hạn hiển thị các module
def PERMISSION_USER(user_ID):
    query="SELECT * FROM [EPERMISSION_USER] WHERE [USER_ID]='"+str(user_ID)+"'"    
    sql=SelectSQL3(query)
    if len(sql)>0: return sql[0]
    else: ''
    

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
                END as PERMMISSION FROM [ESIGN4.0].[dbo].[EPERMISSION_USER] WHERE USER_ID='''+"'"+str(user)+"'"
    sql=SelectSQL3(query)
    if len(sql)>0: return sql[0]['PERMMISSION']
    else: return ''
    
    
