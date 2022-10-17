from API.API_MSSQL import *
from API.API_sendMail import SEND_MAIL
from API.API_MYSQL import *

#  trả về Signer_Type,Signer_Name,Sign_Type của userID
def Get_Signer_Info(userid):
    strquery="SELECT * FROM [File_Signer_Info] WHERE Signer_No='"+str(userid)+"'"
    if len(SelectSQL3(strquery))>0:return SelectSQL3(strquery)[0]
    else: return ''



# Sắp xếp lại số thứ tự ký của trường Order_No
def SapXep_Order_No(docno):
    strSX='''
        SET NOCOUNT ON;  
        DECLARE vend_cursor CURSOR FOR 
            SELECT ID FROM [File_Signer_Work_S]  WHERE Apply_No'''+"='"+str(docno)+"'"+''' Order by Order_No
        OPEN vend_cursor  

        DECLARE @I INT;
        DECLARE @ID INTEGER;
        Set @I = 0
        
        Fetch Next From vend_cursor  INTO @ID
        While @@Fetch_Status = 0
        Begin
            Update [File_Signer_Work_S] set Order_No = @I Where ID=@ID
            Set @I = @I + 1
            Fetch Next From vend_cursor  INTO @ID
        End

        CLOSE vend_cursor;  
        DEALLOCATE vend_cursor; 
    '''
    if QuerySQL2(strSX) : return True
    else: return False
   
   
     
# trả về chữ ký cho bảng:
def List_SignInfo(docno):
       #Lấy thông tin các chữ ký trả về phía client
    strq='''
                 SELECT  s.[Order_No],s.[Is_Check],s.Sign_Type,s.[Signer],s.[Status],u.[UserName],s.[Sign_Agent],s.[Sign_Detail],s.[Sign_IP],s.[Sign_Time],s.[Sign_FileNameOld]
                    FROM 
                    ( 
                    SELECT  *
                    FROM  [File_Signer_Work_S] as a
                    WHERE a.Apply_No''' +"='"+str(docno)+"'"+'''
                    ) as s
                    LEFT JOIN [Users] as u
                    ON s.Signer= u.UserID order by Order_No
       '''
    sql=SelectSQL3(strq)# Lấy danh sách các chữ ký
    return sql



# trả về userID đang chờ ký trong bảng S
def Get_waiting_ID(docno):
    strq="SELECT TOP 1 Signer,Order_No,Sign_Type,Signer_Type FROM [File_Signer_Work_S] WHERE Is_Check='N'  AND Apply_No='"+str(docno)+"'  Order by Order_No"
    if len(SelectSQL3(strq))>0: 
        # print(strq)
        return SelectSQL3(strq)[0]
    else: return ''



# trả về mã của người đang chờ được phê duyệt ['Next_Approver'] bảng H
def GET_NEXT_APPROVER(docno):
    strsearch="SELECT Next_Approver FROM [File_Signer_Apply_H] where Apply_No='"+str(docno)+"'"
    sql=SelectSQL3(strsearch)
    if len(sql)>0: return sql[0]
    else: return ''



# trả về trạng thái của đơn trong bảng H
def GET_Status_DOC(docno):
    strsearch="SELECT [Process] FROM [File_Signer_Apply_H] where Apply_No='"+str(docno)+"'"
    if len(SelectSQL3(strsearch))>0: return SelectSQL3(strsearch)[0]['Process']
    else: return ''



# trả về userID người tạo đơn trong bảng S
def Get_Applicant(docno):
    strq="SELECT TOP 1 Signer,Order_No,Sign_Type FROM [File_Signer_Work_S] WHERE Order_No='0' AND Apply_No='"+str(docno)+"' Order by Order_No"
    if len(SelectSQL3(strq))>0 : return SelectSQL3(strq)[0]
    else: return ''



# chèn thêm người ký vào bảng ký S
def INSERT_SIGN(docno,OrderNo,Signer_Type,Sign_Type,Emp_no,Sign_Agent):
        
        strchen= '''
              INSERT INTO [File_Signer_Work_S] ([Apply_No],[Order_No],[Signer_Type],[Sign_Type],[Is_Check],[Signer],[Status],[Sign_Detail],[Sign_FileNameOld],[Sign_Agent])
              VALUES('''+"'"+str(docno)+"','"+str(float(OrderNo)+0.1)+"',N'"+str(Signer_Type)+"','"+str(Sign_Type)+"','N','"+str(Emp_no)+"','','','','"+str(Sign_Agent)+"')"
        if QuerySQL2(strchen): return True
        else: return False



