

from django.db import models
from django.utils import timezone
from pymysql import *


# Create your models here.

#Tạo danh sách các loại đơn yêu cầu
class ListAppTitle(models.Model):
    Person_Create= models.CharField(max_length=10)   
    app_title = models.CharField(max_length=150) 
    Dept =models.CharField(max_length= 10)
    detail= models.TextField()        
    create_at= models.DateTimeField(default=timezone.now )    
    CHOICES = (
    ('yes','Y'),
    ('no', 'N'))
    課級主管審核=  models.CharField(max_length=5, choices=CHOICES, default='no')   
    部級主管審核=  models.CharField(max_length=5, choices=CHOICES, default='no')   
    處級主管審核=  models.CharField(max_length=5, choices=CHOICES, default='no')   
    Bu_Header=  models.CharField(max_length=5, choices=CHOICES, default='no')   
    經管簽核=  models.CharField(max_length=5, choices=CHOICES, default='no')   
    結案單位=  models.CharField(max_length=5, choices=CHOICES, default='no')   
 
    def __str__(self):
        return self.app_title
    
#Bảng chi tiết đơn mới tạo hoặc đã tạo
class DetailDoc(models.Model):
    Application_No =models.CharField(max_length=14)
    Application_Title = models.CharField(max_length=255)
    Degree_urgency = models.CharField(max_length=10)
    Apply_Person = models.CharField(max_length=30)  
    Apply_Person_Tel = models.CharField(max_length=5)
    Apply_Person_Mail = models.CharField(max_length=100) 
    Apply_File = models.CharField(max_length=255) 
    Attest_File = models.CharField(max_length=255)
    Mail_CC_for_applied =  models.TextField()
    Mail_CC_for_end =   models.TextField()
    Remark	= models.TextField(blank=True)
    Signoff_Status= models.CharField(max_length=30,blank=True)
    Signoff_Station= models.CharField(max_length=30,blank=True)
    Signoff_Person= models.CharField(max_length=30,blank=True)
    Signoff_SupplyPerson= models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.Application_No
    
# Bảng Danh sách đơn và tình trạng closed
class ApplicationDoc(models.Model):
    Application_No = models.ForeignKey(DetailDoc, on_delete=models.CASCADE)
    Degree_of_urgency = models.CharField(max_length=10)
    Application_Title = models.CharField(max_length=255)
    Apply_File = models.CharField(max_length=255)
    Attest_File = models.CharField(max_length=255) 
    Apply_Person = models.CharField(max_length=30) 
    Signoff_Status= models.CharField(max_length=30)
    Signoff_Station= models.CharField(max_length=30)
    Signoff_Person= models.CharField(max_length=30)
    Signoff_SupplyPerson= models.CharField(max_length=30)
    def __str__(self):
        return self.Application_Title

#Bảng thông tin nhóm ký cho 1 đơn nào đó , được tạo cùng đơn mới 
class GroupSigner(models.Model):   
    Application_No =  models.ForeignKey(DetailDoc, on_delete=models.CASCADE)
    Name_grouper=models.CharField(max_length=50)
    Sign_off_Type= models.CharField(max_length=50)
    Sign_off_Person= models.CharField(max_length=30)
    Sign_off_Status	= models.CharField(max_length=30)
    Sign_off_Memo= models.TextField()
    Sign_off_Time=  models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return self.Name_grouper

#Bảng lưu trình ký cho 1 đơn
class File_Signer_Work_S(models.Model):
    Application_No =  models.ForeignKey(DetailDoc, on_delete=models.CASCADE)
    Oder_No= models.FloatField()
    Signer_Type=   models.CharField(max_length= 50)
    Sign_Type=   models.CharField(max_length= 50)
    Is_Check=   models.CharField(max_length= 50)
    Signer=   models.CharField(max_length= 50)
    Status=   models.CharField(max_length= 50)
    Sign_Detail=   models.CharField(max_length= 50)
    Sign_IP=   models.CharField(max_length= 50)
    Sign_Time=   models.DateTimeField(default=timezone.now)
    Sign_FileNameOld=   models.CharField(max_length= 100)
    Sign_FileNameNew=   models.CharField(max_length= 100)
    Sign_Agent=   models.CharField(max_length= 30)
    
# Bảng Danh sách các nhóm phòng ban
class DepartmentGroup(models.Model):
    Dept=models.CharField(max_length= 50)
    Cost_No=models.CharField(max_length= 50)
    Dept_Manager=models.CharField(max_length= 50,blank=True)
    Manager_ID=models.CharField(max_length= 50,blank=True)
    Tel=models.CharField(max_length= 50,blank=True)
    Email=models.CharField(max_length= 50,blank=True)
    def __str__(self):
        return "%s  %s" % (self.Dept, self.Cost_No)
    
