
# pip install pythonnet
#python 3.8
# import clr
# pip install -U clr-loader


#Nhấn CRT+SHIFT+P ==> CHọn Python:Select interpreter đổi sang ver python 3.8
import clr


clr.AddReference("E:/DJANGO/E-SIGN-4.0 All/Esign4/API/SysSecurity.dll")
from SysSecurity import AccountManage 
ojb = AccountManage()

def PWDDecode_Str(pwd):
    encode=ojb.PWDDecode(pwd)
    return encode

def PWDEncode_Str(pwd):
    encode=ojb.PWDEncode(pwd)
    return encode



def DECODE_PASS():
    with open('API/user1.txt', 'r', encoding='utf-8') as o:
        alls= o.read().split('\n')
        for query in alls:
            if len(query)<3: return
            user=query[0:query.index("_[[")]
            passw=query[query.index("_[[")+3:-2]

            passw=PWDDecode_Str(str(passw))
            with open('API/showpass.txt','w',encoding='utf-8') as w:
                 w.write(str(user)+"_[["+(str(passw))+"]]"+ "\n")
                 print('OK')


DECODE_PASS()
    

