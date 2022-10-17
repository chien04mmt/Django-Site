
import xlsxwriter,pandas as pd,json
from artice_car.settings import MEDIA_ROOT

#_-------------------------------------------------------------------------------------------------------------------
#In bản ra file exel
def WRITE_EXEL_(sql,namefile,list_columes,title_table):  
    link_file=MEDIA_ROOT+ '/'+namefile    
    wb=xlsxwriter.Workbook(link_file)
    ws=wb.add_worksheet()

    #tăng kích thước column cell của  cell 
    ws.set_column('A:K',13)

    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,30)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp n cell
    ws.merge_range(0,0,0,len(list_columes)-1,title_table,merge_format)
    col=0
    row=1       
    for item in list_columes:
        ws.write(row, col, item,merge_format1)  # Writes a string for columes
        col+=1

    for item in sql:#in ra danh sách người đi xe
        row=row+1
        col=0        
        for ite in list_columes:
            ws.write(row, col,str(item[ite]),merge_format1)        
            col=col+1      
    wb.close()
    return '/static/media/'+namefile





#----------------------------------------------------------------------------------------------------------------------

#In bản ra file exel quyền server
def WRITE_EXEL_SERVERROOM(sql,user):
    namefile=user+'_Table_Server.xlsx'
    wb=xlsxwriter.Workbook(MEDIA_ROOT+ '/'+namefile)
    ws=wb.add_worksheet()

    #tăng kích thước column cell của  cell 
    ws.set_column('A:K',13)

    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,30)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp 3 cell
    ws.merge_range(0,0,0,10,'BẢNG TỔNG HỢP THÔNG TIN',merge_format)
    
    #Ghi dữ liệu wirte(dòng+1,cột, dữ liệu)
    ws.write(1, 0, 'Mã thẻ',merge_format1)  # Writes a string
    ws.write(1, 1, 'Tên tiếng Trung',merge_format1)  # Writes a string
    ws.write(1, 2, 'Tên tiếng Việt',merge_format1)  # Writes a string
    ws.write(1, 3, 'Phòng ban',merge_format1)  # Writes a string
    ws.write(1, 4, 'Nhà máy',merge_format1)  # Writes a string
    ws.write(1, 5, 'Ghi chú',merge_format1)  # Writes a string
    ws.write(1, 6, 'Thời gian',merge_format1)  # Writes a string
    ws.write(1, 7, 'Người tạo',merge_format1)  # Writes a string
   

    row=1
    col=0
      
    for item in sql:#in ra danh sách người đi xe
        row=row+1
        col=0
        
        for n in range(8):
            if col==0:ws.write(row, col,str(item['emp_no']),merge_format1)
            if col==1:ws.write(row, col,str(item['cname']),merge_format1) 
            if col==2:ws.write(row, col,str(item['yname']),merge_format1) 
            if col==3:ws.write(row, col,str(item['deptname']),merge_format1) 
            if col==4:ws.write(row, col,str(item['FACTORYCODE']),merge_format1) 
            if col==5:ws.write(row, col,str(item['FREMARK']),merge_format1) 
            if col==6:ws.write(row, col,str(item['FBDATE']),merge_format1) 
            if col==7:ws.write(row, col,str(item['CreatedBy']),merge_format1)             
            col=col+1      
    wb.close()
    return namefile


#In bản ra file exel log vào ra phòng server
def WRITE_EXEL_LOG_INOUT_SERVER(sql,user):
    namefile=user+'_Table_Server.xlsx'
    wb=xlsxwriter.Workbook(MEDIA_ROOT+ '/'+namefile)
    ws=wb.add_worksheet()

    #tăng kích thước column cell của  cell 
    ws.set_column('A:K',13)

    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,30)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp 3 cell
    ws.merge_range(0,0,0,10,'BẢNG TỔNG HỢP THÔNG TIN',merge_format)
    
    #Ghi dữ liệu wirte(dòng+1,cột, dữ liệu)
    ws.write(1, 0, 'Mã thẻ',merge_format1)  # Writes a string
    ws.write(1, 1, 'Tên tiếng Trung',merge_format1)  # Writes a string
    ws.write(1, 2, 'Tên tiếng Việt',merge_format1)  # Writes a string
    ws.write(1, 3, 'Phòng ban',merge_format1)  # Writes a string
    ws.write(1, 4, 'Nhà máy',merge_format1)  # Writes a string
    ws.write(1, 5, 'Ghi chú',merge_format1)  # Writes a string
    ws.write(1, 6, 'Thời gian',merge_format1)  # Writes a string
    ws.write(1, 7, 'Người tạo',merge_format1)  # Writes a string
   

    row=1
    col=0
      
    for item in sql:#in ra danh sách người đi xe
        row=row+1
        col=0
        
        for n in range(8):
            if col==0:ws.write(row, col,str(item['emp_no']),merge_format1)
            if col==1:ws.write(row, col,str(item['cname']),merge_format1) 
            if col==2:ws.write(row, col,str(item['yname']),merge_format1) 
            if col==3:ws.write(row, col,str(item['deptname']),merge_format1) 
            if col==4:ws.write(row, col,str(item['FACTORYCODE']),merge_format1) 
            if col==5:ws.write(row, col,str(item['FREMARK']),merge_format1) 
            if col==6:ws.write(row, col,str(item['FBDATE']),merge_format1) 
            if col==7:ws.write(row, col,str(item['CreatedBy']),merge_format1)             
            col=col+1      
    wb.close()
    return namefile





