        
from django.http import HttpResponseRedirect
def cost_login_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff != 0:
                return function(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    return wrapper
       
        
        