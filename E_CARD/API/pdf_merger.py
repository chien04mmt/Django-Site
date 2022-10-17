# pdf_merger2.py

from email.mime import base
from operator import truediv
import PyPDF2

from django.http import HttpResponse
from django.http import JsonResponse # AJAX RESPONSE AND REQUEST
import mimetypes
import os
from Esign.settings import BASE_DIR,MEDIA_ROOT
from API.is_ajax import is_ajax

# Path_file_input1='home/static/media/20220329151209GANGWANGBAOFEI.pdf'
# Path_file_input2='home/static/media/20220329154520Add new 67 IP Cameras for M09-3F WH at GZ area.pdf'


def MERGE_PDF(Path_file_input1,Path_file_input2):

    f1= open(MEDIA_ROOT+ '/'+Path_file_input1,'rb')
    f2= open(MEDIA_ROOT+ '/'+Path_file_input2,'rb')

    pdf1= PyPDF2.PdfFileReader(f1)
    pdf2=PyPDF2.PdfFileReader(f2)

    pdf1_pages=pdf1.getNumPages()
    pdf2_pages=pdf2.getNumPages()
        
    output_file=open('API/PDFOUT/new_marge.pdf','wb')
    writer= PyPDF2.PdfFileWriter()

    for i in range(pdf1_pages):
        writer.addPage(pdf1.getPage(i))
        
    for j in range(pdf2_pages):
        writer.addPage(pdf2.getPage(j))

    writer.write(output_file)

    f1.close()
    f2.close()
    output_file.close()
    return True


def download_Merge_PDF():
        filename='new_marge.pdf'
        filepath='API/PDFOUT/new_marge.pdf'
        path=open(filepath,'rb').read()
        # Set the mime type
        mime_type,_=mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response=HttpResponse(path,content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition']="attachment; filename=%s"% filename
        # Return the response value
        return response


# MERGE_PDF(Path_file_input1,Path_file_input2)