# Bảng Danh sách các loại chức vụ
class ListLeaderType(models.Model):
    Leader_Type= models.CharField(max_length= 50) 
    Create_At=models.DateTimeField(default= timezone.now) 
    def __str__(self):
        return "%s " % (self.Leader_Type)

#Bảng danh sách người được quyền ký (chủ quản các cấp)
class ListApprover(models.Model):
    
    User_Id=models.CharField(max_length= 20)  
    User_Name= models.CharField(max_length= 30) 
    Leader_Type= models.OneToOneField(ListLeaderType, on_delete=models.CASCADE)
    Setup_Person=models.CharField(max_length= 30) 
    Setup_Time=models.DateTimeField(default= timezone.now) 
    def __str__(self):
        return "%s __ %s" % (self.User_Id, self.Leader_Type)

#-------------------------------------------------------------------Mới của MYSQL-------------------------------------------------

#bảng thông tin chức vụ Người ký Process_t
class Process_t(models.Model):
    WORKFLOW_NAME=models.CharField(max_length= 50)  
    PROCESS_NUMBER= models.CharField(max_length= 10) 
    PROCESS_TITLE=models.CharField(max_length= 100) 
    STATION_TILE=models.CharField(max_length= 255) 
    STATION_CONDITION=models.CharField(max_length= 255)  

    def __str__(self):
        return "%s __ %s" % (self.STATION_CONDITION, self.PROCESS_NUMBER)

#bảng trạng thái đơn (đóng,chờ,...) __wf_r_document_t
class Document_t(models.Model):
    WORKFLOW_NAME=models.CharField(max_length= 50)  
    DOC_NO= models.CharField(max_length= 25) 
    CREATE_DATE=models.DateTimeField(default= '') 
    AUTHOR_ID=models.CharField(max_length= 20) 
    STATION_CONDITION=models.IntegerField()
    APPROVAL_TIME=models.DateTimeField(default= '') 
    NEXT_APPROVER=models.CharField(max_length= 20)  
    AGENT=models.CharField(max_length= 30) 
    STATUS=models.CharField(max_length= 20) 
    FORWARD=models.CharField(max_length= 255) 
    REAL_APPROVAL=models.CharField(max_length= 255) 
    SERIAL_APPROVAL=models.CharField(max_length= 255) 
    def __str__(self):
        return "%s __ %s" % (self.DOC_NO, self.NEXT_APPROVER)

#Bảng lịch sử người đã phê duyệt __wf_r_approversign_t
class Approvalsign_t(models.Model):
    WORKFLOW_NAME=models.CharField(max_length= 50)  
    DOC_NO= models.CharField(max_length= 25) 
    STEP_NO=models.IntegerField()
    STATION_CONDITION=models.IntegerField()
    STATION_TILE=models.CharField(max_length= 50) 
    EMP_NO=models.CharField(max_length= 20) 
    STATUS=models.CharField(max_length= 20) 
    HAVE_COMMENT=models.IntegerField()
    APPROVAL_TIME=models.DateTimeField(default= '')   
    ORG_APPROVER_NO=models.CharField(max_length= 20) 
    def __str__(self):
        return "%s __ %s" % (self.DOC_NO, self.NEXT_APPROVER)
    
    
#Bảng lịch sử truy cập server SESSION_T
class Session_t(models.Model):
    SESION_ID=models.CharField(max_length= 50)  
    CONNECT_IP= models.CharField(max_length= 50) 
    CONNECT_HOSTNAME=models.CharField(max_length= 50) 
    STATION_CONDITION=models.CharField(max_length= 50) 
    WORK=models.CharField(max_length= 255) 
    LAST_VISIT=models.DateTimeField(default= '')   
    STATION_CONDITION=models.TextField(default= '')

    def __str__(self):
        return "%s __ %s" % (self.CONNECT_IP, self.WORK)
    
#Bảng Danh sách loại đơn generate_doc_t
class Generate_Doc_t(models.Model):
    WORKFLOW_NAME=models.CharField(max_length= 50)  
    FORMAT= models.CharField(max_length= 50) 
    TICKET=models.CharField(max_length= 24) 
    CREATE_DATE=models.DateTimeField(default= '')   
    NO=models.IntegerField(default=NULL)
   
    def __str__(self):
        return self.FORMAT
    
# Bảng Danh sách file được upload
class  Upload_File_Attack(models.Model):
    Apply_No=models.CharField(max_length= 50,blank=True)  
    File_Name= models.CharField(max_length= 1000,blank=True) 
    File_upload=models.FileField(blank=True)
    def __str__(self):
        return self.Apply_No
  
class FilesAdmin(models.Model):
    Apply_No = models.CharField(max_length=50,blank=True)
    File_Name = models.CharField(max_length=1000,blank=True)
    File_upload = models.FileField(upload_to='media',blank=True)
    total_downloads = models.IntegerField(default=0,blank=True)
    def __str__(self):
        return self.Apply_No
  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    