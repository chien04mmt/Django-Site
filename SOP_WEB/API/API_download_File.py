

from genericpath import exists
from django.http import HttpResponse
import os
from django.http import JsonResponse # AJAX RESPONSE AND REQUEST
import mimetypes
from API.is_ajax import is_ajax
from pathlib import Path
# Nhập mô-đun mimetypes

def download_file(request):
    try:
        if is_ajax(request=request) and request.method == "GET": 
            lst_filename=request.GET
            lst_paths=[]
            for item in lst_filename:
                if item.find('lstfile')!=1: 
                    filename=lst_filename[item]
                    strn=filename[0:4]
                    strm=filename[4:6]
                    strd=filename[6:8]
                    filepath='/home/wwwroot/Esign4/Esign/home/static/media/'+filename

                    if os.path.exists(filepath)==False:return JsonResponse({"error":"File không tồn tại, hoặc đã bị xóa"}, status = 400)
                    # print(os.path.exists(filepath))
                    path=open(filepath,'rb').read()
                    
                    # Set the mime type
                    mime_type,_=mimetypes.guess_type(filepath)
                    # Set the return value of the HttpResponse
                    response=HttpResponse(path,content_type=mime_type)
                    # Set the HTTP header for sending to browser
                    response['Content-Disposition']="attachment; filename=%s"% filename
                    # Return the response value
                    # print(response)
                    return response
                    lst_paths.append(filepath)
                    print(lst_paths)
                    return JsonResponse({"returndata":lst_paths}, status = 200)
        return JsonResponse({"error":"ERROR REQUEST 400"}, status = 400)
    except Exception as ex: return JsonResponse({"error":str(ex)}, status = 400)
