
from certifi import contents
import requests
from requests.structures import CaseInsensitiveDict
from API.API_MSSQL import *



#-----------------------------------------------------------------config2
url = 'http://10.224.69.51:88/smtp.asmx'
headers = CaseInsensitiveDict()
headers["Content-Type"] = "text/xml; charset=utf-8"
headers["Content-Length"] = "length"
headers["SOAPAction"] = "http://tempuri.org/SendMailSMTP_Web"

#-----------------------------------------------------------------config1
url1 = 'http://10.224.69.51/SMTPService/SMTPService.asmx'
headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "text/xml;  charset=utf-8"
headers1["Content-Length"] = "length"

mail_user='cncs-vn-code@mail.foxconn.com'
mail_passw='Foxconn88!'
mail_from='fkvehicle@foxconn.com'

hostserver='https://fkvehicle.efoxconn.com'
hostserver_internet='https://fkvehicle.efoxconn.com'
system_name="Artice 2.0 System"
contact="Contact Information (Admin: Tran Net Thom, Ext: 32050; email: idsbg-hr-vnga09@mail.foxconn.com)"


#------------------HỆ THỐNG ĐIỀU XE----------------------------------------------------------------------------------------------------------------

Name_System="車輛分配系統 2.0"

noidungchonguoiky='''
    <div>敬愛的用戶，</div>
    <div>您好，客服問題單號 </div>
    <div>待您受理，請知悉，謝謝。</div>
    <div>注意 : 此為系統通知信箱,請勿用此mail address 回覆</div>
'''

noidungchonguoilamdon=''' 

<h3>您好！</h3>
<div>您的一封“越南車調申請單”已全部簽核完成。</div>
<div>-------本郵件為系統郵件，請勿直接回復-------</div>
<div></div><br/>

<H3>Xin chào! </H3>
<div>One of your "Application to transfer a vehicle to Vietnam" has been signed and completed. </div>
<div>------- This email is a system email, please do not reply directly ------- </div>
<div></div>
'''
  
thongbaodondakyduyet='''
<h3>您好！</h3>
<div>您的一封“越南車調申請單”已全部簽核完成。</div>
<div>-------本郵件為系統郵件，請勿直接回復-------</div>
<div></div><br/>

<H3>Xin chào! </H3>
<div>One of your "Application to transfer a vehicle to Vietnam" has been signed and completed. </div>
<div>------- This email is a system email, please do not reply directly ------- </div>
<div></div>
'''
  
subject_kethuc='''越南車調申請單結案通知! 單號 (Announcement of closing registration for car transfer in Vietnam! Formber): '''
subject_khoitao='''已创建越南通知表中的汽车转让申请! 單號 (A car transfer app in Vietnam has been created! Tracking number): '''
subject_kydon='''待您受理! 單號(Waiting for your acceptance! Claim number): '''

subject_capxe="車調申請通過， 車調已同意派車 (The system administrator has assigned the vehicle to you)"
subject_cancel="請求已被取消或拒絕 (Request has been canceled or denied)"




#Hàm gửi mail bằng Soap 1.1
def SEND_PASSWORD(mailto,mailcc,password,request):
    data ='''<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <SendMailSMTP_Web xmlns="http://tempuri.org/">
                  <from>{}</from>
                  <mailto>{}</mailto>                  
                  <cc></cc>
                  <subject>Forgot Password ! Vihicle 2.0</subject>
                  <msg>
                    <![CDATA[
                        <h3 style="color:Green;">{}</h3>
                        <div>
                          Please delete this mail affter you readed. Thanks  so  much!<br>
                          Your password login is: <span style="color:Green;">{}</span>
                          </div><br> 
                          <div>The system URL Login is: {}</div>                         
                          <a>{}</a>
                        </div>
                      ]]>
                  </msg>
                  <bcc>string</bcc>
                </SendMailSMTP_Web>
              </soap:Body>
            </soap:Envelope>
    '''.format(mail_from,mailto,system_name,system_name,password,hostserver,contact)
    
    resp = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False




#Gửi mail cho người làm đơn điều xe
def SEND_MAIL_TO_APPLY_PERSON(mailto,UserID_autologin,docno,hostserver_,subject_khoitao,noidungchonguoilamdon):
      return SEND_MAIL_DIEUXE(mailto,UserID_autologin,docno,hostserver_,subject_khoitao,noidungchonguoilamdon)


#Gửi mail cho người ký
def SEND_MAIL_TO_APPROVAL(mailto,UserID_autologin,docno,hostserver_):
      return SEND_MAIL_DIEUXE(mailto,UserID_autologin,docno,hostserver_,subject_kydon,noidungchonguoiky)


#Gửi mail khi đã hoàn thành ký duyệt
def SEND_MAIL_FINISH_TO_APPLY_PERSON(mailto,UserID_autologin,docno,hostserver_,subject_kethuc,thongbaodondakyduyet):
      return SEND_MAIL_DIEUXE(mailto,UserID_autologin,docno,hostserver_,subject_kethuc,thongbaodondakyduyet)




