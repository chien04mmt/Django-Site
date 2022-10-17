
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from API.API_MSSQL import QuerySQL_SOP,SelectSQL3_SOP,QuerySQL2_SOP
from API.SOP_DB import *


# Create your views here.


    
#Load danh sách các phòng ban
def Load_Department(request):
    try:
        sql=Get_Department(request.user.get_username())
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    
    
    
#------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------TÌM KIẾM ĐƠN----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------
	# @Department as nvarchar(10),
	# @CodeDocument nvarchar(50),
	# @DocumentNo nvarchar(50),
	# @CheckWait nvarchar(50),
	# @Code_Name nvarchar(50),
	# @CreatedBy nvarchar(50),
	# @ToDate datetime,
	# @FromDate datetime
#tra cứu trình ký
def TraCuuTrinhKy(request):
    try:
        data=request.GET
        user=request.user.get_username()
        CheckWait=data['CheckWait']
        if data['CheckWait']!='':CheckWait =user
        
        # query='''exec sp_ListCheckWait '{}','{}','{}','{}','{}','{}','{}','{}' 
        #         '''.format(data['Code'],data['Dcc'],CheckWait,CheckWait,
        #             data['CreatedBy'],data['FromDate'],data['ToDate'],data['Type'])
        # print(query) 
        # sql=SelectSQL3_SOP(query)
        #print(CheckWait)
        user=request.user.get_username()        
        dept=SELECT_TABLE('[UserInDepartment]','[UserName]',user.strip())
        dept=dept[0]['Department']
        if len(dept)>0:
            query='''EXEC sp_GetListCheckWait1 '{}','{}','{}','{}','{}','{}','{}','{}'
             '''.format('',data['CodeDocument'],data['DocumentNo'],CheckWait,
                            data['Code_Name'],data['CreatedBy'],data['ToDate'],data['FromDate'])
            #print(query)
            sql=SelectSQL3_SOP(query)
            return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    

#tra cứu danh sách mã văn bản
def TraCuuDSMaVB(request):
    try:
        data=request.GET
        user=request.user.get_username()
        # query='''exec sp_ListRegisterCodeDocument '{}','{}','{}','{}','{}',
        #                                           '{}','{}','{}','{}','{}' 
        # '''.format(data['CodeDocument'],data['CreatedBy'],'','','',
        #         data['Department'],data['DocNo'],data['DocName'],data['FromApplicationDate'],data['ToApplicationDate'])
        query='''exec sp_ListRegisterCodeDocument '{}','{}','{}','{}','{}',
                                                  '{}','{}','{}','{}','{}' 
        '''.format(data['CodeDocument'],data['CreatedBy'],'','','',
                data['Department'],data['DocNo'],data['DocName'],data['FromApplicationDate'],data['ToApplicationDate'])
        #query="exec sp_ListRegisterCodeDocument '','王氏香','','','','','02','','2017-10-07','' "
        # print(query)
        
        sql=SelectSQL3_SOP(query)
        # print(sql)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    
#tra cứu danh sách hủy mã văn bản
def TraCuuDSHuyMaVB(request):
    try:
        data=request.GET
        user=request.user.get_username()
        # query='''exec sp_ListRegisterCancelDocument '{}','{}','{}','{}','{}',
        #                                             '{}','{}','{}','{}','{}'
        # '''.format(data['CancelDocument'],data['DocNo_DCC'],data['DocName'],
        #            data['CreatedBy'],'','','',data['Department'],
        #            data['FromApplicationDate'],data['ToApplicationDate'])
        query='''exec sp_ListRegisterCancelDocument '{}','{}','{}','{}','{}',
                                                    '{}','{}','{}','{}','{}'
        '''.format(data['CodeDocument'],data['DocNo'],data['DocName'],
                   data['CreatedBy'],'','','',data['Department'],
                   data['FromApplicationDate'],data['ToApplicationDate'])

        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    

#tra cứu danh sách phế bỏ văn bản
def TraCuuDSPheBoVB(request):
    try:
        data=request.GET
        user=request.user.get_username()
        # query='''exec sp_ListApplicationObsoletedDocument '{}','{}','{}','{}','{}',
        #                                                   '{}','{}','{}','{}'
        # '''.format(data['ObsoletedDocument'],data['CreatedBy'],'','',data['DocNo'],
        #            data['DocName'],data['Department'],data['FromApplicationDate'],data['ToApplicationDate'])
        query='''exec sp_ListApplicationObsoletedDocument '{}','{}','{}','{}','{}',
                                                          '{}','{}','{}','{}'
        '''.format(data['CodeDocument'],data['CreatedBy'],'','',data['DocNo'],
                   data['DocName'],data['Department'],data['FromApplicationDate'],data['ToApplicationDate'])
        #print(query)
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    

