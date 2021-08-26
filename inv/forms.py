from django.db.models import fields
from django.db.models.expressions import Exists
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EngineerForm(ModelForm):
    class Meta:
        model=Engineer
        fields=['first_name','last_name','email','phone','employee_number','role']


class EngineerUpdateForm(ModelForm):
    class Meta:
        model=Engineer
        fields=['first_name','last_name','email','phone','employee_number','role']

class VendorForm(ModelForm):
    class Meta:
        model=Vendor
        fields='__all__'


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class StoreForm(ModelForm):
    class Meta:
        model=Store
        fields='__all__'

class IssuanceForm(ModelForm):
    class Meta:
        model=Issuance
        fields='__all__'

class TeamleaderissuanceForm(ModelForm):
    class Meta:
        model=Teamleaderissuance
        fields='__all__'

class RequestproductForm(ModelForm):
    class Meta:
        model=Requestproduct
        fields=['product','quantity','sitename','service']

class PurchaseForm(ModelForm):
    class Meta:
        model=Purchase
        fields='__all__'


class StockForm(ModelForm):
    class Meta:
        model=Purchase
        fields=['product','vendor','quantity',]

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','first_name','last_name','email','password1','password1'

        ]
class ProductreturnForm(ModelForm):
    class Meta:
        model= Productreturn
        fields='__all__'