#Gửi mail tiếng việt
def SEND_MAIL_DIEUXE(mailto,UserID_autologin,docno,hostserver_,subject,message):
    linkdoc=hostserver+'/detail_bus/?docno='+str(docno)
    autologin_link=linkdoc
    if len(UserID_autologin)>3:autologin_link=str(linkdoc)+ '''&tktlog='''+str(UserID_autologin)
    subject_=subject+str(docno)+' ，請知悉!'
    
    data="""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <SendMailSMTP_Web xmlns="http://tempuri.org/">
                  <from>{}</from>
                  <mailto>{}</mailto>                  
                  <cc></cc>
                  <subject>{}</subject>
                  <msg>
                    <![CDATA[
                          <h3 style="color:Green;">{}</h3>
                          <div>
                          現有一份 文件簽核申請,申請單號為 : <a href='{}'>{}</a>
                          </div><br> 
                          <div>系統網址為: <a href='{}'>{}</a></div>
                         {}
                         <div style="color:Blue">{}</div>
                      ]]>
                  </msg>
                  <bcc>string</bcc>
                </SendMailSMTP_Web>
              </soap:Body>
            </soap:Envelope>             
      """.format(mail_from,mailto,subject,system_name,autologin_link,linkdoc,autologin_link,linkdoc,message,contact)
    resp = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False
    
    

