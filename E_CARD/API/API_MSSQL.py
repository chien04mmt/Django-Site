
#pip install pymssql
# conn = pymssql.connect(server, username, password, database) 
# MSSQL 접속 
# cursor = conn.cursor() # 쿼리 생성과 결과 조회를 위해 사용
# cursor.execute('SELECT * FROM POST;') 
# row = cursor.fetchone() 
# while row: print(row[0], row[1].encode('ISO-8859-1').decode('euc-kr')) 
# row = cursor.fetchone()

import pymssql

server = '10.224.54.26:4433' 
database = 'VN_Door_162'
username = 'sa'
password = 'Foxconn()'


table_Users="Users_New"


#Truy vấn BẢNG TRẢ LẠI JSON DICT Lấy Varchar
def SelectSQL(strquery):
    conn= pymssql.connect(server,username,password, database,charset='cp936')
    cursor= conn.cursor(as_dict=True)
    cursor.execute(strquery)
    cursor1= cursor.fetchall()   
    conn.close()
    return cursor1


#THỰC HIỆN INSERT HOẶC UPDATE
def QuerySQL(strquery):		
    conn= pymssql.connect(host=server, user=username, password=password, database=database)
    cursor= conn.cursor()		
    cursor.execute(strquery)
    conn.commit()		
    conn.close()	
    
#Truy vấn BẢNG TRẢ LẠI JSON DICT
def SelectSQL2(strquery):
    conn= pymssql.connect(host=server, user=username, password=password, database=database, charset='utf-8')
    cursor= conn.cursor(as_dict=True)
    cursor.execute(strquery)
    cursor1= cursor.fetchall()
    conn.close()
    return cursor1

#THỰC HIỆN QUERY TRẢ VỀ TRUE AND FALSE
def QuerySQL2(strquery):
        try:
            conn= pymssql.connect(host=server, user=username, password=password, database=database)
            cursor= conn.cursor()		
            cursor.execute(strquery)
            conn.commit()
            #conn.close()
            return True
        except Exception as ex:    
            print(ex)      
            return False
	
 
#Truy vấn BẢNG lấy tiếng việt Nvarchar
def SelectSQL3(strquery):
    conn= pymssql.connect(host=server, user=username, password=password, database=database)
    cursor= conn.cursor(as_dict=True)
    cursor.execute(strquery)
    cursor1= cursor.fetchall()    
    conn.close()
    return cursor1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


