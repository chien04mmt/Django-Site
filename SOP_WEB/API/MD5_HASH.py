# Python 3 code to demonstrate the 
# working of MD5 (byte - byte)
  
# import hashlib
# result = hashlib.md5(b'Foxcon88#')
# print(result.hexdigest())
# import API_MSSQL 
import base64

# Mã hóa
def Encript_Pass(password):
    message = password
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

#Giải mã
def Decript_Pass(password):
    base64_bytes = password.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


# print(Decript_Pass('Rk94Y29ubjg4IQ=='))
# def test():
              
#     with open('E:\\DJANGO\\E-SIGN-4.0 All\\Esign4\\API\\user.txt', 'r', encoding='utf-8') as o:# cai nay dung cai decode cua no chua hay la cai G6 gì đó
#         alls =  o.read().split('\n')
#         for query in alls:
#             i=query[query.index('||')+2:]
#             query =Encript_Pass(query[0:query.index('||')])
#             query="UPDATE [Users]  SET [passWord2] ='"+str(query)+"' WHERE ID='"+str(i)+"'"
#             if not API_MSSQL.QuerySQL2(query):
#                 with open('notexcute.txt', 'a+', encoding='utf-8') as w:
#                     w.write(query+'\n')                 
#             else:
#                 print( str(i)+ ' \n')

# print(Decript_Pass("pxV+JvWZDMeJ79YXNF9Sb682uJNXspBSU75lHcOOYSc="))       





