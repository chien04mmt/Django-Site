
#pip install pymssql
# conn = pymssql.connect(server, username, password, database) 
# MSSQL 접속 
# cursor = conn.cursor() # 쿼리 생성과 결과 조회를 위해 사용
# cursor.execute('SELECT * FROM POST;') 
# row = cursor.fetchone() 
# while row: print(row[0], row[1].encode('ISO-8859-1').decode('euc-kr')) 
# row = cursor.fetchone()





from email import charset
import chardet
import pymssql

#Server
server = '10.224.69.52:3000' 
username = 'sa'
password = 'cnsbgesigndb52@'
#Table list


#Server DB
database_SOP = 'SOP_V2'
database = 'ESIGN4.0'
#Table list


#Truy vấn BẢNG TRẢ LẠI JSON DICT Lấy Varchar
def SelectSQL(strquery):
    conn= pymssql.connect(server,username,password, database,charset='cp936')
    cursor= conn.cursor(as_dict=True)
    cursor.execute(strquery)
    cursor1= cursor.fetchall()   
    conn.close()
    return cursor1


#Truy vấn BẢNG TRẢ LẠI JSON DICT
def SelectSQL2(strquery):
    conn= pymssql.connect(host=server, user=username, password=password, database=database, charset='utf-8')
    cursor= conn.cursor(as_dict=True)
    cursor.execute(strquery)
    cursor1= cursor.fetchall()
    conn.close()
    return cursor1

#Truy vấn BẢNG lấy tiếng việt Nvarchar
def SelectSQL3(strquery):
    conn= pymssql.connect(host=server, user=username, password=password, database=database)
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
def SelectSQL3_SOP(strquery):
    conn= pymssql.connect(host=server, user=username, password=password, database=database_SOP)
    cursor= conn.cursor(as_dict=True)
    cursor.execute(strquery)
    cursor1= cursor.fetchall()    
    conn.close()
    return cursor1



#THỰC HIỆN INSERT HOẶC UPDATE
def QuerySQL_SOP(strquery):		
    conn= pymssql.connect(host=server, user=username, password=password, database=database_SOP)
    cursor= conn.cursor()		
    cursor.execute(strquery)
    conn.commit()		
    conn.close()	
    
    

#THỰC HIỆN QUERY TRẢ VỀ TRUE AND FALSE
def QuerySQL2_SOP(strquery):
        try:
            conn= pymssql.connect(host=server, user=username, password=password, database=database_SOP)
            cursor= conn.cursor()		
            cursor.execute(strquery)
            conn.commit()
            #conn.close()
            return True
        except Exception as ex:    
            print(ex)      
            return str(ex)
	