# cập nhật trạng thái đơn bảng H
def SET_STATTUS_DOC(docno,Sign_Type,Next_Approver,Next_Name,Process):
    str_updateH=" UPDATE [File_Signer_Apply_H] SET [Next_Approver] ='"+str(Next_Approver)+"',"+"[Process]='"+str(Process)+"',[Sign_Type] ='"+str(Sign_Type)+"',"+"[Next_Name]='"+str(Next_Name)+"' WHERE [Apply_No]='"+str(docno)+"'"
    if QuerySQL2(str_updateH): return True
    else: return False
   
   
# Hủy  đơn bảng H
def SET_CANCEL_DOC(docno,Process):
    str_updateH=" UPDATE [File_Signer_Apply_H] SET [Process]='"+str(Process)+"'"+'''
            '''+ " WHERE [Apply_No]='"+str(docno)+"'"
    if QuerySQL2(str_updateH): return True
    else: return False



# xác nhận ký
def Approval_(docno,Process,Sign_Detail,IP,userID,Sign_FileNameOld):
    # print(Sign_Detail)
    strquery='''
        UPDATE tb SET tb.[Is_Check]='Y',tb.[Status]'''+"='"+Process+"',tb.[Sign_Detail]=N'"+str(Sign_Detail)+"',tb.[Sign_IP]='"+str(IP)+"',"+'''tb.[Sign_Time]=SYSDATETIME(),
        tb.[Sign_FileNameOld]'''+"=N'"+str(Sign_FileNameOld)+"'"+ '''
        FROM (SELECT TOP 1 * FROM [File_Signer_Work_S]  WHERE Apply_No'''+"='"+str(docno)+"' AND [Is_Check]='N' and ([Signer]='"+str(userID)+"' OR [Sign_Agent]='"+str(userID)+"') Order By Order_No asc) as tb"
    # print(strquery)
    QuerySQL(strquery)# thực hiện chèn ký vào bảng S



# lấy thông tin đầu đơn trong bảng H
def GET_DOCNO_INFO(docno):
    strqueryDoc="SELECT * FROM [File_Signer_Apply_H] WHERE [Apply_No]"+"='"+str(docno)+"'"
    sql1=SelectSQL3(strqueryDoc)# Lấy thông tin ID đầu đơn
    if len(sql1)>0 : return sql1[0]       
    return ''

#Lấy thông tin đơn trong bảng H và costno trong bảng User
def GET_DOCNO_INFOR(docno):
    query='''
        SELECT h.*,u.CostNo,u.Telephone
        FROM [ESIGN4.0].[dbo].[File_Signer_Apply_H]  as h
            INNER JOIN [ESIGN4.0].[dbo].[Users] as u
            ON h.Apply_EmpNo= u.UserID
        where h.Apply_No'''+"='"+str(docno)+"'"
    sql=SelectSQL3(query)
    if len(sql)>0 : return sql[0]       
    return ''

#Lấy tên của Flow title trong bảng Flow Detail
def GET_FLOWNAME_DETAIL(docno):
    strqueryDoc="SELECT * FROM [File_Signer_Apply_H] WHERE [Apply_No]"+"='"+str(docno)+"'"
    sql1=SelectSQL3(strqueryDoc)# Lấy thông tin ID đầu đơn
    if len(sql1)>0 : 
        flowID=sql1[0]['Flow_Name_Detail']
        str_docname="SELECT [Flow_Name] FROM [File_Signer_Flow] WHERE ID"+"='"+str(flowID)+"'"
        flowdetail=SelectSQL3(str_docname)
        if len(flowdetail)>0: return str(flowID)+": "+flowdetail[0]['Flow_Name']
    return ''



#Lấy danh sách tên các file Attachment 
def GET_LIST_ATTACHMENT(docno):
    sql=SelectSQL3("SELECT * FROM [File_Signer_Apply_F] WHERE Apply_No"+"='"+str(docno)+"'")
    if len(sql)>0: return sql
    else: return ''
   
   
    
