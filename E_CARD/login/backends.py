# # customers/backends.py

# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
# from .models import Customer


# class CustomerBackend(ModelBackend):

#     def authenticate(self, request, **kwargs):
#         customer_id = kwargs['username']
#         password = kwargs['password']
#         try:
#             customer = Customer.objects.get(customer_id=customer_id)
#             if Customer.user.check_password(password) is True:
#                 return Customer.user
#         except Customer.DoesNotExist:
#             pass