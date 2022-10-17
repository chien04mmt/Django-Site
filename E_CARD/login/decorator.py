
from django.http import HttpResponse,JsonResponse


def Check_login_byAjax(function):
    def wraper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return JsonResponse({'error':'Please login and try again!'}, status=400)
    return wraper