#Ghi dữ liệu nhiều đơn cho file mẫu
def WRITE_ALL_DATA_PRINT_EXEL(sql,arrLength,sql2,arrLength1,sql3,user):
    wb=xlsxwriter.Workbook(MEDIA_ROOT+ '/'+user+'_Detail_bus.xlsx')
    ws=wb.add_worksheet()

    #tăng kích thước column cell của  cell 
    ws.set_column('A:Q',13)

    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,30)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp cell theo chiều ngang
    ws.merge_range(0,0,0,16,'越南車調用車情況匯總表 Bảng tổng hợp tình hình gọi xe tại Việt Nam',merge_format)
    
    #Ghi dữ liệu wirte(dòng+1,cột, dữ liệu)
    ws.write(1, 0, '單號 Đơn số',merge_format1)  # Writes a string
    ws.write(1, 1, '用車類型 Loại xe ôtô',merge_format1)  # Writes a string
    ws.write(1, 2, '用車開始時間 Thời gian bắt đầu',merge_format1)  # Writes a string
    ws.write(1, 3, '用車結束時間 Thời gian kết thúc',merge_format1)  # Writes a string
    ws.write(1, 4, '出發地點 Điểm khởi đầu',merge_format1)  # Writes a string
    ws.write(1, 5, '候車地點 Điểm đến',merge_format1)  # Writes a string
    ws.write(1, 6, '派車類型 Loại hình dùng xe',merge_format1)  # Writes a string
    ws.write(1, 7, '申請人姓名 Người nộp đơn',merge_format1)  # Writes a string
    ws.write(1, 8, '行車路線 Lộ trình',merge_format1)  # Writes a string
    ws.write(1, 9, '審核狀態 Tình trạng đơn',merge_format1)  # Writes a string
    
    ws.write(1, 10, '車牌號 Biển số',merge_format1)  # Writes a string
    ws.write(1, 11, '公里數 Kilomet',merge_format1)  # Writes a string
    ws.write(1, 12, '加班時間 Tăng ca',merge_format1)  # Writes a string

    ws.write(1, 13, '乘車人姓名 Tên hành khách',merge_format1)  # Writes a string
    ws.write(1, 14, '費用代碼 Mã chi phí',merge_format1)  # Writes a string
    ws.write(1, 15, '乘車人數 Lượng hành khách',merge_format1)  # Writes a string
    ws.write(1, 16, '乘車人電話 Điện thoại khách',merge_format1)  # Writes a string

    row=1
    col=0
    for item in sql2:#in ra danh sách người đi xe
        row=row+1
        col=13
        for ite in item:
            if item[ite] is None: item[ite]=''
            ws.write(row, col,str(item[ite]),merge_format1)
            col=col+1            

    row=2
    index=0
    rowx=row
    for item in sql:#in ra thông tin đơn        
        while row<rowx+arrLength[index]:
            col=0
            for ite in item:           
                if item[ite] is None: item[ite]=''
                # print(item[ite])
                ws.write(row,col, str(item[ite]),merge_format1)               
                col=col+1
            row+=1
        rowx=rowx+arrLength[index]
        index+=1
            
    # for item in sql:#in ra thông tin đơn
    #     col=0
    #     # for ite,val in enumerate(item):
    #     #     print(ite,val)

    #     for ite in item:
    #         while row<row+arrLength[index]
    #         if item[ite] is None: item[ite]=''
    #         # print(item[ite])
    #         if arrLength[index]==1:ws.write(row,col, str(item[ite]),merge_format1)
    #         else:ws.merge_range(row,col,row+arrLength[index]-1,col,str(item[ite]),merge_format1)
    #         col=col+1
    #     row+=1
    #     rowx+=1
    #     row=row+arrLength[index]
    #     index+=1


    row=2
    index=0#chỉ số của arr
    index1=0#chỉ số giá trị tăng của row

    iter1= (sql3)
    for i in arrLength1: 
        if index1-i==0:
            row+=arrLength[index]-index1
            index+=1   
            index1=0
        else:            
            for item in iter1:
                col=10              
                for ite in item:                   
                    if item[ite] is None: item[ite]=''
                    ws.write(row,col, str(item[ite]),merge_format1)                
                    col=col+1
                iter1.remove(item)
                row+=1
                index1+=1
                if index1-i==0:
                    row+=arrLength[index]-index1
                    index+=1   
                    index1=0
                    break
    wb.close()



