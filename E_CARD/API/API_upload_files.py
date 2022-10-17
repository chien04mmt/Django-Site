
from multiprocessing import context
from operator import indexOf
from django.http import JsonResponse # AJAX RESPONSE AND REQUEST
from artice_car.settings import MEDIA_URL
from django.views.decorators.csrf import csrf_protect # kiểm tra csrtocken của method POST
from django.core.files.storage import FileSystemStorage
from time import strftime
from home.models import FilesAdmin
from API.resize_image import RESIZE_IMAGE
from django.views.decorators.csrf import csrf_exempt#Bỏ qua csrftocken
    
# Phương thức Upload file tới server
@csrf_protect
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile0']:
        index=0
        arrlstFile=[]
        for item in request.FILES:
            if(item.find("myfile")>=0):
                myfile=request.FILES['myfile'+str(index)]
                fs = FileSystemStorage()
                strtime=strftime("%Y%m%d%H%M%S")
                stry=strftime("%Y")
                strm=strftime("%m")
                strd=strftime("%d")
                filename = fs.save(strtime+ myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                arrlstFile.append(strtime+ myfile.name)
                
                #lưu thông tin file upload vào Model AdminUpload
                model= FilesAdmin(Apply_No=filename,File_Name=filename,File_upload=filename)
                model.save()
            
                #print(uploaded_file_url)
                # <a href='{{ MEDIA_URL }}{{ file.relative_path }}'>{{ file.name }}</a>đường dẫn file tải
                #print(MEDIA_URL +stry+"/"+strm+"/"+strd+"/" +strtime+ myfile.name )
                index+=1
        return JsonResponse({'returndata':arrlstFile}, status = 200)
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)


import os
from artice_car.settings import MEDIA_ROOT
class OverwriteStorage(FileSystemStorage):
    
    def get_available_name(self, name):      
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(MEDIA_ROOT, name))
        return name


@csrf_exempt
def change_image(request):
    if request.method == 'POST' and request.FILES['myfile']:

        myfile=request.FILES['myfile']
        fs = FileSystemStorage()
        
        namefile= myfile.name
        namefile=namefile[namefile.rindex('.'):]
        namefile=request.user.username + namefile
        # print(namefile)
        if fs.exists(namefile):os.remove(os.path.join(MEDIA_ROOT+'/', namefile))
        filename = fs.save(namefile, myfile)
        uploaded_file_url = fs.url(filename)
        
        context={'filename':namefile,'path':os.path.join(MEDIA_ROOT+'/', namefile)}
        return context
    return ''




#Upload file exel lên server
@csrf_exempt
def upload_exel(request,filename):
    if request.method == 'POST' and request.FILES['myfile']:
        user= request.user.username
        myfile=request.FILES['myfile']
        fs = FileSystemStorage()
        namefile=user+"_"+  filename

        if fs.exists(namefile):os.remove(os.path.join(MEDIA_ROOT+'/', namefile))
        fs.save(namefile, myfile)

        uploaded_file_url = fs.url(filename)
        context={'filename':namefile,'path':os.path.join(MEDIA_ROOT+'/', namefile)}
        return context
    return False





#UPLOAD PHOTO
@csrf_exempt
def UPLOAD_PHOTO(request,filename):
    if request.method == 'POST' and request.FILES['myfile']:        
        myfile=request.FILES['myfile']
        
        fs = FileSystemStorage()
        namefile= filename+(myfile.name[myfile.name.rindex('.'):])
        newfile=namefile[0:namefile.rindex('.')]+".jpg"
        try:
            if fs.exists(newfile):os.remove(os.path.join(MEDIA_ROOT+'/', newfile))
        except:pass

        fs.save(newfile, myfile)

        uploaded_file_url = fs.url(filename)
        path=os.path.join(MEDIA_ROOT+'/', newfile)
        context={'filename':newfile,'path':path}
        try:RESIZE_IMAGE(path)
        except:pass
        
        return context
    return False