#Hàm gửi mail ĐIỀU XE bằng Soap 1.1
def SEND_MAIL_DIEUXE1(mailto,UserID_autologin,docno,hostserver_,subject,message):
    linkdoc=hostserver+'/detail_bus/?docno='+str(docno)
    autologin_link=linkdoc
    if len(UserID_autologin)>3:autologin_link=str(linkdoc)+ '''&tktlog='''+str(UserID_autologin)
    subject_=subject+str(docno)+' ，請知悉!'
    
    data ='''<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <SendMailSMTP_Web xmlns="http://tempuri.org/">
                  <from>'''+mail_from+'''</from>
                  <mailto>'''+mailto+'''</mailto>                  
                  <cc></cc>
                  <subject>'''+subject_+'''</subject>
                  <msg>
                    <![CDATA[
                          <div style="width:800px !important">
                            <h3 style="color:Green;">'''+system_name+'''</h3>
                            <hr/>
                            <div style="color:#1260d8;margin-top: 10px;margin-left: 10px;">
                                <div style="padding: 10px;border: 2px solid #e5c59b;">
                                  <p>申請通過，派車信息如下(Application approved,Car arrange information as bellow):<br>
                                  派車申請單號(Document No): '''+str(docno)+'''<br><hr/>
                                  <span>******************************************************</span><hr/>
                                  
                                  車牌號及司機信息(Driver Information with License Plate): <br>'''+str(bienso)+'''<br>
                                  候車時間(Time): '''+str(thoigiancho)+'''<br>
                                  候車地點(Waiting Point): '''+str(noicho)+'''<br>
                                  同乘人(Passengers): '''+str(hanhkhach)+'''<br>                            
                                  用車路線(Route): <br>
                                    <li>[出發地](Departure): '''+ str(diemdi) + ''' >> [目的地](Terminus): '''+str(diemden)+'''</li><br>  
                                          
                                  <span>******************************************************</span>                    
                                  </p><br>
                                  <div style="color:Blue;">'''+str(contact)+'''</div>
                              </div>
                            </div>  
                        </div> 
                      ]]>
                  </msg>
                  <bcc>string</bcc>
                </SendMailSMTP_Web>
              </soap:Body>
            </soap:Envelope>      
    '''
    resp = requests.post(url1, headers=headers1, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False




#Hàm gửi mail cấp xe thành công
def SEND_MAIL_CAPXE(mailto,docno,bienso,diemdi,diemden,thoigiancho,noicho,hanhkhach):
    data ='''<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <SendMailSMTP_Web xmlns="http://tempuri.org/">
                  <from>'''+mail_from+'''</from>
                  <mailto>'''+mailto+'''</mailto>                  
                  <cc></cc>
                  <subject>'''+subject_capxe+ ''' : ''' +str(docno)+''' ，請知悉!</subject>
                  <msg>
                    <![CDATA[
                          <div style="width:800px !important">
                            <h3 style="color:Green;">'''+system_name+'''</h3>
                            <hr/>
                            <div style="color:#1260d8;margin-top: 10px;margin-left: 10px;">
                                <div style="padding: 10px;border: 2px solid #e5c59b;">
                                  <p>申請通過，派車信息如下(Application approved,Car arrange information as bellow):<br>
                                  派車申請單號(Document No): '''+str(docno)+'''<br><hr/>
                                  <span>******************************************************</span><hr/>
                                  
                                  車牌號及司機信息(Driver Information with License Plate): <br>'''+str(bienso)+'''<br>
                                  候車時間(Time): '''+str(thoigiancho)+'''<br>
                                  候車地點(Waiting Point): '''+str(noicho)+'''<br>
                                  同乘人(Passengers): '''+str(hanhkhach)+'''<br>                            
                                  用車路線(Route): <br>
                                    <li>[出發地](Departure): '''+ str(diemdi) + ''' >> [目的地](Terminus): '''+str(diemden)+'''</li><br>  
                                          
                                  <span>******************************************************</span>                    
                                  </p><br>
                                  <div style="color:Blue;">'''+str(contact)+'''</div>
                              </div>
                            </div>  
                        </div> 
                      ]]>
                  </msg>
                  <bcc>string</bcc>
                </SendMailSMTP_Web>
              </soap:Body>
            </soap:Envelope>      
    '''
    resp = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False
    

#Hàm gửi mail cấp xe thành công
def SEND_MAIL_CAPXE1(mailto,docno,bienso,diemdi,diemden,thoigiancho,noicho,hanhkhach):
    data ='''
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Header>
        <ContainsKey xmlns="http://tempuri.org/SmtpService/SmtpService">
          <ContainsKey>string</ContainsKey>
          <UserName>'''+mail_user+'''</UserName>
          <Password>'''+mail_passw+'''</Password>
        </ContainsKey>
      </soap12:Header>
      <soap12:Body>
        <SendMail xmlns="http://tempuri.org/SmtpService/SmtpService">
          <obj>
            <mailto>'''+str(mailto)+'''</mailto>
            <cc></cc>
            <from>'''+mail_from+'''</from>
            <subject>'''+subject_capxe+ ''' : ''' +str(docno)+''' ，請知悉!</subject>
            <body>
                <![CDATA[
                    <!DOCTYPE html>
                    <html>
                    <head>
                    	<meta charset="utf-8">
                    	<meta name="viewport" content="width=device-width, initial-scale=1">
                    	<title></title>
                    </head>
                    <body>
                         <div style="width:800px !important">
                            <h3 style="color:Green;">'''+system_name+'''</h3>
                            <hr/>
                            <div style="color:#1260d8;margin-top: 10px;margin-left: 10px;">
                                <div style="padding: 10px;border: 2px solid #e5c59b;">
                                  <p>申請通過，派車信息如下(Application approved,Car arrange information as bellow):<br>
                                  派車申請單號(Document No): '''+str(docno)+'''<br><hr/>
                                  <span>******************************************************</span><hr/>
                                  
                                  車牌號及司機信息(Driver Information with License Plate): <br>'''+str(bienso)+'''<br>
                                  候車時間(Time): '''+str(thoigiancho)+'''<br>
                                  候車地點(Waiting Point): '''+str(noicho)+'''<br>
                                  同乘人(Passengers): '''+str(hanhkhach)+'''<br>                            
                                  用車路線(Route): <br>
                                    <li>[出發地](Departure): '''+ str(diemdi) + ''' >> [目的地](Terminus): '''+str(diemden)+'''</li><br>  
                                          
                                  <span>******************************************************</span>                    
                                  </p><br>
                                  <div style="color:Blue;">'''+str(contact)+'''</div>
                              </div>
                            </div>  
                        </div> 
                    </body>
                    </html>
                   
                  ]]>
            </body>
            <format>Html</format>
            <priority>Normal</priority>
          </obj>
        </SendMail>
      </soap12:Body>
    </soap12:Envelope>
    '''
    resp = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False
    #----------------------------------------------------------------------------------------------------------------------------------
    

#Hàm gửi mail cấp xe thành công
def SEND_MAIL_HUYDON(mailto,docno,lydo):
    data ='''
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Header>
        <ContainsKey xmlns="http://tempuri.org/SmtpService/SmtpService">
          <ContainsKey>string</ContainsKey>
          <UserName>'''+mail_user+'''</UserName>
          <Password>'''+mail_passw+'''</Password>
        </ContainsKey>
      </soap12:Header>
      <soap12:Body>
        <SendMail xmlns="http://tempuri.org/SmtpService/SmtpService">
          <obj>
            <mailto>'''+str(mailto)+'''</mailto>
            <cc></cc>
            <from>'''+mail_from+'''</from>
            <subject>'''+subject_cancel+str(docno)+''' ，請知悉!</subject>
            <body>
                <![CDATA[
                        <h3 style="color:Green;">'''+str(Name_System)+'''</h3>
                        <div>'''+str(subject_cancel)+'''</div><br>
                        <div>原因(lý do): '''+str(lydo)+'''</div><br>
                        <div></div><br>
                       <div style="color:Blue;">'''+str(contact)+'''</div>
                ]]>
            </body>
            <format>Html</format>
            <priority>Normal</priority>
          </obj>
        </SendMail>
      </soap12:Body>
    </soap12:Envelope>
    '''
    resp = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False
    #----------------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    
    
    
    
    