#Ghi dữ liệu thống kê đi chung xe
def WRITE_THONGKE_BIENSO_EXEL(sql,user,date,CARNUM):
    wb=xlsxwriter.Workbook(MEDIA_ROOT+ '/'+user+'_THONGKE_BIENSO.xlsx')
    ws=wb.add_worksheet()

    #tăng kích thước chiều rộng column
    ws.set_column('B:B',14)
    ws.set_column('G:G',14)
    ws.set_column('H:H',14)
    
    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,30)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp cell theo chiều ngang
    ws.merge_range(0,0,0,11,'車輛使用量簡表 Bảng tóm tắt về việc sử dụng xe',merge_format)
    
    #Ghi dữ liệu wirte(dòng+1,cột, dữ liệu)
    ws.write(1,0,"時間(Thời gian): "+date)
    ws.write(2,0,"車牌(Biển số):"+CARNUM)
    
    ws.write(3, 0, '訊號 STT',merge_format1)  # Writes a string
    ws.write(3, 1, '單號 Số đơn',merge_format1)  # Writes a string
    ws.write(3, 2, '部門 Phòng ban',merge_format1)  # Writes a string
    ws.write(3, 3, '費用代碼 Mã chi phí',merge_format1)  # Writes a string
    ws.write(3, 4, '用車日期 Ngày sử dụng',merge_format1)  # Writes a string
    ws.write(3, 5, '路程 Hành trình',merge_format1)  # Writes a string
    ws.write(3, 6, '出發時間 Thời gian khởi hành',merge_format1)  # Writes a string
    ws.write(3, 7, '結束時間 Thời gian kết thúc',merge_format1)  # Writes a string
    ws.write(3, 8, '車牌 Biển số',merge_format1)  # Writes a string
    ws.write(3, 9, '加班時間 Tăng ca',merge_format1)  # Writes a string
    ws.write(3, 10, '公里數 Số km',merge_format1)  # Writes a string
    ws.write(3, 11, '出行次数 Số chuyến',merge_format1)  # Writes a string
    
    row=4
    col=0
    for item in sql:#in ra danh sách xe đi chung        
        col=0
        for ite in item:
            if item[ite] is None: item[ite]=''
            ws.write(row, col,str(item[ite]),merge_format1)            
            col=col+1
        row=row+1
    wb.close()


#Ghi dữ liệu thống kê đi chung xe
def WRITE_THONGKE_DICHUNG_EXEL(sql,user,date):
    wb=xlsxwriter.Workbook(MEDIA_ROOT+ '/'+user+'_THONGKE_DICHUNG.xlsx')
    ws=wb.add_worksheet()

    #tăng kích thước chiều rộng column
    ws.set_column('B:H',14)
    ws.set_column('D:D',40)
    
    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,30)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp cell theo chiều ngang
    ws.merge_range(0,0,0,8,'拼車統計表 Thống kê đi chung xe',merge_format)
    
    #Ghi dữ liệu wirte(dòng+1,cột, dữ liệu)
    ws.write(1,0,"時間Thời gian : "+date)
    
    ws.write(2, 0, '訊號 STT',merge_format1)  # Writes a string
    ws.write(2, 1, '單號 Số đơn',merge_format1)  # Writes a string
    ws.write(2, 2, '出發時間 Thời gian khởi hành',merge_format1)  # Writes a string
    ws.write(2, 3, '候車地點 Nời chờ xe',merge_format1)  # Writes a string
    ws.write(2, 4, '加班時間 Tăng ca',merge_format1)  # Writes a string
    ws.write(2, 5, '車牌號 Biển xe',merge_format1)  # Writes a string
    ws.write(2, 6, '公里數 Số km',merge_format1)  # Writes a string
    ws.write(2, 7, '拼車 Đi chung xe',merge_format1)  # Writes a string
    ws.write(2, 8, '出行次数 Số chuyến',merge_format1)  # Writes a string
    
    row=3
    col=0
    for item in sql:#in ra danh sách xe đi chung        
        col=0
        for ite in item:
            if item[ite] is None: item[ite]=''
            ws.write(row, col,str(item[ite]),merge_format1)            
            col=col+1
        row=row+1
    wb.close()


