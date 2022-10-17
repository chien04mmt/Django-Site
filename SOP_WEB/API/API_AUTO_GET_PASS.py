import pymssql
import MD5_HASH
#Nhấn CRT+SHIFT+P ==> CHọn Python:Select interpreter đổi sang ver python 3.10

from time import strftime

server = '10.224.69.52:3000' 
database = 'eSign_New'
username = 'sa' 
password = 'cnsbgesigndb52@' 


def AUTO_GET_USER():#Hàm lấy thông tin mã thẻ và mật khẩu vào file user1.txt
    conn= pymssql.connect(host=server, user=username, password=password, database=database,charset='cp936')
    cursor= conn.cursor(as_dict=True)
    query='''
    SELECT [UserID],[PassWord] FROM [Users]
    '''
    cursor.execute(query)

    with open('API/user1.txt','w',encoding='utf-8') as w:
        for row in cursor:
            w.write(row['UserID']+"_[["+(str(row['PassWord']))+"]]"+ "\n")
            print("OK")
        conn.close()

         
AUTO_GET_USER()
