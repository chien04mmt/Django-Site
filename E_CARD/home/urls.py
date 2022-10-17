

from django.urls import path
from .views import SHOW_ICON_USER, TRA_CUU,TRA_CUU_LICHSU,THEM_XOA_QUYEN,TRA_CUU_QUYEN_PHONG_MAY,DELETE_PERSON_ROOM,ADD_PERSON_ROOM
from .views import get_homeindex,CHANGE_LANGUAGE,GET_LANGUAGE,Manual_Show
from .views import TRA_CUU,THEM_XOA_USER,ACTION_Permission,ACTION_Menus,ACTION_Modules,PRINT_EXEL_PERMISS_SERVER,PRINT_EXEL_LOG_INOUT_SERVER,PRINT_EXEL_LOG_ACTION_SERVER
from .views import QUANLY_TAIKHOAN,THONGTIN_CANHAN,QUANLY_NHOMQUYENHAN
from .views import DOWNLOAD_TEMPLATE_PERSON,UPLOAD_EXEL
from .views import TIM_TAIKHOAN,SaveProfile_UserManager,ShowSearchInfo,ShowModifyProfile_User,SAVE_PERMISSION,GET_INFO_PERMISSION,SHOW_PERMISSION
from .views import PRINT_EXEL_MAUDON,PRINT_EXEL_REPORT,PRINT_EXEL_ALLREPORT

from .views import WEB_LOG_DI_LAI,TRACUU_LOG_DI_LAI  #Nhật ký phòng server




urlpatterns = [   
    
    #Truy cập trang chủ
    path("home/",get_homeindex, name="home"),#Homepage index    

#------------------------------QUẢN LÝ PHÒNG MÁY CHỦ--------------------------------------------------------------------------------

    path("tracuu/",TRA_CUU, name="tracuu"),#Danh sách đơn đã yêu cầu điều xe chờ ký
    path("themxoa/",THEM_XOA_USER, name="themxoa"),#Danh sách đơn đã hoàn thành
    path("tracuulichsu/",TRA_CUU_LICHSU),#thực hiện tra cứu 
    path("thuchienthemxoa/",THEM_XOA_QUYEN),#Thực hiện thêm xóa thông tin
    path("tracuuquyenphongmay/",TRA_CUU_QUYEN_PHONG_MAY),#Thực hiện tra cứu người có quyền trong phòng máy
    
    path("downloadtemplateimport/",DOWNLOAD_TEMPLATE_PERSON, name="downloadtemplateimport"),#Tải file template import ds người cấp quyền vào phòng máy
    path("uploadexel/",UPLOAD_EXEL, name="uploadexel"),#đăng file exel   thêm nhiều người vào phòng máy chủ

    path("print_exel_permiss_server/",PRINT_EXEL_PERMISS_SERVER),#Xuất file exel quyền ra vào phòng máy chủ
    path("print_exel_inout_server/",PRINT_EXEL_LOG_INOUT_SERVER),#Xuất file exel log vào ra phòng máy
    path("print_exel_action_server/",PRINT_EXEL_LOG_ACTION_SERVER),#Xuất file exel log thao tác phòng máy
     
    path("delete_person/",DELETE_PERSON_ROOM),#Thực hiệnxóa 1 người trong phòng máy
    path("add_person/",ADD_PERSON_ROOM),#Thêm 1 người vào cơ sở phòng máy
    
    path("Web_In_Out_SVR/",WEB_LOG_DI_LAI),#trang tra cứu nhật ký vào ra phòng máy chủ
    path("log_In_Out_SVR/",TRACUU_LOG_DI_LAI,name="log_In_Out_SVR"),#thao tác tra cứu
   
#----------------------------------------------------------------------------------------------------------------------------------







#------------------------------QUẢN LÝ HỆ THÔNG------------------------------------------------------------------------------------


#------------------------------Quản lý tài khoản----------------------------------------------------------------------------------
    
    path("quanlytaikhoan/",QUANLY_TAIKHOAN, name="quanlytaikhoan"), #Quản lý tài khoản
    path("nhomquyenhan/",QUANLY_NHOMQUYENHAN, name="nhomquyenhan"), #Quản lý nhóm quyền hạn
    path("search_acount/",TIM_TAIKHOAN, name="search_acount"), #Tìm kiếm tài khoản bằng mã thẻ
    path("delete_acount/",QUANLY_TAIKHOAN, name="delete_acount"), #Hủy bỏ quyền người dùng trong hệ thống xe bus
    path("showsearchinfo/",ShowSearchInfo,name='showsearchinfo'),
    path("save_permiss/",SAVE_PERMISSION),#Lưu quyền hạn tài khoản người dùng
    path("getInfo_permiss/",GET_INFO_PERMISSION),#lấy thông tin quyền hạn tài khoản
    path("show_permission/",SHOW_PERMISSION),#lấy danh sách các module quyền hạn cho phép
      
      
      
      
#------------------------------Quản lý nhóm phân quyền---------------------------------------------------------------   
path("action_groups_permiss/",ACTION_Permission),#Thêm,sửa xóa nhóm quyền hạn 
    
    
    
    
    
#------------------------------Quản lý nhóm Menu---------------------------------------------------------------   
path("action_Menus/",ACTION_Menus),#Thêm,sửa xóa nhóm menus





#------------------------------Quản lý phân quyền với modules---------------------------------------------------------------   
path("action_Modules/",ACTION_Modules),#Thêm,sửa xóa phân quyền hạn modules


    
    
    
#------------------------------Quản lý thông tin cá nhân---------------------------------------------------------------
    path("thongtincuatoi/",THONGTIN_CANHAN, name="thongtincuatoi"), #Thay đổi thông tin cá nhân
    path("show_icon_user/",SHOW_ICON_USER,name='show_icon_user'),#Hiển thị ảnh cá nhân và tên
    path("change_lang/",CHANGE_LANGUAGE,name='change_lang'),#Đổi ngôn ngữ
    path("get_lang/",GET_LANGUAGE,name='get_lang'),#Lấy thông tin ngôn ngữ trong db
    path("saveprofile_user/",SaveProfile_UserManager,name='saveprofile_user'),
    path("showprofile_user/",ShowModifyProfile_User,name='showprofileuser'),

        
#----------------------------------------------------------------------------------------------------------------------------------









#------------------------------DỮ LIỆU HOẠT ĐỘNG-----------------------------------------------------------------------------------


#------------------------------Xuất đơn đăng ký cấp xe------------------------------------------------------------------
    path("print_allreport_exel/",PRINT_EXEL_ALLREPORT, name="print_allreport_exel"),#In toàn bộ thông tin danh sách đơn ra file exel
    path("print_doc_exel/",PRINT_EXEL_MAUDON, name="print_doc_exel"),#In danh sach mẫu đơn
    path("print_report_exel/",PRINT_EXEL_REPORT, name="print_report_exel"),#In danh sach mẫu đơn



    
#-----------------------------Hướng dẫn sử dụng------------------------------------------------------------------------
    path("manual/",Manual_Show,name='manual'),# Hướng dẫn sử dụng    
    


]
    

