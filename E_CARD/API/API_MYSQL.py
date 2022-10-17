
from email import charset
from sqlite3 import Cursor
import chardet
import pymysql.cursors

host='10.224.69.62'
user='chien'
password='Foxconn88@'
database='foxconn'

# Connect to the database
def GET_TAINI(userid):
    conn = pymysql.connect(host=host,user=user,password=password,database=database,)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query='''SELECT t.USER_ID,t.AGENT_LINE,t.AGENT_WHO,u.USER_NAME,u.NOTDUTY
            FROM  `__person_c_agent_t`  AS t
            INNER JOIN `__person_c_user_t` AS u
            ON u.USER_ID=t.USER_ID 
            WHERE t.USER_ID'''+"=%s  AND t.AGENT_LINE=%s"
    cursor.execute(query,(userid,7))
    result = cursor.fetchone()
    return result

def QueryMYSQL(strquery):
    connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:           
            cursor.execute(strquery)

            # # Create a new record
            # sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            # # sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

def SelectMYSQL(userid):
    conn = pymysql.connect(host=host,user=user,password=password,database=database,)
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM __person_c_user_t WHERE USER_ID=%s"
    cursor.execute(sql,userid)
    result = cursor.fetchone()
    return result

def ADD_USER(USER_ID,USER_NAME,USER_NAME_EXT,JOB_TITLE,CURRENT_OU_CODE,CURRENT_OU_NAME,JOB_TYPE,EMAIL):
    conn = pymysql.connect(host=host,user=user,password=password,database=database,)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    #CURRENT_OU_CODE: mã chi phí
    #CURRENT_OU_NAME: Tên bộ phận
    # query='''    
    #         INSERT INTO `__person_c_user_t` 
    #         (`USER_ID`, `USER_NAME`, `USER_NAME_EXT`, `SEX`,`GRADE`, `JOB_TITLE`,
    #         `CURRENT_OU_CODE`, `CURRENT_OU_NAME`, `NOTES_ID`, `CL_ID`, `CL_NAME`, `EMAIL`, 
    #         `LOCATION`, `ALL_MANAGERS`, `SITE_ALL_MANAGERS`, `BU_ALL_MANAGERS`, `CARD_ID`, `UPPER_OU_CODE`,
    #         `UPPER_OU_NAME`, `NOTDUTY`, `TRAVEL`, `HIREDATE`, `LEAVEDAY`, `USER_ID_EXT`,
    #         `JOB_TYPE`, `ASSISTANT_ID`, `USER_LEVEL`) 
            
    #             VALUES
    #             (''' +"'"+str(USER_ID)+"','"+str(USER_NAME)+"','"+str(USER_NAME_EXT)+ "', '', '', '"+str(JOB_TITLE)+ "',"+'''
    #             '''+ "'"+str(CURRENT_OU_CODE)+"', '" +str(CURRENT_OU_NAME)+"', '"+str(EMAIL)+"', '', '', '"+str(EMAIL)+"',"+'''
    #             '', '', '', '', NULL, NULL, 
    #             NULL, 'No', 'No', NULL, NULL, '', 
    #             '', NULL, 0)
    #             '''
    strquery = '''INSERT INTO __person_c_user_t (USER_ID, USER_NAME,USER_NAME_EXT, JOB_TITLE, CURRENT_OU_CODE, CURRENT_OU_NAME, JOB_TYPE,NOTES_ID, EMAIL) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(strquery,(USER_ID,USER_NAME,USER_NAME_EXT,JOB_TITLE,CURRENT_OU_CODE,CURRENT_OU_NAME,JOB_TYPE,EMAIL,EMAIL))
    conn.commit()
    conn.close()

def UPDATE_USER(USER_ID,USER_NAME,USER_NAME_EXT,JOB_TITLE,CURRENT_OU_CODE,CURRENT_OU_NAME,JOB_TYPE,EMAIL):
    conn = pymysql.connect(host=host,user=user,password=password,database=database,)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    strquery = "UPDATE __person_c_user_t SET USER_NAME=N'"+USER_NAME+"',USER_NAME_EXT=N'"+USER_NAME_EXT+"', JOB_TITLE=N'"+JOB_TITLE+"', CURRENT_OU_CODE=N'"+CURRENT_OU_CODE+"', CURRENT_OU_NAME=N'"+CURRENT_OU_NAME+"', JOB_TYPE=N'"+JOB_TYPE+"', EMAIL='"+EMAIL+"', NOTES_ID='"+EMAIL+"' WHERE USER_ID='"+USER_ID+"'"
    cursor.execute(strquery)
    conn.commit()
    conn.close()
    
def DELETE_USER(USER_ID):
    conn = pymysql.connect(host=host,user=user,password=password,database=database,)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    strquery = "delete from __person_c_user_t WHERE USER_ID='"+USER_ID+"'"
    cursor.execute(strquery)
    conn.commit()
    # print(USER_ID)
    conn.close()
    

















