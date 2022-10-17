
from pydoc import doc
import requests
from requests.structures import CaseInsensitiveDict
from API.API_MSSQL import *



mail_user='cncs-vn-code@mail.foxconn.com'
mail_passw='Foxconn88!'
mail_from='cncs-vn-esign@foxconn.com'

hostserver='https://10.224.70.55:8080'
system_name="外部公文管理系統 Hệ thống quản lý công văn"
server_domain="https://10.224.70.55:8080"
server_link=hostserver

contact1="""<p style="color:#0000">            
            -----------------鄧氏垂楊 ------------------<br>
            ●•꧁Ƹ̵̡Ӝ̵̨̄Ʒ Đặng Thị Thùy Dương Ƹ̵̡Ӝ̵̨̄Ʒ꧂•●<br>           
            _           分機: 535-20221<br>
            _           手機: 0394447888<br>
            _   郵件: thuyduong.dang@foxconn.com<br>           
            </p>
        """
        
contact="""<p style="color:#28a745!important">            
            *****************************************************<br>
            Đặng Thị Thùy Dương/鄧氏垂楊 <br>
            HR Central (VN-HR)<br>
            Tel/分機  (535) 20221<br>
            Mobile/手機: (+84) 0394447888<br>
            Mailbox/郵箱地址:thuyduong.dang@foxconn.com<br>
            Addess: Lô B, KCN Quế  Võ, P.Nam Sơn, TP.Bắc Ninh,  Tỉnh Bắc Ninh. Việt Nam.<br>
            *****************************************************   
            </p>
        """
#-----------------------------------------------------------------config2
url = 'http://10.224.69.51:88/smtp.asmx'
headers = CaseInsensitiveDict()
headers["Content-Type"] = "text/xml; charset=utf-8"
headers["Content-Length"] = "length"
headers["SOAPAction"] = "http://tempuri.org/MailSendText_Net"

#headers["SOAPAction"] = "http://tempuri.org/SendMailSMTP_Web"


#Hàm gửi mail bằng Soap 1.1
def SEND_MAIL(mailSystem,mailto,mailcc,docno,Who,dvphutrachchinh,dvhotro,dvkhac,ByName):
    linkdoc=server_domain+'/chitietdon_CVD/?Sodon='+str(docno)
    linkdoc_a=server_link+'/chitietdon_CVD/?Sodon='+str(docno)
    subject_=system_name+ """==> Thông báo tạo đơn trên hệ thống số: """+str(docno)
    
    #Mail thông báo tạo đơn thành công
    body_CreatedDoc="""
                    <h3>Thông báo tạo đơn thành công số: ---- {} ----</h3>                  
                    <p>Xem chi tiết đơn tại liên kết : <a href="{}">{}</a></p>
                  """.format(docno,linkdoc_a,linkdoc_a)
                  
    #Mail nhắc ký tổng giám đốc
    if Who=='TGD':
          subject_=system_name+ "【中央文管系統消息】，尊敬的 阮氏水 主管,單號: {},【文件清單】已被批准".format(docno)
          body_CreatedDoc="""          
            <h3>
            【中央文管系統消息】，尊敬的 阮氏水 主管,單號: {},<br>
            【文件清單】已被批准</h3>           
            <p>
              您好！單號: {},【文件清單】<br/>
              已被批准請點擊以下系統鏈接查看簽核進度：<br/>
              <li><a href='{}'>{}</a></li><br/>
            </p>
          """.format(docno,docno,linkdoc,linkdoc)
          
    #Mail nhắc ký người tiếp theo
    if Who=='NextAppro':
          subject_=system_name+ " Thông báo đơn chờ ký duyệt : {}".format(docno)
          body_CreatedDoc="""          
            <h3>Thông báo đơn chờ ký duyệt</h3>           
            <p>           
              Xin chào bạn ! Bạn có 1 đơn yêu cầu phê duyệt số: 【{}】<br/>
              Chi tiết đơn xem liên kết phía dưới：<br/>
              <li><a href='{}'>{}</a></li><br/>           
            </p>
          """.format(docno,docno,linkdoc,linkdoc)

    #Mail thông báo triển khai từ tổng giám đốc
    if Who=='Group':
          subject_=system_name+ "Thông báo triển khai công văn số đơn : {}, đã được tổng giám đốc phê duyệt !".format(docno)
          body_CreatedDoc="""          
            <h3>Thông báo từ hệ thống</h3>           
            <p>             
              Xin chào các bạn ! Số đơn thực hiện: 【{}】<br/>
              Đã được tổng giám đốc phê duyệt và phân phối đơn vị thực hiện như sau:<br/>
              <br/>
              Đơn vị phụ trách chính:
              {}
              <br/>
              Đơn vị phụ hỗ trợ :<br/>
              {}
              <br/>              
              Đơn vị khác (nếu có):<br/>
              <li>{}</li><br/>
              <br/>
              Xem chi tiết liên kết phía dưới:<br/>
              <li><a href='{}'>{}</a></li><br/>             
            </p>                 
          """.format( docno,dvphutrachchinh,dvhotro,dvkhac,linkdoc,linkdoc)
   
    #Mail thông báo kêt thúc đơn
    if Who=='Finished':
          subject_=system_name+ "Thông báo đóng đơn số : {}".format(docno)
          body_CreatedDoc="""          
            <h3>Thông báo từ hệ thống</h3>           
            <p>            
              Xin chào bạn ! Số đơn thực hiện: 【{}】đã được được các phòng ban thực hiện hoàn thành<br/>
              Người thực hiện đóng đơn :<br/>
              <li>{}</li>
              Xem chi tiết đơn tại liên kết phía dưới:<br/>
              <li><a href='{}'>{}</a></li><br/>              
            </p>                 
          """.format(docno,docno,dvphutrachchinh,dvhotro,linkdoc,linkdoc,ByName)
                
          
          
    data ='''<?xml version="1.0" encoding="utf-8"?>
          <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
              <MailSendText_Net xmlns="http://tempuri.org/">
                <from>'''+mailSystem+'''</from>
                <mailto>'''+mailto+'''</mailto>
                <cc>'''+mailcc+'''</cc>
                <subject>'''+subject_+'''</subject>
                <msg>
                      <![CDATA[
                          <div style="width:800px !important">
                            <h3 style="color:Green;">'''+system_name+'''</h3>
                            <hr/>
                            <div style="color:#1260d8;margin-top: 10px;margin-left: 10px;">
                                <div style="padding: 10px;border: 2px solid #e5c59b;">
                                  '''+body_CreatedDoc+'''
                                  <br>
                                  <div style="color:#0693e3;">                                 
                                  '''+str(contact)+'''                             
                                  </div>
                              </div>
                            </div>  
                        </div> 
                      ]]>
                </msg>
                <bcc></bcc>
              </MailSendText_Net>
            </soap:Body>
          </soap:Envelope>
    '''
    resp = requests.post(url, headers=headers, data=data.encode("utf-8"))
    if(resp.status_code==200):return True
    else:return False

