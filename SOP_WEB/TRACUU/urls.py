from django.contrib import admin
from django.urls import path
from .views import Load_Department
from .views import TraCuuDSMaVB,TraCuuDSHuyMaVB,TraCuuDSPheBoVB,TraCuuDSPhatHanhVB,TraCuuDSSuaDoiVB,TraCuuTrinhKy,TimKiemPhuLuc
from .views import XEM_CHI_TIET_MOI_LOAI_DON

urlpatterns = [
    path("load_Department/",Load_Department),#Tải danh sách phòng ban

    path("tracuutrinhky/",TraCuuTrinhKy),#Tìm kiếm tiến độ trình ký
    path("tracuudsmavb/",TraCuuDSMaVB),#tra cứu danh sách mã văn bản
    path("tracuudshuymavb/",TraCuuDSHuyMaVB),#tra cứu danh sách hủy mã văn bản
    path("tracuudsphebovb/",TraCuuDSPheBoVB),#tra cứu danh sách phế bỏ văn bản
    path("tracuudsphathanhvb/",TraCuuDSPhatHanhVB),#tra cứu danh sách phát hành văn bản
    path("tracuudssuadoivb/",TraCuuDSSuaDoiVB),#tra cứu danh sách phát hành văn bản
    path("timphuluc/",TimKiemPhuLuc),#Tìm kiếm phụ lục    

    path("chitietdon/",XEM_CHI_TIET_MOI_LOAI_DON),#Chi tiết đơn các đơn văn bản

]
