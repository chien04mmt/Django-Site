
from API.API_MSSQL import *
import hashlib



# kiểm tra tài khoản trong DB MSSQL Users 
def Check_Acount(username,passw): 
    passw = hashlib.md5(passw.encode()).hexdigest().upper()
    # query="exec sp_CheckLogin '{}','{}','' ".format(username,passw)
    query="""SELECT * FROM Users WHERE TenDangNhap='{}' AND MatKhau='{}' """.format(username.upper(),passw)
    # print(query)
    sql=SelectSQL3_SOP(query)
    # print(query)
    return sql

#Kiểm tra tên đăng nhập tồn tại
def GET_ACOUNT_INFO(username):
    query='''exec sp_GetInfoAcount '{}' '''.format(username)
    return SelectSQL3_SOP(query)