#Ghi dữ liệu thống kê đi chung xe
def WRITE_THONGKE_THEONAM_EXEL(sql,user,year):
    wb=xlsxwriter.Workbook(MEDIA_ROOT+ '/'+user+'_THONGKE_THEONAM.xlsx')
    ws=wb.add_worksheet()

    #tăng kích thước chiều rộng column
    ws.set_column('A:M',14)
    ws.set_column('A:A',40)
    
    #tăng kích thước chiều rộng của cell thứ i+1 worksheet.set_row(i,size)
    ws.set_row(0,33)

    #tạo một định dạng sử dụng merged range
    merge_format= wb.add_format({
        'bold':1,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 15,
        'fg_color':'yellow'
    })
    merge_format1= wb.add_format({
        'bold':0,
        'border':1,
        'align':'center',
        'valign':'vcenter',
        'font_name': 'Calibri',
        'font_size': 8
    })
    merge_format1.set_text_wrap()

    #gộp cell theo chiều ngang
    ws.merge_range(0,0,0,12,'車輛使用量匯總表 Tóm tắt tình hình sử dụng xe',merge_format)
    
    #Ghi dữ liệu wirte(dòng+1,cột, dữ liệu)
    ws.write(1,0,"年份(năm):"+year)
    # ws.write(2, 0, '年份(năm):'+year,merge_format1)  # Writes a string
    
    ws.write(2, 0, '類型 Loại hình',merge_format1)  # Writes a string
    ws.write(2, 1, '一月',merge_format1)  # Writes a string
    ws.write(2, 2, '二月',merge_format1)  # Writes a string
    ws.write(2, 3, '三月',merge_format1)  # Writes a string
    ws.write(2, 4, '四月',merge_format1)  # Writes a string
    ws.write(2, 5, '五月',merge_format1)  # Writes a string
    ws.write(2, 6, '六月',merge_format1)  # Writes a string
    ws.write(2, 7, '七月',merge_format1)  # Writes a string
    ws.write(2, 8, '八月',merge_format1)  # Writes a string
    ws.write(2, 9, '九月',merge_format1)  # Writes a string
    ws.write(2, 10, '十月',merge_format1)  # Writes a string
    ws.write(2, 11, '十一月',merge_format1)  # Writes a string
    ws.write(2, 12, '十二月',merge_format1)  # Writes a string
    
    ws.write(3, 0, '值班車 xe trực ban',merge_format1)  # Writes a string
    ws.write(4, 0, '固定接送主管 Cố định đưa đón chủ quản',merge_format1)  # Writes a string
    ws.write(5, 0, '固定班車Xe cố định',merge_format1)  # Writes a string
    ws.write(6, 0, '固定送飯 Cố định đưa cơm',merge_format1)  # Writes a string
    ws.write(7, 0, '接送友誼關 Đưa đón Hữu Nghị Quan',merge_format1)  # Writes a string
    ws.write(8, 0, '接送員工上下班 Đưa đón nhân viên đi làm và tan ca',merge_format1)  # Writes a string
    ws.write(9, 0, '接送客戶 Đưa đón khách hàng',merge_format1)  # Writes a string
    ws.write(10, 0, '接送機場 Đưa đón sân bay',merge_format1)  # Writes a string
    ws.write(11, 0, '臨時派車 điều xe lẻ',merge_format1)  # Writes a string
  
    col=1
    for item in sql:#in ra danh thông tin số lượng chuyến hàng tháng của năm     
        row=3
        for ite in item:
            if item[ite] is None: item[ite]=''
            ws.write(row, col,str(item[ite]),merge_format1)   
            row=row+1         
        col=col+1    
        
    wb.close()


