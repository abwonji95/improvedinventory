from django.db.models import fields
from django.db.models.expressions import Exists
from django.forms import ModelForm,fields, widgets
from inv.myvalidators import *
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
import datetime
from bootstrap_modal_forms.forms import BSModalModelForm



class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])


class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields='__all__'

class StoreForm(ModelForm):
    class Meta:
        model=Store
        fields='__all__'

class PurchaseForm(ModelForm):
    class Meta:
       
        model=Purchase
        fields='__all__'
      


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
           
            'username': None,
            'email': None,
            
        }

class VendorPriceForm(ModelForm):
    class Meta:
        model=VendorPrice
        fields='__all__'
    
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

class TeamleaderRequestForm(ModelForm):
    class Meta:
        model=TeamleaderRequest
        fields='__all__'

class EngineerRequestForm(ModelForm):
    class Meta:
        model=EngineerRequest
        fields='__all__'

class AdminReturnsForm(ModelForm):
    class Meta:
        model=AdminReturns
        fields='__all__'

class TeamleadReturnsForm(ModelForm):
    class Meta:
        model=TeamleadReturns
        fields='__all__'
