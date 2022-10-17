
from multiprocessing import context
from django.http import JsonResponse # AJAX RESPONSE AND REQUEST
from SOP_WEB.settings import MEDIA_URL,MEDIA_ROOT
from django.views.decorators.csrf import csrf_protect,csrf_exempt#Bỏ qua csrftocken# kiểm tra csrtocken của method POST
from django.core.files.storage import FileSystemStorage
from time import strftime
import os
from SOP_WEB import settings


    
# Phương thức Upload file tới server
@csrf_exempt
def simple_upload(request):
    try:
        if request.method == 'POST':
            index=0
            arrlstFile=[]
            strtime=strftime("%Y%m%d%H%M%S")
            stry=strftime("%Y")
            strm=strftime("%m")
            strd=strftime("%d")
            fs = FileSystemStorage() 
            
            if len(request.FILES)==1:
                myfile=request.FILES['myfile']                               
                filename = fs.save(strtime+"_"+ myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                arrlstFile.append(strtime+'_'+ myfile.name)                
            else:
                for item in request.FILES:            
                    if(item.find("myfile")>=0):
                        myfile=request.FILES['myfile'+str(index)]                        
                        filename = fs.save(strtime+"_"+ myfile.name, myfile)
                        uploaded_file_url = fs.url(filename)
                        arrlstFile.append(strtime+'_'+ myfile.name)                    
                        index+=1
            return JsonResponse({'returndata':arrlstFile}, status = 200)
        return JsonResponse({"error":"Can not upload file"}, status = 400)
    except Exception as ex:return JsonResponse({"error":str(ex)}, status = 400)



class OverwriteStorage(FileSystemStorage):
    
    def get_available_name(self, name):      
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name




def change_image(request):
 
    try:
        if request.method == 'POST':          
            myfile=request.FILES['myfile']
            fs = FileSystemStorage()
            namefile= myfile.name
           
            namefile=namefile[namefile.rindex('.'):]
            namefile=request.user.username + namefile
            # print(MEDIA_ROOT)
            if fs.exists(namefile):os.remove(os.path.join(settings.MEDIA_ROOT, namefile))
            filename = fs.save(namefile, myfile)
            uploaded_file_url = fs.url(filename)
            context={'filename':namefile,'path':str(MEDIA_ROOT)+namefile}
            return context
    except Exception as ex:
        return str(ex)
 
 
 
 