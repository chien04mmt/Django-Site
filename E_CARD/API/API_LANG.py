from API.API_MSSQL import *

#Cập nhật ngôn ngữ đã chọn vào DB
def CHANGE_LANG(lang,user_ID):
    query="UPDATE "+table_Users+" SET [lang]='"+str(lang)+"' WHERE [UserID]='"+str(user_ID)+"'"
    try:
        sql=QuerySQL(query)
        return True
    except: return False
    
    
       
#Truy vấn ngôn ngữ đang sử dụng trong db
def GET_LANG(user_ID):
    query="SELECT [lang] FROM "+table_Users+" WHERE [UserID]='"+str(user_ID)+"'"  
    sql=SelectSQL(query)
    return sql[0]['lang']
    
    