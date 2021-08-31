from django.db import models
from django.db.models.fields import EmailField, IntegerField
from django.db.models import Avg, Max, Min, Sum
from django.core.validators import MinValueValidator,MinLengthValidator
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=15,validators=[MinLengthValidator(9)])
    email=models.EmailField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name


class Item(models.Model):
    UNITS=(
        ('METERS','METERS'),('PACKET','PACKET'),('EXACT','EXACT')
        )
    name=models.CharField(max_length=200,null=True)
    units=models.CharField(max_length=200,null=True,choices=UNITS)
    item_description=models.TextField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name


class Account(models.Model):
    VIEW=(
        ('Team leader','Team leader'),('Engineer','Engineer'),('Admin','Admin')
        )
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    view=models.CharField(max_length=200,null=True,choices=VIEW)
   
class Engineer(models.Model):
    ROLE=(
        ('Team leader','Team leader'),('Engineer','Engineer'),
        )
    date_created=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    employee_number=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=15,validators=[MinLengthValidator(9)])
    email=models.EmailField(max_length=200,null=True)
    role=models.CharField(max_length=200,null=True,choices=ROLE)
    id=models.AutoField(primary_key=True)
    def __str__(self) :
        return "{} {}".format(self.first_name,self.last_name)
    
    def teamleaders(self):
        return Engineer.objects.all().filter()
   
class Store(models.Model):
    name=models.CharField(max_length=200,null=True)
    engineer=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    def __str__(self) :
        return self.name

class Issuance(models.Model):
    STATUS=(
            ('Issued','Issued'),('Available','Availabe'),
            )
            
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    issuedto=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    store=models.ForeignKey(Store,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS)


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




class Purchase(models.Model):
    STATUS=(
            ('COMPLETED','COMPLETED'),('PENDING','PENDING'),('CANCELED','CANCELED'),
            )
    po= models.CharField(max_length=10,null=True)
    vendor=models.ForeignKey(Vendor,null=True,on_delete=models.SET_NULL)
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    quantity= models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    price= models.FloatField(default=0,blank=True,validators=[MinValueValidator(0)])
    total_price=models.FloatField(default=0,blank=True,validators=[MinValueValidator(0)])
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    @property
    def total_price(self):
        return self.quantity * self.price
    
    def __str__(self) :
        return "{} {}".format(self.po,self.item)
   

class Returneditems(models.Model):
    quantity=models.IntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    item=models.ForeignKey(Item,null=True,on_delete=models.SET_NULL)
    returnedby=models.ForeignKey(Engineer,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    store=models.ForeignKey(Store,null=True,on_delete=models.SET_NULL)

    def __str__(self) :
            return "{} {}".format(self.item,self.returnedby)
