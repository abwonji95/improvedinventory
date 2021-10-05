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




class Item(models.Model):
    UNITS=(
        ('METERS','METERS'),('PACKET','PACKET'))
    ITEMTYPE=(
        ('Service','Service'),('Goods','Goods'))
    name=models.CharField(max_length=200,null=True,unique=True)
    item_type=models.CharField(max_length=200,null=True,choices=ITEMTYPE)
    sku=models.CharField(max_length=200,null=True,unique=True)
    units=models.CharField(max_length=200,choices=UNITS,blank=True)
    item_description=models.TextField(max_length=200,blank=True,default=0)
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
    item=models.ForeignKey(Item,blank=False,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,blank=False,on_delete=models.CASCADE)
    price= models.IntegerField(default=0,blank=False,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        unique_together=[('item','vendor','price')]
   
class Engineer(models.Model):
    ROLE=(
        ('Team leader','Team leader'),('Engineer','Engineer'),
        )
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    employee_number=models.CharField(max_length=200,null=True,unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField(max_length=200,null=True,unique=True)
    role=models.CharField(max_length=200,null=True,choices=ROLE)
    id=models.AutoField(primary_key=True)
    history = HistoricalRecords()
    def __str__(self) :
        return "{} {}".format(self.first_name,self.last_name)
    
 
   
class Store(models.Model):
    name=models.CharField(max_length=200,blank=False,unique=True)
    teamleader=models.ForeignKey(Engineer,blank=False,on_delete=models.CASCADE)
    date_updated=models.DateTimeField(auto_now=True)
    date_created=models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name

    def teamleader(self):
        return Engineer.objects.all().filter(role='Team leader')

class EngineerStock(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

class TeamleaderStock(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

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
    approval=models.CharField(max_length=200,null=True,choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

#request made by  Teamleaders to Admin
class TeamleaderRequest(models.Model):
    STATUS=(
            ('Approve','Approve'),('Disapprove','Disapprove'),('Pending','Pending'),
            )
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    approval=models.CharField(max_length=200,null=True,choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()


class Purchase(models.Model):
    STATUS=(
            ('Approve','Approve'),('Disapprove','Disapprove'),('Pending','Pending'),
            )

    po=models.CharField(max_length=200,blank=False)
    vendor=models.ForeignKey(Vendor,blank=False,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    purchased_qty=models.IntegerField(default=0,blank=False,validators=[MinValueValidator(0)])
    price= models.ForeignKey("inv.VendorPrice",blank=False,on_delete=models.CASCADE)
    approval=models.CharField(max_length=200,null=True,choices=STATUS)
    total_price=models.FloatField(default=0,blank=False,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    @property
    def total_price(self):
        return self.purchased_qty * self.price
    
    def __str__(self) :
        return "{}".format(self.po)
   
'''
class Purchasedetails(models.Model):
    po=models.ForeignKey(Purchase,null=True,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    purchased_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    price=models.FloatField(default=0,blank=True,validators=[MinValueValidator(0)])
    def __str__(self) :
        return "{}".format(self.po)
 ''' 

 #items returned by engineer recieved by Teamlead     
class TeamleadReturns(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    returned_by=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self) :
            return "{} {}".format(self.item,self.returned_by)

#items returned by teamlead recieved by Admin
class AdminReturns(models.Model):
    item=models.ForeignKey(Item,null=True,on_delete=models.CASCADE)
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    store=models.ForeignKey(Store,null=True,on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self) :
            return "{} {}".format(self.item,self.returned_by)


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
    reorder_level=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
            return self.item


   # @property
    #def current_qty(self):
        #return self.purchased_qty + self.current_qty
    
"""
    def purchasestock(sender,instance,**kwargs):
            #stock=Stock()
            #stock.item=instance.item
            #stock.purchased_qty=instance.purchased_qty
            #stock.save()
            print(instance.item)
    
    
    post_save.connect(purchasestock,sender=Purchase)

    def returnedstock(sender,instance,**kwargs):
            stock=Stock()
            stock.item=instance.item
            stock.returned_qty=instance.returned_qty
            print('returned success')
            stock.save()
    
    
    post_save.connect(returnedstock,sender=Returneditems)
"""