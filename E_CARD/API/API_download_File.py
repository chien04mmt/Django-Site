

from django.http import HttpResponse
import os
from artice_car.settings import MEDIA_ROOT
from django.http import JsonResponse # AJAX RESPONSE AND REQUEST
import mimetypes
from API.is_ajax import is_ajax

# Nhập mô-đun mimetypes

def download_file(request):
    if is_ajax(request=request) and request.method == "GET": 
        lst_filename=request.GET
        lst_paths=[]
        for item in lst_filename:
            if item.find('lstfile')!=1: 
                filename=lst_filename[item]
                strn=filename[0:4]
                strm=filename[4:6]
                strd=filename[6:8]
                BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))                
                filepath=MEDIA_ROOT+ '/'+filename
                path=open(filepath,'rb').read()
                
                # Set the mime type
                mime_type,_=mimetypes.guess_type(filepath)
                # Set the return value of the HttpResponse
                response=HttpResponse(path,content_type=mime_type)
                # Set the HTTP header for sending to browser
                response['Content-Disposition']="attachment; filename=%s"% filename
                # Return the response value
                return response
    return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)




def download_exel(filename):
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath=MEDIA_ROOT+ '/'+filename
    path=open(filepath,'rb').read()
    # Set the mime type
    mime_type,_=mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response=HttpResponse(path,content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition']="attachment; filename=%s"% filename
    return response












