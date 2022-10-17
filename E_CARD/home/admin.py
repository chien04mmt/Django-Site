from django.contrib import admin

# from login.models import CustomUser

# Register your models here.
from .models import ApplicationDoc,ListAppTitle,DetailDoc,GroupSigner,ListLeaderType
from .models import File_Signer_Work_S,DepartmentGroup,ListApprover
from .models import FilesAdmin,Upload_File_Attack


# Register your models here.
# admin.site.register(RegisterForm)
# admin.site.register(ApplicationDoc)
admin.site.register(ListAppTitle)
# admin.site.register(DetailDoc) #
# admin.site.register(GroupSigner)
# admin.site.register(File_Signer_Work_S)
# admin.site.register(File_Signer_Work_T) #
# admin.site.register(Users_Info) # Thông tin Danh sách Tài khoản
# admin.site.register(DepartmentGroup)# Danh sách các phòng ban thiết lập
# admin.site.register(ListApprover)# Danh sách người ký phê duyệt
# admin.site.register(ListLeaderType)
admin.site.register(FilesAdmin)# Danh sách File Upload
admin.site.register(Upload_File_Attack)# Danh sách File Upload attachment
# admin.site.register(CustomUser)

