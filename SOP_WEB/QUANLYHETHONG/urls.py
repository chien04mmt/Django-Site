from django.urls import path

#-------Quản lý phần chức năng Modify password
from .views import ShowSearchInfo

#------Quản lý tài khoản
from API.SOP_DB import Load_Dept,Load_permissgroup,Load_manager_room,Load_list_manager_room,Show_TendangnhapInfo
from .views import ACTION_ACOUNT_USER

#------Quản lý quyền hạn
from .views import Get_AutoCode
from .views import Load_Roles,Load_Menus,Load_Group_Permiss,Save_Group_Permiss,ACTION_GROUP_PERMISS

#------Quản lý các danh mục
from .views import Load_OptionsCategorys,Action_Categorys,Action_Menus,Action_Dept_Arrive,Action_TGD


urlpatterns = [
#------------------------------Các url dùng chung----------------------------------------------------------------------

    path("get_autocode/",Get_AutoCode), #Sinh mã tự động

#---------------------------------------------------------------------------------------------------------------------


#------------------------------Quản lý tài khoản-----------------------------------------------------------------------

    path("showsearchinfo/",ShowSearchInfo,name='showsearchinfo'),  #Tìm kiếm tài khoản
    path("load_department/",Load_Dept), #Lấy danh sách phòng ban
    path("load_permissgroup/",Load_permissgroup), #Lấy danh chức vụ quyền hạn
    path("load_manager_room/",Load_manager_room), #Lấy danh quản lý phòng ban cho 1 tài khoản
    path("load_listmanager_room/",Load_list_manager_room), #Lấy danh quản lý phòng ban
    path("show_tendangnhapInf/",Show_TendangnhapInfo), #Lấy thông tin tài khoản hiển thị modal
    path("Action_Acount/",ACTION_ACOUNT_USER), #Thao tác với tài khoản (Thêm sửa xóa)
    
    
    
#------------------------------Quản lý quyền hạn-----------------------------------------------------------------------
    path("load_roles/",Load_Roles), #Lấy danh sách các bảng nhóm quyền hạn
    path("load_menus/",Load_Menus), #Lấy danh sách các danh sách menu
    path("load_groups_permiss/",Load_Group_Permiss), #//Load quyền hạn của nhóm quyền hạn
    path("save_groups_permiss/",Save_Group_Permiss), #//lưu cấu hình nhóm quyền hạn
    path("action_groups_permiss/",ACTION_GROUP_PERMISS), #lưu cấu hình nhóm quyền hạn

    
    
#------------------------------Quản lý các danh mục-----------------------------------------------------------------------
    path("get_OptionCategorys/",Load_OptionsCategorys), #Lấy danh sách các danh mục
    path("action_Categorys/",Action_Categorys), #Thêm sửa xóa Categorys
    path("action_Menus/",Action_Menus), #Thêm sửa xóa Menu
    path("action_DeptArr/",Action_Dept_Arrive), #Thêm sửa xóa quản lý đơn vị Department
    path("Action_TGD/",Action_TGD), #Sửa xóa với tổng giám đốc


]