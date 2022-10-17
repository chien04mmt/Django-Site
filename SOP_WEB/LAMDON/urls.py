from django.contrib import admin
from django.urls import path
from .views import  DonXinPhatHanhVB,HuyMaVanBan,PheBoVanBan,SuaChuaVanBan
from .views import DonXinMaVB,NoiDungDonXinMa
from .views import TimMaDeHuyMaVB,TaoDonHuyMaVB,LuuDonHuyMaVB
from .views import HUY_HOAC_DUYET_DON_BAT_KY

from API.API_upload_files import simple_upload
from API.API_download_File import download_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path("phathanhvb/",DonXinPhatHanhVB,name='phathanhvb'),
    path("huymavb/",HuyMaVanBan,name='huymavb'),
    path("phebovb/",PheBoVanBan,name='phebovb'),
    path("suachuavb/",SuaChuaVanBan,name='suachuavb'),
    path("donxinma/",DonXinMaVB,name='donxinma'),   #Đơn xin mã văn bản
    path("CreateCancelDocNo/",TaoDonHuyMaVB,name='CreateCancelDocNo'),#Tạo đơn hủy mã văn bản
     
     
    path("chitietdinxinma/",NoiDungDonXinMa),


    
    path("ApproOrCancelDocument/",HUY_HOAC_DUYET_DON_BAT_KY),#hủy bỏ hoặc duyệt đơn bất kỳ

    # path("duyetdkmavb/",DuyetDKMavb),#Duyệt đăng ký mã văn bản
    # path("cancel_registercode/",HuyDKMavb),#Hủy đăng ký mã văn bản
    path("get_ListRegisterCodeDocumentByDCC/",TimMaDeHuyMaVB),#Tìm các mã đã cấp DCC để hủy mã văn bản
    path("InsertOrUpdateRegisterCancelDocument/",LuuDonHuyMaVB),#Lưu đơn hủy mã VB
    # path("AcceptRegisterCancelDocument/",DuyetDKHuyMavb),#Ký duyệt đơn đăng ký mã văn bản
     
    path("simple_upload/",simple_upload, name="simple_upload"),# Upload file simple
    path('download_file/', download_file), # add this route

    
]
