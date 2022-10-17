# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import  AbstractBaseUser , PermissionsMixin , BaseUserManager,AbstractUser

# from pydantic import BaseModel

# # Create your models here.


# class Customer(BaseModel):
#     customer_id = models.CharField(max_length=10)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     opject=models.Manager()

#     def __str__(self):
#         return self.customer_id
    
    
    
  
# CUSTOM lại bảng USER

# class CustomUserManager(BaseUserManager):

#     def create_user(self,username, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not username:
#             raise ValueError('The USER_ID must be set')
#         username = self.normalize_email(username)
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, username, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(username, password, **extra_fields)


# class CustomUser(AbstractUser):
#     # username = None
#     # email = models.EmailField(_('email address'), unique=False)
#     username=models.CharField(max_length=20,unique=True)
#     USER_NAME =models.CharField(max_length= 50,blank=True,unique=True)   
#     EXT=models.CharField(max_length= 20,blank=True,unique=True)
#     SEX=models.CharField(max_length= 30,blank=True,unique=True)
#     GRADE=models.CharField(max_length= 30,blank=True,unique=True)
#     JOB_TITLE=models.CharField(max_length=50,blank=True,unique=True)
#     CURRENT_OU_CODE =models.CharField(max_length= 30,blank=True,unique=True)
#     CURRENT_OU_NAME =models.CharField(max_length= 30,blank=True,unique=True)
#     CARD_ID =models.CharField(max_length= 30,blank=True,unique=True)
#     HIRE_DATE =models.CharField(max_length= 30,blank=True,unique=True)
#     LEAVE_DAY =models.CharField(max_length= 30,blank=True,unique=True)
    
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.username
    
    
