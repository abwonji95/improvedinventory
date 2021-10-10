#from typing_extensions import Required
from django.db import models
from simple_history.models import HistoricalRecords
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField, IntegerField
from django.db.models import Avg, Max, Min, Sum
from django.core.validators import MinValueValidator,MinLengthValidator
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.db.models.signals import post_delete, pre_save,post_save
import datetime
#from postgres.fields import JSONField
# Create your models here.


class Engineer(models.Model):
  
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    employee_number=models.CharField(max_length=200,null=True,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField(max_length=200,null=True,unique=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return "{} {}".format(self.first_name,self.last_name)

class Teamleader(models.Model):
    
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    employee_number=models.CharField(max_length=200,null=True,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField(max_length=200,null=True,unique=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return "{} {}".format(self.first_name,self.last_name)
    
class Staff(models.Model):
    
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    employee_number=models.CharField(max_length=200,null=True,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField(max_length=200,null=True,unique=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return "{} {}".format(self.first_name,self.last_name)
    


class Item(models.Model):
    UNITS=(
        ('METERS','METERS'),('PACKET','PACKET'))
    ITEMTYPE=(
        ('Service','Service'),('Goods','Goods'))
    name=models.CharField(max_length=200,null=True,unique=True)
    item_type=models.CharField(max_length=200,null=True,choices=ITEMTYPE)
    sku=models.CharField(max_length=200,null=True,unique=True)
    units=models.CharField(max_length=200,choices=UNITS,blank=True)
    item_description=models.TextField(max_length=200,blank=True,default="Item description")
    reorder_level=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    purchased_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    issued_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    current_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name


class Vendor(models.Model):
    name=models.CharField(max_length=200,unique=True)
    primary_contact_person=models.CharField(max_length=200,blank=True)
    website=models.CharField(max_length=200,blank=True)
    items=models.ManyToManyField(Item,through='VendorPrice')
    phone = PhoneNumberField( null=True,blank=True, unique=True)
    email=models.EmailField(max_length=200,blank=True)
    shipping_address=models.TextField(max_length=200,blank=True)
    billing_address=models.TextField(max_length=200,blank=True)
    other_details=models.TextField(max_length=200,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name
    



class VendorPrice(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    price=models.IntegerField(default=0,null=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        unique_together=[('item','vendor')]

    def __str__(self) :
            return "{} {}".format(self.vendor,self.item,)

class Purchase(models.Model):
  
    po=models.CharField(max_length=200,blank=False)
    vendor=models.ForeignKey(Vendor,blank=False,on_delete=models.CASCADE)
    items=models.ForeignKey(Item, null=True,on_delete=models.CASCADE)
    purchased_qty=models.IntegerField(default=0,blank=False,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self) :
        return "{}".format(self.po)
    
class Stock(models.Model):
    
    
    item=models.CharField(max_length=200,null=True,unique=True)
    current_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    purchased_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    purchased_by=models.CharField(max_length=200,null=True)
    approved_by=models.CharField(max_length=200,null=True)
    issued_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    issued_by=models.CharField(max_length=200,null=True)
    issued_to=models.CharField(max_length=200,null=True)
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    returned_by=models.CharField(max_length=200,null=True)
    recieved_by=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
   
#request made by  Teamleaders to Admin
class TeamleaderRequest(models.Model):
  
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    requested_qty= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    approval=models.CharField(max_length=200,null=True,default='Pending')
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

class TeamleaderStock(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

#items returned by teamlead recieved by Admin
class TeamleadReturns(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self) :
            return "{} {}".format(self.item,self.returned_by)



#request made by engineers to Teamleaders
class EngineerRequest(models.Model):
    STATUS=(
            ('Approve','Approve'),('Disapprove','Disapprove'),('Pending','Pending'),
            )
    SERVICE=(
            ('Installation','Installation'),('Support','Support'),('Survey','Survey'),
            )
    sitename=models.CharField(max_length=200,null=True)
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    ci_no=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    service=models.CharField(max_length=200,null=True,choices=SERVICE)
    approval=models.CharField(max_length=200,null=True,default='Pending')
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

class EngineerStock(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

class EngineerReturns(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    returned_by=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self) :
            return "{} {}".format(self.item,self.returned_by)


 
   
class Store(models.Model):
    name=models.CharField(max_length=200,blank=False,unique=True)
    teamleader=models.ForeignKey(Teamleader,null=True,blank=False,on_delete=models.CASCADE)
    date_updated=models.DateTimeField(auto_now=True)
    date_created=models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name



