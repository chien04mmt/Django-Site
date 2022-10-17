from django.shortcuts import render
from django.http import JsonResponse
from http.client import HTTPResponse
from API.SOP_DB import *
from API.API_MSSQL import SelectSQL3_SOP,QuerySQL2_SOP,QuerySQL_SOP


    
#------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------TẠO YÊU CẦU ĐƠN-----------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------


# Đơn xin phát hành văn bản
def DonXinPhatHanhVB(request):
    data=request.GET
    return render(request,'HOME/lamdon/donxinphathanhvb.html')


# Đơn xin hủy Văn bản
def HuyMaVanBan(request):
    data=request.GET
    return render(request,'HOME/lamdon/donxinhuymavb.html')


# Đơn xin phế bỏ văn bản
def PheBoVanBan(request):
    data=request.GET
    return render(request,'HOME/lamdon/donxinphebovb.html')


# Đơn xin sửa chữa văn bản
def SuaChuaVanBan(request):
    data=request.GET
    return render(request,'HOME/lamdon/donxinsuavb.html')




#Đơn xin mã văn bản
def DonXinMaVB(request):     
    try:        
        data=request.GET 
        user=request.user.get_username()
        docno=data['ApplicationNO'][0:data['ApplicationNO'].index('-')+4]
 
        if data['action']=='CREATE':docno={'CodeDocument':docno+str(CreatedCodeAuto('CodeDocument','RegisterCodeDocument'))}
        elif data['action']=='UPDATE': docno={'CodeDocument':str(data['ApplicationNO'])}
        
        data=data.dict() 
        data.update(docno)
        data['CreatedBy']=user
       
        sql=InsertRegisterCode(data)
        if sql!=True:return JsonResponse({'error':str(sql)},status=400)
        sql=InsertDocRef(data)
        if sql!=True:return JsonResponse({'error':str(sql)},status=400)

        sql=InsertApprovalSection(data)
        if sql!=True:return JsonResponse({'error':str(sql)},status=400)
        
        sql=ListApprovalSection(docno['CodeDocument'])  
        return JsonResponse({'returndata':docno,'list_appro':sql},status=200)
    
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)



#Hiển thị thông tin chi tiết đơn xin mã văn bản
def NoiDungDonXinMa(request):
    try:
        data=request.GET
        docno=data['CodeDocument']
        
        if InsertRegisterCode(data):
            if InsertDocRef(data):
                if InsertApprovalSection(data):return JsonResponse({'returndata':''},status=200)
        return JsonResponse({'returndata':''},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)

    
    

# #Duyệt đăng ký mã VB(C-00010: đã ký,C-00011:từ chối,C-00009: chờ ký)
# def DuyetDKMavb(request):
#     try:
#         data=request.GET
#         Orders=GetTypeOrdersApprover(data['CodeDocument'])

#         if len(Orders)>0:#Nếu còn người chờ ký trong bảng approval section (C-00010: đã ký,C-00011:từ chối,C-00009: chờ ký)
#             State=Orders[0]['Orders']
#             State=GET_Orders_Appro(State)

#             #Cập nhật đơn khi ký xong
#             query='''UPDATE [ApprovalSection]
#                             SET Comment='{}',Status='C-00010',UpdatedDate=GETDATE(),UpdatedBy='{}'
#                             WHERE CodeDocument='{}' and UserName='{}'
                            
#                      UPDATE RegisterCodeDocument 
#                             SET States ='{}',UpdatedBy='{}',UpdatedDate=GETDATE() 
#                             WHERE CodeDocument ='{}'
#                     '''.format(data['Comment'],data['User'],data['CodeDocument'],data['User'],State,data['User'],data['CodeDocument'])
#             QuerySQL_SOP(query)


#             if State=='A15':#Nếu là DCC ký thì hiệu lực cho đơn
#                 query='''UPDATE RegisterCodeDocument SET States ='{}',UpdatedBy='{}',EffectiveDate=GETDATE(),UpdatedDate=GETDATE() 
#                             WHERE CodeDocument = '{}'
#                             '''.format(State,data['User'],data['CodeDocument'])  
#                 QuerySQL_SOP(query)
                
#         return JsonResponse({'returndata':''},status=200)
#     except Exception as ex: return JsonResponse({"error":str(ex)},status=400)




#TÌm các mã văn bản DCC để hủy mã
def TimMaDeHuyMaVB(request):
    try:
        data=request.GET      
        user=request.user.get_username()
        query='''exec sp_ListRegisterCodeDocumentByDCC '{}','{}','{}','{}','{}','{}'
                '''.format(data['CodeDocument'],user,data['DocNo'],
                           '1',data['FromApplicationDate'],data['ToApplicationDate'])  
        print(query)   
        sql=SelectSQL3_SOP(query)

        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)


    
# #Hủy bỏ đơn đăng ký mã văn bản
# def HuyDKMavb(request):
#     try:
#         data=request.GET              
#         Orders=GetTypeOrdersApprover(data['CodeDocument'])
#         if len(Orders)>0:#Nếu còn người chờ ký trong bảng approval section (C-00010: đã ký,C-00011:từ chối,C-00009: chờ ký)
           
