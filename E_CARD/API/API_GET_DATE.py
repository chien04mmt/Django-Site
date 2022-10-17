
from time import strftime
#Hàm trả về chuỗi ngày
def GET_STR_DATE():
    strtime=strftime("%Y%m%d%H%M%S")
    stry=strftime("%Y")
    strm=strftime("%m")
    strd=strftime("%d")
    day=strftime("%Y%m%d")
    return day
    
#Hàm trả về chuỗi thời gian 
def GET_STR_DATE_TIME():
    strtime=strftime("%Y%m%d%H%M%S")
    stry=strftime("%Y")
    strm=strftime("%m")
    strd=strftime("%d")
    day=strftime("%Y%m%d%H%M")
    return day

#Hàm trả về chuỗi giờ hiện tại
def GET_STR_TIME():
    strtime=strftime("%Y%m%d%H%M%S")
    stry=strftime("%Y")
    strm=strftime("%m")
    strd=strftime("%d")
    time=strftime("%H%M%S")
    return time

