from API.API_MSSQL import *

def GET_INFO_WIFI(Apply_No):#Nếu trả về false là k có
    query="SELECT * FROM [Add_Wifi] WHERE Apply_No='"+str(Apply_No)+"'"
    sql= SelectSQL(query)
    if len(sql)>0:
        return sql
    return False