#             #Cập nhật đơn khi ký xong
#             query='''UPDATE [ApprovalSection]
#                             SET Comment='{}',Status='C-00011',UpdatedDate=GETDATE(),UpdatedBy='{}'
#                             WHERE CodeDocument='{}' and UserName='{}'
                            
#                      UPDATE RegisterCodeDocument 
#                             SET States ='{}',UpdatedBy='{}',UpdatedDate=GETDATE() 
#                             WHERE CodeDocument ='{}'
#                     '''.format(data['Comment'],data['User'],data['CodeDocument'],data['User'],'A20',data['User'],data['CodeDocument'])
#             QuerySQL_SOP(query)
            
#         return JsonResponse({'returndata':''},status=200)
#     except Exception as ex: return JsonResponse({"error":str(ex)},status=400)

    
    
   
#Tạo đơn hủy mã văn bản
def TaoDonHuyMaVB(request):
    try:
        data=request.GET
        query='''  SELECT rd.Department,rd.ApplicationSite,dcc.CodeDocument,dcc.DocNo,dcc.DocName,dr.EstimatedCloseDate
                    FROM DCC_Ref  as dcc
                    left JOIN RegisterCodeDocument as rd on rd.CodeDocument=dcc.CodeDocument
                    left join DocumentRef as dr on rd.CodeDocument=dr.CodeDocument
                    WHERE dcc.DocNo='{}'
                    '''.format(data['DocNo'])
        sql=SelectSQL3_SOP(query)
        if len(sql)>0: sql=sql[0]
        return render(request,'HOME/lamdon/donxinhuymavb.html',context={'sql':sql})
    except Exception as ex: return HTTPResponse(str(ex),status=400)

 


#Tạo đơn hủy mã văn bản State('G01':Đơn mới, 'G15':Kết án)
def LuuDonHuyMaVB(request):
    try:
        data=request.GET
        user=request.user.get_username()
        docno=data['CancelDocument'][0:data['CancelDocument'].rindex('-')+2]

        if data['Action']=='CREATE':
            docno=docno+str(CreatedCodeAuto('CancelDocument','RegisterCancelDocument'))
            #Tạo lưu trình ký
            query='''EXEC sp_InsertApprovalSection_CancelDocument '{}','{}','{}' '''.format(docno,user,data['Department'])
            QuerySQL_SOP(query)
        elif data['Action']=='UPDATE':
            docno=str(data['CancelDocument'])

        #Tạo đơn hoặc cập nhât đơn đăng ký hủy trên bảng RegisterCancelDocument
        query='''sp_InsertOrUpdateRegisterCancelDocument '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'
                '''.format(docno,data['ApplicationSite'],'',data['ApplicationNo_Code'],
                           data['DocNo_DCC'],data['ReasonOfApplication'],'G01',user,data['Department'],data['Action'])
        QuerySQL_SOP(query)       
        
        
        return JsonResponse({'CancelDocument':docno},status=200)
    except Exception as ex: return JsonResponse({"error":str(ex)},status=400)

          


# #Duyệt đơn đăng ký hủy mã State('A05':,'A15':,'A15':DCC đã ký)
# def DuyetDKHuyMavb(request):
#     try:
#         data=request.GET
#         user=request.user.get_username()               
#         Orders=GetTypeOrdersApprover(data['CancelDocument'])

#         if len(Orders)>0:#Nếu còn người chờ ký trong bảng approval section (C-00010: đã ký,C-00011:từ chối,C-00009: chờ ký)
#             State=Orders[0]['Orders']
#             State=GET_Orders_Appro(State)

#             #Tạo đơn hoặc cập nhât đơn đăng ký hủy trên bảng RegisterCancelDocument
#             query=''' exec sp_AcceptRegisterCodeDocument '{}','{}','{}'
#                     '''.format(data['CancelDocument'],State,user)
#             QuerySQL_SOP(query) 
        
#         return JsonResponse({'returndate':'ok'},status=200)
#     except Exception as ex: return JsonResponse({"error":str(ex)},status=400)


         
        
 
#Hủy bỏ  hoặc duyệt đơn 
# 'Action'=APPRO:thực hiện ký; 
# 'Action'=CANCEL: hủy đơn
def HUY_HOAC_DUYET_DON_BAT_KY(request):
    #try:
        data=request.GET
        data=Convert_QueryDict_ToDict(data)       
        User=request.user.get_username()  
     
        Orders=GetTypeOrdersApprover(data['CodeDocument'])    
        if len(Orders)>0:#Nếu còn người chờ ký trong bảng approval section (C-00010: đã ký,C-00011:từ chối,C-00009: chờ ký)           
            States=Orders[0]['Orders']
            States=GET_Orders_Appro(States)
            # query='''sp_ApproOrCancelApprovalSection1 '{}','{}','{}','{}','{}'
            #         '''.format(data['CodeDocument'],data['Comment'],State,user,data['Action'])
            # sql=QuerySQL2_SOP(query)
            # sql=sp_ApproOrCancelApprovalSection(data['CodeDocument'],data['Comment'],State,user,data['Action'])
            data.update({'States':States,'User':User})
            sql=sp_ApproOrCancelApprovalSection(data)
        return JsonResponse({'returndata':sql},status=200)
    #except Exception as ex: return JsonResponse({"error":str(ex)},status=400)



