import datetime
import socket

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'
    
SESSION_COOKIE_SECURE=False

def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=HOSTNAME,
        secure=SESSION_COOKIE_SECURE or None,
    )
    
    
    # def view(request):
    #     response = HttpResponse("hello")
    # set_cookie(response, 'name', 'jujule')
    # return response