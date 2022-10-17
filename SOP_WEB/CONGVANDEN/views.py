from multiprocessing import context
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from USER.decorator import Check_login_byAjax
from API.API_sendMail import SEND_MAIL

from API.API_MSSQL import SelectSQL3_SOP
from API.SOP_DB import Insert_RegisterDocumentArrive,Search_SOP_H,Detail_HOC_H,Create_SectionApproArr,Get_ListApproSection,Get_ListWaiting_ForAppro
from API.SOP_DB import Update_ApproSection,Check_WaitngAppro_TGD,Get_MailSystem,Save_Log_SendMail,Get_Email_From_Employe,Check_Next_Approver,Get_NextApprover
from API.SOP_DB import Get_Application_Document,Get_List_Mail_Send


#Tạo đơn yêu cầu công văn
@Check_login_byAjax
def TaoYeuCauCongVanDen(request):
    #try:
        data=request.GET  
        user=request.user.get_username()     
        #print(data)      
        Sodon=Insert_RegisterDocumentArrive(data,user)
        sql=Create_SectionApproArr(request,Sodon)
        #print(sql)
        mailSystem=Get_MailSystem()
        ApplyMail=Get_Email_From_Employe(user)
        #print(ApplyMail)
        #Gửi mail thông báo tạo đơn thành công cho người làm đơn SEND_MAIL(mailSystem,mailto,mailcc,docno,Who)
        if len(ApplyMail)>0:
            ApplyMail=ApplyMail[0]['Email']
            send=SEND_MAIL(mailSystem,ApplyMail,'',str(Sodon),'Application','','','','')
            Save_Log_SendMail(Sodon,ApplyMail,'',send,'Gửi mail thông báo tạo đơn thành công',user,'Tạo đơn thành công')
        else:  return JsonResponse({"error":"Không tìm thấy mail của người làm đơn ! kiểm tra lại thông tin email "},status=400)
        
        if sql!=False:
            if len(sql)>0:                
                #Gửi mail cho chủ quản phê duyệt
                TGD_Mail=sql[0]['Email']
                send=SEND_MAIL(mailSystem,TGD_Mail,'',str(Sodon),'TGD','','','','')
                Save_Log_SendMail(str(Sodon),TGD_Mail,'',str(send),'Gửi mail báo ký đơn tới chủ quản phê duyệt: '+str(TGD_Mail),str(user),'Thông báo ký đơn')
            else: return JsonResponse({'error':'Lỗi chưa gửi được mail cho chủ quản phê duyệt'},status=400)
        return JsonResponse({'returndata':Sodon},status=200)
    #except Exception as ex: return JsonResponse({"error":str(ex)},status=400)



#Tra cứu công văn đến
@Check_login_byAjax
def TraCuuCongVan(request):
    try:
        data=request.GET
        user=request.user.get_username()
        sql=Search_SOP_H(data)        
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({"error":str(ex)},status=400)



#Lấy danh sách duyệt công văn
@Check_login_byAjax
def DuyetCongVan(request):
    try:            
        sql=Get_ListWaiting_ForAppro(request)
        #print(sql)
        return JsonResponse({'returndata':sql},status=200)
    except Exception as ex: return JsonResponse({"error":str(ex)},status=400)