#Chèn File Attach vào bảng File F
def INSERT_ATTACH(docno,File_Name):
    str_is1="INSERT INTO File_Signer_Apply_F([Apply_No],[File_Name]) VALUES('"+str(docno)+"',N'"+str(File_Name)+"')"
    if QuerySQL2(str_is1): return True
    else: return False
    

def CREATE_DOC_H(docno,Order_No,Flow_Name_Detail,Project_Name,Description,Apply_File,Site,bu,Level_Grade,Apply_Person,Apply_EmpNo,Apply_Tel,Apply_Notus,Process,Next_Approver,Next_Name,Remark,MailCC,MailCC_End):
    Project_Name=Project_Name.replace("'"," ")
    Remark=Remark.replace("'"," ")
    Description=Description.replace("'"," ")
    try:
        if(len(SelectSQL3("SELECT * FROM [File_Signer_Apply_H] WHERE Apply_No='{}'".format(docno)))>0):
                    QuerySQL2("DELETE [File_Signer_Apply_H] WHERE Apply_No='{}'".format(docno))
        
    except :pass   
    try:
        strquery2='''
                INSERT INTO File_Signer_Apply_H (
                    Apply_No, Order_No, Flow_Name_Detail,Project_Name,Description,Apply_File,Site,bu,Level_Grade,Apply_Person,
                    Apply_EmpNo,Apply_Tel,Apply_Notus,Edit_Time,Process,Next_Approver,Next_Name,IS_GK,Remark,MailCC,MailCC_End)
                VALUES ('''+ "'"+ str(docno) +"','"+ str(Order_No) +"',N'"+ str(Flow_Name_Detail) +"',N'"+ str(Project_Name)  +"',N'"+ str(Description) +"',N'"+ str(Apply_File)+"',N'"+ str(Site)+"',N'"+ str(bu)+"','"+str(Level_Grade) +"',N'"+str(Apply_Person )+"',"+ "'"+str(Apply_EmpNo)+"','"+ str(Apply_Tel)+"',N'"+str(Apply_Notus)+"', SYSDATETIME(),'"+str(Process)+"',N'"+str(Next_Approver)+"',N'"+str(Next_Name)+"','N',N'"+str(Remark) +"',N'"+str(MailCC) +"',N'"+ str(MailCC_End)+"')"# Câu lệnh chèn  thông tin đơn vào bảng [File_Signer_Apply_H]    
        # print(strquery2)
        print(strquery2)
        if QuerySQL2(strquery2): 
            return True
        else: 
            return False
    except Exception as ex: return "Lỗi:"+str(ex)


#Chạy lệnh đối sánh SQL để đồng bộ dữ liệu các bảng.Lấy tên người ký và kiểu nhóm ký (Sign_Type và [Signer_Name)
def UPDATE_SIGNTYPE_SIGNERNAME(docno):
    strupdate_signtype='''
        UPDATE  h
            SET	
                h.[Sign_Type] =o.[Sign_Type_E],	
                h.[Next_Name] =o.[Signer_Name]
            FROM	
                [File_Signer_Apply_H] as h
            INNER JOIN	
                [File_Signer_Info] as o	
            ON 	
            h.[Next_Approver]=o.[Signer_No]	
            Where	h.[Apply_No]='''+ "'"+str(docno)+"'"
    QuerySQL(strupdate_signtype)
    


#Cập nhật thông tin đơn khi bị sai
def UPDATE_DOCNO(Apply_No,Flow_Name_Detail,Apply_File,Level_Grade,Remark,MailCC,MailCC_End):
    strquery='''UPDATE  [File_Signer_Apply_H] SET [Apply_File]''' +" =N'"+str(Apply_File)+"'," + "[Level_Grade]='"+str(Level_Grade)+"',"+  '''
        [Flow_Name_Detail]''' +" ='"+str(Flow_Name_Detail)+"',[Remark]=N'"+str(Remark)+"',[MailCC]=N'"+str(MailCC)+"',[MailCC_End]=N'"+str(MailCC_End)+"' WHERE [Apply_No]='"+str(Apply_No)+"'"
        
    if len(Apply_File)==0 :
            strquery='''UPDATE  [File_Signer_Apply_H] SET [Level_Grade]'''+" ='"+str(Level_Grade)+"',"+  '''
        [Flow_Name_Detail]''' +" ='"+str(Flow_Name_Detail)+"',[Remark]=N'"+str(Remark)+"',[MailCC]=N'"+str(MailCC)+"',[MailCC_End]=N'"+str(MailCC_End)+"' WHERE [Apply_No]='"+str(Apply_No)+"'"
    
    ex=QuerySQL2(strquery)
    if ex: return True
    else : return False
    
    
    
