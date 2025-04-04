import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,GroupManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import PermissionDenied
#from django.contrib.auth.models import Permission
#from company.models import Company
#from httplib2 import Response


#Create your models here.

#Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)
#    created_by=models.ForeignKey(user, on_delete=models.SET_NULL, null=True)      
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
    class Meta:
        verbose_name_plural = 'Role'     
    def __str__(self):
        return str(self.name)



#custom user
class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("email required")
        if not username:
            raise ValueError("username required")

        user=self.model(
            email=self.normalize_email(email),
            username=username)

        user.set_password(password)
        user.save(using=self.db)
        return user 

    def create_superuser(self,email,username,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,)
        
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)
        return user
        
class user(AbstractBaseUser):
    name=models.CharField(verbose_name="full_name",max_length=2250)
    email=models.EmailField(verbose_name="email",max_length=22250,unique=True)
    username=models.CharField(max_length=2250,unique=True)
    mobile_no=models.CharField(max_length=2250,unique=True)
    is_activated = models.BooleanField(default=False)#registration field
    is_activate = models.BooleanField(default=False)#after registration email status field
    is_subscribed = models.BooleanField(default=False) 
    activation_code = models.CharField(max_length=2250, blank=True,  default='null', null=True)
    forgot_pass_code = models.CharField(max_length=2250, blank=True,  default='null', null=True)
    forgot_pass_time = models.DateTimeField(null=True)
    last_password_change = models.DateTimeField(null=True)
    forgot_password_is_active=models.BooleanField(default=False)# To deactivate link after forgot password done
    forgot_password_reset_secret_key = models.CharField(max_length=16, null=True)
    forgot_password_reset_secret_time = models.DateTimeField(null=True)
   # forgot_password_token = models.CharField(max_length=2250)
    is_on_trial = models.CharField(max_length=10, blank=True,  default='null', null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    trial_expiry_date = models.DateField(blank=True, null=True)
    dob=models.DateField(blank=True, null=True)
    company = models.CharField(max_length=250, blank=True, default='null', null=True)
    industry = models.CharField(max_length=250, blank=True, default='null', null=True)
    country = models.CharField(max_length=250, blank=True, default='null', null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)  
    gender = models.CharField(max_length=250, blank=True, default='null', null=True)
    district = models.CharField(max_length=250, blank=True, default='null', null=True)
    username = models.CharField(max_length=250, blank=True, default='null', null=True)
    department = models.CharField(max_length=250, blank=True, default='null', null=True)
    designation = models.CharField(max_length=250, blank=True, default='null', null=True)
    image = models.ImageField(default='image', blank=True, null=True)
    provider=models.CharField(max_length=250, blank=True, default='null', null=True)
    address = models.CharField(max_length=100, blank=True, default='null', null=True)    
    pincode = models.BigIntegerField(blank=True, default=0, null=True)
    city = models.CharField(max_length=250, blank=True, default='null', null=True)
    state = models.CharField(max_length=250, blank=True, default='null', null=True)    
    created_id = models.CharField(max_length=250, blank=True, default='null', null=True)
    created_date = models.DateTimeField(auto_now_add=True)#add current time in minute to the database table
    modified_id = models.CharField(max_length=250, blank=True, default='null', null=True)
    modified_date = models.DateTimeField(auto_now=True)# it adds the time that is currently updated
    deleted_id = models.CharField(max_length=250, blank=True, default='null', null=True)
    deleted_date = models.DateTimeField(auto_now=True)
  #  role=models.CharField(max_length=250)
    
    country=models.CharField(max_length=250)
    password = models.CharField(max_length=250, blank=True,  default='null', null=True)
  #  permissions=models.ManyToManyField(Permission)
   # role=models.ForeignKey(Role,on_delete=models.CASCADE, null=True)
    date_joined=models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last_login", auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username',]

    objects=MyUserManager()


    def __str__ (self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser



    
    
#Table for User Subscription
class Subscribe(models.Model):
    subscriber_id = models.UUIDField(primary_key=True, default = uuid.uuid4) 
    full_name = models.CharField(max_length=250, blank=True, default='null', null=True)
    mobile_no = models.CharField(max_length=15, blank=True, default='null', null=True)
    email = models.EmailField(max_length=250, blank=True, default='null', null=True)
    username = models.CharField(max_length=250, blank=True, default='null', null=True)    
    is_subscribed = models.BooleanField(default=False)    
    country = models.CharField(max_length=250, blank=True, default='null', null=True)  
    user_id = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)      
    created_id = models.CharField(max_length=250, blank=True, default='null', null=True)
    created_date = models.DateTimeField(auto_now_add=True)#add current time in minute to the database table
    modified_id = models.CharField(max_length=250, blank=True, default='null', null=True)
    modified_date = models.DateTimeField(auto_now=True)# it adds the time that is currently updated
    deleted_id = models.CharField(max_length=250, blank=True, default='null', null=True)
    deleted_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Subscribe"
        verbose_name_plural = 'subscribe'     
    def __str__(self):
        return self.username

#Table for feedback



class UserDetails(models.Model):
    device=models.TextField(default="",max_length=100)
    device_type=models.TextField(default="",max_length=100)
    browser=models.CharField(default="",max_length=100)
    browser_family=models.CharField(default="",max_length=100)
    browser_version=models.CharField(default="",max_length=100)
    os_type=models.CharField(default="",max_length=100)
    os_family=models.CharField(default="",max_length=100)
    os_version=models.CharField(default="",max_length=100)
    ip=models.TextField(default="",max_length=100)

    def __str__(self):
       return self.device_type

######API For saving user details###############

#################################
# class Company_Users(models.Model):
#     User = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
#     company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)  
#     role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)  
#     def __str__(self):
#        return self.User