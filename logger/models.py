from django.db import models
from registration.models import user
import uuid
# Create your models here.
class Hospitals(models.Model):
    gid = models.IntegerField(primary_key=True)
    hosp_name = models.CharField(max_length=250)
    lat = models.FloatField()
    long = models.FloatField()
    address=models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    type = models.CharField(max_length=200,default='null')
    total_beds = models.FloatField()
    occupied_b = models.FloatField()
    available = models.FloatField()
    total_vent = models.FloatField()
    used_venti = models.FloatField()
    availabl_1 = models.FloatField()
    total_staf = models.FloatField()
    geom = models.CharField(max_length=200)

    class Meta:
        db_table = "Hospitals"


class Logger(models.Model):
    logger = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    # created_time = models.CharField(max_length=100,default='null')
    visited_time = models.CharField(max_length=100)
    description = models.CharField(max_length=200,default='null')
    status = models.CharField(max_length=100,default='To be Valid')
    hosp= models.ForeignKey(Hospitals,on_delete=models.SET_NULL,null=True,related_name='Hospitals')
    user=models.ForeignKey(user,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = "Logger"

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    product_name = models.CharField(max_length=100,default='null')
    product_price = models.FloatField()
    product_type = models.CharField(max_length=100,default='null')
    latx = models.FloatField(default=0)
    longy = models.FloatField(default=0)

    class Meta:
        db_table = "Product"

class Feedback(models.Model):
    feedbackid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #userid = models.CharField(max_length=50, blank=True, default='null', null=True)
    Feedback = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    user=models.ForeignKey(user,on_delete=models.SET_NULL,null=True)
    class Meta:
        verbose_name_plural = 'Feedback'
        db_table = "Feedback"