#Chi tiết công văn
@login_required(login_url='/login/')
def ChiTietCongVan(request):
    #try:
        data=request.GET  
        user=request.user.get_username()
        sql=Detail_HOC_H(data)[0]        
        tbl_appro=Get_ListApproSection(data)
        Donvichusu1=sql['Donvichusu']
        Donvihopban1=sql['Donvihopban']
        Donvichusu=[]
        Donvihopban=[]
        Chondvkhac=''
        Donvikhac='hidden'
        Dongsauhop=''
        
        Traloivanban=''
        Div_traloivb='hidden'
        Tepvbtraloi='hidden'
        btn_upfiletraloi='hidden'
        
        btn_pheduyet='hidden'
        btn_huydon='hidden'
        btn_donviphutrach='hidden'
        
        Show_DivPDF='hidden'
        Show_TepPDF='hidden'
        Check_TGD=Check_WaitngAppro_TGD(request)        
        
        #Kiểm tra xem người ký có đang là người đăng nhập
        NextAppro=Check_Next_Approver(request)
        if len(NextAppro)>0:
            #Kiểm tra xem người ký có phải là TGD không
            btn_pheduyet=''
            btn_huydon=''
            Tepvbtraloi=''
            btn_upfiletraloi=''
            if Check_TGD==True:
                Show_DivPDF=''
                Show_TepPDF=''
            else:
                btn_donviphutrach=''
                Tepvbtraloi=''
                
                
            
        if sql['TepscanPDF']!='': Show_TepPDF=''            
        if sql['Chondvkhac']=='1':
            Chondvkhac='checked'
            Donvikhac=''
        if sql['Dongsauhop']=='1':Dongsauhop='checked'
        if sql['Traloivanban']=='1':
            Traloivanban='checked'
            if sql['file_vbtraloi'] is not None:Tepvbtraloi=''            
            Div_traloivb=''
           

        #print(Donvichusu1)
        if Donvichusu1.replace(' ','')!='':
            Donvichusu1=Donvichusu1.split(',')
            for item in Donvichusu1:
                query="""SELECT CatCode as Department,CatName as Department1 FROM Categorys WHERE CatCode='{}' """.format(item)
                sql1=SelectSQL3_SOP(query)
                Donvichusu.append(sql1[0])
        if Donvihopban1.replace(' ','')!='':
            Donvihopban1=Donvihopban1.split(',')
            for item in Donvihopban1:
                query="""SELECT CatCode as Department,CatName as Department1 FROM Categorys WHERE CatCode='{}' """.format(item)
                sql1=SelectSQL3_SOP(query)
                Donvihopban.append(sql1[0])

        context={'sql':sql,
                 'tbl_appro':tbl_appro,
                'Donvichusu':Donvichusu,
                'Donvihopban':Donvihopban,
                'Chondvkhac':Chondvkhac,
                'Donvikhac':Donvikhac,
                'Dongsauhop':Dongsauhop,
                'Traloivanban':Traloivanban,
                'Tepvbtraloi':Tepvbtraloi,
                'Div_traloivb':Div_traloivb,
                'btn_upfiletraloi':btn_upfiletraloi,
                'Show_DivPDF':Show_DivPDF,
                'Show_TepPDF':Show_TepPDF,
                'btn_pheduyet':btn_pheduyet,
                'btn_huydon':btn_huydon,
                'btn_donviphutrach':btn_donviphutrach
                }
        return render(request,'HOME/chitietdon/congvanden.html',context=context)
    #except Exception as ex: return HttpResponse("error"+str(ex))


#Ký duyệt công văn đến
@Check_login_byAjax
def Approval_Doc(request):
    try:
        user=request.user.get_username()
        #Ký đơn cập nhật chữ ký
        TGD_Check= Check_WaitngAppro_TGD(request)
        sql=Update_ApproSection(request)
        #print(sql)  
        mailSystem=Get_MailSystem()      
        data=request.GET 
       
        Application=Get_Application_Document(data['Sodon'])      
        mail=Get_List_Mail_Send(data)    
        #print(mail)     
        #Kiểm tra có phải giám đốc thì gửi mail cho các bên liên quan
        if TGD_Check:
                      
            if mail!=False:     
                send=SEND_MAIL(mailSystem,str(mail['MailTo']),str(mail['MailCC']),str(data['Sodon']),'Group',data['TenDonvichusu'],data['TenDonvihopban'],data['Donvikhac'],'')
                Save_Log_SendMail(str(data['Sodon']),str(mail['MailTo']),str(mail['MailCC']),str(send),'Gửi mail thông báo thực hiện cho phòng ban',user,'Thông báo phòng ban triển khai')
                       
                
        #Nếu không là giám đốc thì gửi mail cho người ký tiếp theo
        else:     
            NextAppro=Get_NextApprover(data['Sodon'])    
            #Nếu còn người ký thì gửi mail thông báo cho người ký
            if len(NextAppro)>0:
                send=SEND_MAIL(mailSystem,str(NextAppro[0]['Email']),'',str(data['Sodon']),'NextAppro','','','','')
                Save_Log_SendMail(str(data['Sodon']),str(NextAppro[0]['Email']),'',str(send),'Thông báo có đơn ký tới người dùng',user,'Thông báo ký đơn cho : '+NextAppro[0]['Next_appro'])
            else:
            #Nếu hết người ký thì gửi mail thông báo hoàn thành đơn cho người làm đơn
                Application=Get_Application_Document(data['Sodon'])
                send=SEND_MAIL(mailSystem,str(Application[0]['Email']),'',str(data['Sodon']),'Finished','','','','')
                Save_Log_SendMail(str(data['Sodon']),str(Application[0]['Email']),'',str(send),'Thông báo kết thúc đơn !',user,'Thông báo cho người làm đơn: '+str(Application[0]['Nguoitrinhdon']))    
        return JsonResponse({'returndata':'OK'},status=200)
    except Exception as ex: return JsonResponse({"error":str(ex)},status=400)




