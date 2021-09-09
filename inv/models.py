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


# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=200,null=True)
    primary_contact_person=models.CharField(max_length=200,null=True)
    website=models.CharField(max_length=200,null=True)
    primary_contact_person=models.CharField(max_length=200,null=True)
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    email=models.EmailField(max_length=200,null=True)
    shipping_address=models.CharField(max_length=200,null=True)
    billing_address=models.CharField(max_length=200,null=True)
    other_details=models.TextField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name


class Item(models.Model):
    UNITS=(
        ('METERS','METERS'),('PACKET','PACKET'))
    ITEMTYPE=(
        ('Service','Service'),('Goods','Goods'))
    name=models.CharField(max_length=200,null=True,unique=True)
    item_type=models.CharField(max_length=200,null=True,choices=ITEMTYPE)
    sku=models.CharField(max_length=200,null=True,unique=True)
    units=models.CharField(max_length=200,null=True,choices=UNITS)
    item_description=models.TextField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name




   
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
    
    def teamleaders(self):
        return Engineer.objects.all().filter()
   
class Store(models.Model):
    name=models.CharField(max_length=200,null=True,unique=True)
    engineer=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    date_updated=models.DateTimeField(auto_now=True)
    date_created=models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()
    def __str__(self) :
        return self.name

class Issuance(models.Model):
    STATUS=(
            ('Issued','Issued'),('Available','Availabe'),
            )
            
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    issued_to=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    issued_qty= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    store=models.ForeignKey(Store,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()


class Requestitem(models.Model):
    SERVICE=(
            ('installation','installation'),('support','support'),('survey','survey'),
            )
    sitename=models.CharField(max_length=200,null=True)
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    ci_no=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    service=models.CharField(max_length=200,null=True,choices=SERVICE)
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()



class Purchase(models.Model):
    po=models.CharField(max_length=200,null=True)
    vendor=models.ForeignKey(Vendor,null=True,on_delete=models.SET_NULL)
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    purchased_qty= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    price= models.FloatField(default=0,blank=True,validators=[MinValueValidator(0)])
    total_price=models.FloatField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    @property
    def total_price(self):
        return self.purchased_qty * self.price
    
    def __str__(self) :
        return "{} {}".format(self.po,self.item)
   

class Returneditems(models.Model):
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    returned_by=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    store=models.ForeignKey(Store,null=True,on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self) :
            return "{} {}".format(self.item,self.returned_by)


class Stock(models.Model):
    item=models.CharField(max_length=200,null=True)
    current_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    purchased_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    purchased_by=models.CharField(max_length=200,null=True)
    issued_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    issued_by=models.CharField(max_length=200,null=True)
    issued_to=models.CharField(max_length=200,null=True)
    returned_qty=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    returned_by=models.CharField(max_length=200,null=True)
    recieved_by=models.CharField(max_length=200,null=True)
    reorder_level=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    date_updated=models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
   # @property
    #def current_qty(self):
        #return self.purchased_qty + self.current_qty
    

    def purchasestock(sender,instance,**kwargs):
            stock=Stock()
            stock.item=instance.item
            stock.purchased_qty=instance.purchased_qty
            stock.save()
    
    
    post_save.connect(purchasestock,sender=Purchase)

    def returnedstock(sender,instance,**kwargs):
            stock=Stock()
            stock.item=instance.item
            stock.returned_qty=instance.returned_qty
            print('returned success')
            stock.save()
    
    
    post_save.connect(returnedstock,sender=Returneditems)
