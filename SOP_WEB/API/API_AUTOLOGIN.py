from API.API_MSSQL import *
from  API.API_USER import GET_USERNAME
from API.MD5_HASH import Encript_Pass,Decript_Pass
from SOP_WEB.settings import BASE_DIR
from ipware import get_client_ip
import socket



def SAVE_USER_AUTOLOGIN(userID):
    sql=GET_USERNAME(userID)
    if sql!='' :
        with open('autologin.sam','a+',encoding='utf-8') as w:
            w.write(Encript_Pass(str(sql))+'\n')
         


def SAVE_LOG_LOGIN(user,request):
    hostname = socket.gethostname()
    ip_address =get_client_ip(request)[0]
    # print(ip_address)
    query='''
        INSERT INTO [ESIGN4.0].[dbo].[Log_User]
        ([UserID]
            ,[IPAddress]
            ,[MacAddress]
            ,[ComputerName]
            ,[Detail]
            ,[SysDate]
            ,[LoginFrom])
        VALUES'''+"('"+str(user)+"','"+str(ip_address)+"','','"+str(hostname)+"','Logged in',SYSDATETIME(),'')"
    sql= QuerySQL(query)





