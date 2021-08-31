from django.db.models import fields
from django.db.models.expressions import Exists
from django.forms import ModelForm,fields
from inv.myvalidators import *
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields='__all__'

class StoreForm(ModelForm):
    class Meta:
        model=Store
        fields='__all__'

class IssuanceForm(ModelForm):
    class Meta:
        model=Issuance
        fields=['item','store','quantity','status']

class TeamleaderissuanceForm(ModelForm):
    class Meta:
        model=Issuance
        fields=['item','issuedto','quantity','status']


class PurchaseForm(ModelForm):
    class Meta:
        model=Purchase
        fields='__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields='__all__'


        #new
class EngineerForm(forms.ModelForm):
    class Meta:
        model=Engineer
        fields=['first_name','last_name','email','phone','employee_number','role']
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'employee_number':'EMP No',
        }

    def __init__(self,*args,**kwargs):
        super(EngineerForm,self).__init__(*args,**kwargs)
        self.fields['role'].empty_label="Select"
        self.fields['phone'].required=False

class VendorForm(ModelForm):
    class Meta:
        model=Vendor
        fields='__all__'

class ReturneditemsForm(ModelForm):
    class Meta:
        model =Returneditems
        fields='__all__'