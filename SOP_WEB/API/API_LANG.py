from API.API_MSSQL import QuerySQL,SelectSQL

#Cập nhật ngôn ngữ đã chọn vào DB
def CHANGE_LANG(lang,user_ID):
    query="UPDATE [Users] SET [lang]='"+str(lang)+"' WHERE [UserID]='"+str(user_ID)+"'"
    try:
        sql=QuerySQL(query)
        return True
    except: return False
    
    
       
#Truy vấn ngôn ngữ đang sử dụng trong db
def GET_LANG(user_ID):
    query="SELECT [lang] FROM [Users] WHERE [UserID]='"+str(user_ID)+"'"
    try:
        sql=SelectSQL(query)
        if len(sql)>0 : return sql[0]
    except: return ''
    return ''
    