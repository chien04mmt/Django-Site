from API.API_MSSQL import *

#THêm mới biểu mẫu
def ADD_FLOW(Site,Bu,Flow_Name,Manager_HQ,Manager_HQ_Num,List_authen,MailCC_for_end,Multi_Signer,Show_Pdf,Submit_Person):
    insert='''INSERT INTO [File_Signer_Flow]
        ([Site]
        ,[Bu]
        ,[Flow_Name]
        ,[Manager_HQ]
        ,[Manager_HQ_Num]
        ,[List_authen]
        ,[MailCC_for_end]
        ,[Multi_Signer]
        ,[Show_Pdf]
        ,[Submit_Person]
        ,[Submit_Time]
        )
        VALUES(''' +"'"+str(Site)+"','"+str(Bu)+"','"+str(Flow_Name)+"','"+str(Manager_HQ)+"','"+str(Manager_HQ_Num)+"','"+str(List_authen)+"','"+str(MailCC_for_end)+"','"+str(Multi_Signer)+"','"+str(Show_Pdf)+"','"+str(Submit_Person)+"',SYSDATETIME())" 
    sql=QuerySQL2(insert)
    return sql



#Sửa thông tin mẫu đơn
def UPDATE_FLOW(ID,Site,Bu,Flow_Name,List_authen,MailCC_for_end,Multi_Signer,Show_Pdf,SignOff):
    update='''UPDATE [File_Signer_Flow] SET
        [Site]'''+"='"+str(Site)+"',"+'''
        [Bu]'''+"='"+str(Bu)+"',"+'''
        [Flow_Name]'''+"='"+str(Flow_Name)+"',"+'''
    
        [List_authen]'''+"='"+str(List_authen)+"',"+'''
        [MailCC_for_end]'''+"='"+str(MailCC_for_end)+"',"+'''
        [Multi_Signer]'''+"='"+str(Multi_Signer)+"',"+'''
        [SignOff]'''+"='"+str(SignOff)+"',"+'''
        [Show_Pdf]'''+"='"+str(Show_Pdf)+"' WHERE ID='"+str(ID)+"'"

    sql=QuerySQL2(update)
    return sql



#Sửa thông tin mẫu đơn
def UPDATE_TITLE(ID,Site,Bu,Flow_Name,Manager_HQ,Manager_HQ_Num):
    update='''UPDATE [File_Signer_Flow] SET
        [Site]'''+"='"+str(Site)+"',"+'''
        [Bu]'''+"='"+str(Bu)+"',"+'''
        [Flow_Name]'''+"='"+str(Flow_Name)+"',"+'''
        [Manager_HQ]'''+"='"+str(Manager_HQ)+"',"+'''
        [Manager_HQ_Num]'''+"='"+str(Manager_HQ_Num)+"' WHERE ID='"+str(ID)+"'"
    sql=QuerySQL2(update)
    return sql
    
    
    
#Xóa thông tin mẫu đơn
def DEL_TITLE(ID):
    delete="DELETE [File_Signer_Flow]  WHERE ID='"+str(ID)+"'"
    sql=QuerySQL2(delete)
    return sql



#Phương thức lấy danh sách các FLOW TITLE dùng hàm LIKE SQL
def SearchOject_(tb_name,field_search,key_value):
        strquery="SELECT  * FROM  "+tb_name+" WHERE "+field_search+" LIKE N'%"+ key_value +"%'"           
        sql= SelectSQL(strquery)
        if len(sql)>0:
            return sql
        else:
            return ''