#tra cứu danh sách phát hành văn bản
def TraCuuDSPhatHanhVB(request):
    try:
        data=request.GET
        user=request.user.get_username()
        # query='''exec sp_ListRegisterPublishDocument '{}','{}','{}','{}','{}',
        #                                              '{}','{}','{}','{}','{}' 
        #         '''.format(data['PublishDocument'],data['CreatedBy'],'','',data['DocumentNo'],
        #                    data['DocumentName'],'',data['Department'],data['FromApplicationDate'],data['ToApplicationDate'])     
        query='''exec sp_ListRegisterPublishDocument '{}','{}','{}','{}','{}',
                                                     '{}','{}','{}','{}','{}' 
                '''.format(data['CodeDocument'],data['CreatedBy'],'','',data['DocNo'],
                           data['DocName'],'',data['Department'],data['FromApplicationDate'],data['ToApplicationDate'])     
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
    
    
    
#tra cứu danh sách Sửa đổi văn bản
def TraCuuDSSuaDoiVB(request):
    try:
        data=request.GET
        user=request.user.get_username()
        # query='''exec sp_ListRegisterEditDocument '{}','{}','{}','{}','{}',
        #                                              '{}','{}','{}','{}','{}'
        #         '''.format(data['EditDocument'],data['CreatedBy'],'','',data['DocumentNo'],
        #                    data['DocumentName'],'',data['Department'],data['FromApplicationDate'],data['ToApplicationDate'])     
        query='''exec sp_ListRegisterEditDocument '{}','{}','{}','{}','{}',
                                                     '{}','{}','{}','{}','{}'
                '''.format(data['CodeDocument'],data['CreatedBy'],'','',data['DocNo'],
                           data['DocName'],'',data['Department'],data['FromApplicationDate'],data['ToApplicationDate'])     
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
   
  
    
#TÌm kiếm Phụ lục đính kèm
def TimKiemPhuLuc(request):
    try:
        data=request.GET
        user=request.user.get_username()
        query='''exec sp_ListPublishReff '{}','{}','{}','{}','{}',
                                         '{}','{}'
                '''.format('',data['FormNo'],data['FormName'],
                           data['Department'],'C26',data['FromApplicationDate'],data['ToApplicationDate'])     
        sql=SelectSQL3_SOP(query)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)



          
#-----------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------
#-------------------------------------CHI TIẾT ĐƠN----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#XEM CHI TIẾT ĐƠN CHO MỖI LOẠI ĐƠN
def XEM_CHI_TIET_MOI_LOAI_DON(request):
    try:
        data=request.GET
        user=request.user.get_username()
        CodeDocument=data['CodeDocument']
        IsDCC='hidden'
        
        link_file=''
        if 'SOP-A' in CodeDocument:
            sql=Detail_CodeDocument('RegisterCodeDocument','CodeDocument',CodeDocument)
            link_file='HOME/chitietdon/donxinmavb.html'
          
        if 'SOP-B' in CodeDocument:
            sql=Detail_CodeDocument('RegisterEditDocument','EditDocument',CodeDocument)
            link_file='HOME/chitietdon/donxinsuavb.html'
        if 'SOP-C' in CodeDocument:
            sql=Detail_CodeDocument('RegisterPublishDocument','PublishDocument',CodeDocument)
            link_file='HOME/chitietdon/donxinphathanhvb.html'
        if 'SOP-D' in CodeDocument:
           sql=Detail_CodeDocument('ApplicationObsoletedDocument','ObsoletedDocument',CodeDocument)
           link_file='HOME/chitietdon/donxinphebovb.html'
        if 'SOP-G' in CodeDocument:
           sql=Detail_CodeDocument('RegisterCancelDocument','CancelDocument',CodeDocument)
           link_file='HOME/chitietdon/donxinhuymavb.html'

        
        list_appro=ListApprovalSection(CodeDocument)
        list_docref=ListDocRef(CodeDocument)

        btn_update='hidden'    
        btn_appro='hidden'
        btn_cancel='hidden'
        btn_other=''
        NextAppro=Get_waiting_approver(CodeDocument)
        Applicant=Get_Applicant(CodeDocument)
        
        if len(NextAppro)>0: 
            NextAppro=NextAppro[0]['UserName']#Nếu người ký tiếp theo là người đang đăng nhập thì cho ký
            if request.user.get_username()==NextAppro.strip():                                
                btn_appro=''
                btn_cancel=''
                if len(Applicant)>0:
                    Applicant=Applicant[0]['UserName']
                    if NextAppro.strip()==Applicant.strip():#Nếu người ký là người làm đơn cho phép cập nhật đơn
                        btn_update=''
                        btn_other='hidden'     
                if Check_IsDCC(user):IsDCC=''
                    
        if len(sql)>0:
            sql=sql[0]
            if sql['States']=='A20':
                btn_update='hidden'    
                btn_appro='hidden'
                btn_cancel='hidden'
                btn_other=''
        #print(sql)       
        return render(request,link_file,context={'sql':sql,"list_appro":list_appro,"list_docref":list_docref,'IsDCC':IsDCC,
                    'btn_update':btn_update,'btn_appro':btn_appro,'btn_cancel':btn_cancel,'btn_other':btn_other})
    except Exception as ex: return HttpResponse(str(ex))
    
    





