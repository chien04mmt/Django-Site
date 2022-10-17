
from django.urls import path
from .views import  TaoYeuCauCongVanDen,DuyetCongVan,TraCuuCongVan,ChiTietCongVan,Approval_Doc

from API.API_upload_files import simple_upload
from API.API_download_File import download_file

urlpatterns = [
    path("taoyeucaucv/",TaoYeuCauCongVanDen),#Tạo yêu cầu công văn đến
    path("chitietdon_CVD/",ChiTietCongVan),#Hiển thị chi tiết công văn đến
    path("duyet_CVD/",DuyetCongVan),#lấy danh sách công văn đến
    path("search_SOP_H/",TraCuuCongVan),#Tìm kiếm công văn đến
    path("Appro_SOP_H/",Approval_Doc),#Phê duyệt ký công văn đến
]