#In xuất danh sách thông tin các đơn ra file exel
@Check_login_byAjax
def PRINT_EXEL_ALLREPORT(request):
    try:
        data=request.GET
        user=request.user.get_username()       
                
        data1={}
        
        for item in data:
            tam=''
            if len(data[item])<1: tam=' is not null '
            else: tam= " like '%"+data[item]+"%' "

            if item=='CREATE_AT_START': tam=data[item].replace("T"," ")
            if item=='CREATE_AT_END': tam= data[item].replace("T"," ")
            if item=='LEAVE_TIME': tam= data[item].replace("T"," ")
            if item=='ARRIVE_TIME': tam= data[item].replace("T"," ")
            if item=='STATUS_DOC':
                if data[item]=='':tam= "!= 'Waiting'"
            if item=='CAR_NUMCARD':
                if data[item]=='':tam=''
                else:tam=" and [CAR_NUMCARD] LIKE '%"+data[item]+"%' "
            if item=='COST_NO':
                if data[item]=='':tam=''
                else:tam=" and [COST_NO] LIKE '%"+data[item]+"%' "
                
            data1.update({item:tam})

        CREATE_AT=" and ([CREATE_AT] BETWEEN (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 23:59:00')) ".format(data1['CREATE_AT_START'],data1['CREATE_AT_END'])        
        if data1['CREATE_AT_START']=='' and data1['CREATE_AT_END']=='':CREATE_AT=""
        elif data1['CREATE_AT_START']!='' and data1['CREATE_AT_END']=='': CREATE_AT=" and [CREATE_AT] between (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and GETDATE() ".format(data1['CREATE_AT_START'])
        elif data1['CREATE_AT_END']!='' and data1['CREATE_AT_START']=='': CREATE_AT=" and [CREATE_AT] between (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and GETDATE() ".format(data1['CREATE_AT_END'])
       
        WAITING_TIME=" and ([WAITING_TIME] BETWEEN  (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00')) ".format(data1['LEAVE_TIME'],data1['ARRIVE_TIME'])        

        if data1['LEAVE_TIME']=='' and  data1['ARRIVE_TIME']=='':WAITING_TIME=""
        elif data1['LEAVE_TIME']!='' and  data1['ARRIVE_TIME']!='':WAITING_TIME=" and [WAITING_TIME] BETWEEN (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and  ( CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 23:59:00') ".format(data1['LEAVE_TIME'],data1['ARRIVE_TIME'])    
        else:
            if data1['LEAVE_TIME']!='': WAITING_TIME=" and ([WAITING_TIME] BETWEEN  (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and getdate()) ".format(data1['LEAVE_TIME'])    
            if data1['ARRIVE_TIME']!='':  WAITING_TIME=" and ([WAITING_TIME] BETWEEN  (CONVERT(VARCHAR(19),CAST('{}' as date), 120)+' 00:00:00') and getdate()) ".format(data1['ARRIVE_TIME'])    


        query='''    select d.[DOC_NO],d.LEAVE_TIME,d.ARRIVE_TIME,t.[DATACODE_CN] as TYPE_USECAR,d.APPLY_EMPNO,u.UserName,d.PERSON_USECAR,d.CREATE_AT, STATUS_DOC
                        from [DOC_DETAIL] as d '''+'''
                        LEFT JOIN [Users] as u ON d.APPLY_EMPNO=u.UserID 
                        LEFT JOIN [DOC_TYPEDATA] as t ON d.[TYPE_USECAR]=t.[DATATYPE] AND t.[DATA_TYPE]='TYPE_USECAR'
                        WHERE [STATUS_DOC] {}
                        '''.format(data1['STATUS_DOC'])+CREATE_AT+'''
                        '''+WAITING_TIME+'''
                        {}
                        and [APPLY_EMPNO] {}
                        {} order by [CREATE_AT] desc
                '''.format(data1['CAR_NUMCARD'],data1['APPLY_EMPNO'].upper(),data1['COST_NO'].upper())
        sql=SelectSQL3_DIEUXE(query)#Lấy thông tin đơn chi tiết
        
        DOC_NO=''
        for item in sql:
            DOC_NO+="'"+item["DOC_NO"]+"',"
            
        
        query='''
        select [DOC_NO],t1.[DATACODE_CN] as [CAR_TYPE],[LEAVE_TIME],[ARRIVE_TIME],[LEAVE_LOCAL],
        [ARRIVE_LOCAL],t.[DATACODE_CN] as [TYPE_USECAR],[UserName],t2.DATACODE_CN as [ROUTE],t3.[DATACODE_CN] as [STATUS_DOC]
            FROM [DOC_DETAIL] as d
            LEFT JOIN [Users] as u ON d.[APPLY_EMPNO]=u.[UserID]
            LEFT JOIN [DOC_TYPEDATA] as t ON d.[TYPE_USECAR]=t.[DATATYPE] AND t.[DATA_TYPE]='TYPE_USECAR'
            LEFT JOIN [DOC_TYPEDATA] as t1 ON d.[CAR_TYPE]=t1.[DATATYPE] AND t1.[DATA_TYPE]='CAR_TYPE'
            LEFT JOIN [DOC_TYPEDATA] as t2 ON d.[ROUTE]=t2.[DATATYPE] AND t2.[DATA_TYPE]='ROUTE'
            LEFT JOIN [DOC_TYPEDATA] as t3 ON d.[STATUS_DOC]=t3.[DATATYPE] AND t3.[DATA_TYPE]='STATUS'
            WHERE d.[DOC_NO] in ({})'''.format(DOC_NO)
        
        # print(query)       
        sql=SelectSQL3_DIEUXE(query)
        print(sql)
        DOC_NO=data['DOC_NO'][0:-1].split(',')
        sql2=[]
        sql4=[]
        arrLength=[]
        arrLength1=[]
        for item in DOC_NO:
            query2='''SELECT [PASSENGER],[CODE_NO],[NUM_PEOPLE],[MOBILE] FROM [DOC_PEOPLE] WHERE [DOC_NO]={} '''.format(item)
            sql3=SelectSQL3_DIEUXE(query2)
            sql2+=sql3
            arrLength.append(len(sql3))
            
            query='''SELECT [CARNUM],[KILOMET],[OVERTIME] FROM [CAR_KM_LOG] WHERE [DOC_NO]={} '''.format(item)
            sql3=SelectSQL3_DIEUXE(query)
            sql4+=sql3
            arrLength1.append(len(sql3))
        # print(arrLength)

       
        
        WRITE_ALL_DATA_PRINT_EXEL(sql,arrLength,sql2,arrLength1,sql4,user)
        response=download_exel(user+'_Detail_bus.xlsx')
        return response
        return JsonResponse({'datareturn':''},status=200)
    except Exception as ex: return JsonResponse({'error':str(ex)},status=400)
