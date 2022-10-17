
import chardet
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

from API_MSSQL import QuerySQL2

# # Register       
# def Auto_Creat_User(username,password1,email):
#     my_user= authenticate(username=username, password= password1) 
#     if my_user is None:
#         try:
#             User.objects.create_user(username,email,password1,is_staff=True)
#             #User.objects.create_user(username,email,password1,is_staff=True, is_superuser=True)
#         except:
#             print("NG")
            
def Auto_Update_Users(Username,password1,Email):
    sqlquery="UPDATE [Users] SET [PassWord]='"+str(password1)+"',[mailbox]='"+str(Email)+"' WHERE [UserID]='"+str(Username)+"'"
    if QuerySQL2(sqlquery):
        print("OK")
    else:
        with open('NG_update_pass.txt','a+',encoding='utf-8') as w:
            w.write(Username + '\n')
                    
with open('C:\\Users\DELL-FUNING\Desktop\\Esign4\\home\\user.txt','r',encoding='utf-8') as w:
    files=w.read().split('\n')
    for ite in files:
        user=ite.index("user=")+6
        mail=ite.index("Emai=")+6
        Email= ite[mail:]
        ae=ite[user:len(ite)-len(Email)]
        Username=ae[0:ae.index(",")]
        p=ite[ite.index("Name=")+6:]
        FullName=p[0:p.index(",")]
        pas=ite[ite.index("Passw=")+7:]
        password1=pas[0:pas.index(",Emai=")]
        # Auto_Creat_User(Username,password1,Email)
        Auto_Update_Users(Username,password1,Email)
        
