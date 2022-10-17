import pymssql
import MD5_HASH
#Nhấn CRT+SHIFT+P ==> CHọn Python:Select interpreter đổi sang ver python 3.10


server = '10.224.69.52:3000' 
database = 'ESIGN4.0'
username = 'sa' 
password = 'cnsbgesigndb52@' 
  
  
def AUTO_UPDATE_PASS():#Hàm mã hóa mật khẩu và cập nhật vào cơ sở dũ liệu E.Sign4.0                              
    with open('API/showpass.txt','r',encoding='utf-8') as r:
        conn= pymssql.connect(host=server, user=username, password=password, database=database,charset='cp936')
        cursor= conn.cursor(as_dict=True)
        for row in r:
            if len(row)<2:
                conn.close()
                return
            user=row[0:row.index("_[[")]
            passw=row[row.index("_[[")+3:-2]
            passw=MD5_HASH.Encript_Pass(passw)
            query="UPDATE Users SET [PassWord]='"+str(passw)+"' WHERE UserID='"+str(user)+"'"
            print(passw)
            cursor.execute(query)


AUTO_UPDATE_PASS()