#Lấy thông tin TOP 4 đơn mới được tạo gần đây nhất
def GET_TOP_DOC(number):
    query='''
        SELECT *
        FROM  (SELECT TOP '''+str(number)+''' * FROM [File_Signer_Apply_H]  order by ID desc) as a
        INNER JOIN 
        (SELECT img,UserID FROM Users ) as b
        ON a.Apply_EmpNo=b.UserID
        Order by a.ID desc
    '''
   
    sql=SelectSQL3(query)
    # print (sql)
    if len(sql)>0 :return sql
    else:''
   
    

#Lấy tổng user, doc,file,attach
def GET_TOTAL_(userID):
    strquery='''SELECT
        (SELECT COUNT(*)
        FROM    [File_Signer_Apply_H]
        ) AS total_doc,
        (SELECT COUNT(*)
        FROM   [Users]
        ) AS total_acount,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_F]
        ) AS total_fileattach,
        (
        SELECT COUNT(*)
        FROM    [File_Signer_Apply_H] where Process='Closed'
        ) AS total_finish,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where Process='Waiting'
        ) AS total_waiting,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where Process='Waiting' and Next_Approver''' +"='"+str(userID)+"'"+'''
        ) AS my_waiting,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where Process='Cancel'
        ) AS total_cancel,
        (SELECT COUNT(*)
        FROM    [File_Signer_Apply_H] where [Apply_EmpNo]''' +"='"+str(userID)+"'"+'''
        ) AS total_application,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where  [Apply_EmpNo]'''+"='"+str(userID)+"'"+'''  AND [Process]='Closed' 
        ) AS total_ApplicationClosed,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where  [Apply_EmpNo]'''+"='"+str(userID)+"'"+'''  AND [Process]='Reject'
        ) AS total_return,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where  [Apply_EmpNo]'''+"='"+str(userID)+"'"+''' AND [Process]='Waiting'
        ) AS total_pending,
        (SELECT COUNT(*)
        FROM   [File_Signer_Apply_H] where  [Apply_EmpNo]'''+"='"+str(userID)+"'"+''' AND [Process]='Cancel'
        ) AS total_cancel,
        (SELECT COUNT(*)
        FROM    [File_Signer_Work_S] where [Signer]'''+"='"+str(userID)+"'"+'''
        ) AS total_signature, 
        (SELECT COUNT(*)
        FROM    [File_Signer_Work_S] where [Is_Check]='Y'
        ) AS total_signature_system
    '''     
    try:       
        sql=SelectSQL3(strquery)
        if len(sql)>0:    return (sql[0])
        else: return''
    except: return ''



#Lấy thông tin đơn đang chờ ký
def GET_WAITING_APPROVAL_DOC(user_ID):
    query='''
            SELECT *
            FROM  (SELECT * FROM [File_Signer_Apply_H] WHERE ([Process]='Waiting' OR [Process]='Reject') AND Next_Approver'''+" ='"+str(user_ID)+"') "+'''as a
            INNER JOIN 
            (SELECT [img],[UserID] FROM Users) as b
            ON a.Apply_EmpNo=b.UserID
            Order by a.ID desc
        '''
    sql= SelectSQL3(query)
    if len(sql)>0: return sql
    else: return ''
            
    
    
#Kiểm tra và lấy thông tin người tai nỉ
def GET_TAINI_SIGN(userid):
    mysql=GET_TAINI(userid)
    
    if mysql is None: return False
    if mysql['NOTDUTY']=='Yes' and len(str(mysql['AGENT_WHO']))>0:
            # print(mysql['AGENT_WHO'])
            return mysql
    else: return False
    

#Kiểm tra lịch sử người



#Cập nhật AGENT Bảng S
def UPDATE_S_AGENT(docno,userid,agent):
    query="UPDATE [File_Signer_Work_S] SET [Sign_Agent]='"+str(agent)+"' WHERE [Apply_No]='"+str(docno)+"' AND [Signer]='"+str(userid)+"'"
    sql=QuerySQL2(query)
    return sql