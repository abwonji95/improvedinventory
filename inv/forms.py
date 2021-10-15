from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm
from django.forms import ModelForm,fields, widgets
from django.db.models.expressions import Exists
from django.contrib.auth.models import User
from django.db.models import fields
from inv.myvalidators import *
from django import forms
from .models import *
import datetime

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'

   
class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields='__all__'

class VendorPriceForm(forms.ModelForm):
    class Meta:
        model=VendorPrice
        fields='__all__'

class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields='__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model=Purchase
        fields='__all__'
      


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model= User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            
        }
class ChangingPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Enter password',widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})),
    new_password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})),
    new_password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})),
    class Meta:
        model= User
        fields = ("old_password", "new_password1", "new_password2")
    help_texts = {
            'new_password1': None,
            'new_password2': None,
            
        }

class ResetPasswordForm(PasswordResetForm):
  
    new_password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})),
    new_password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})),
    class Meta:
        model= User
        fields = ( "new_password1", "new_password2")
    help_texts = {
            'new_password1': None,
            'new_password2': None,
            
        }
    
class EngineerForm(forms.ModelForm):
    class Meta:
        model=Engineer
        fields=['first_name','last_name','email','phone','employee_number']
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'employee_number':'EMP No',
        }

    def __init__(self,*args,**kwargs):
        super(EngineerForm,self).__init__(*args,**kwargs)
        self.fields['role'].empty_label="Select"
        self.fields['phone'].required=False


class TeamleaderRequestForm(forms.ModelForm):
    class Meta:
        model=TeamleaderRequest
        fields='__all__'

class EngineerRequestForm(forms.ModelForm):
    class Meta:
        model=EngineerRequest
        fields='__all__'

class TeamleadReturnsForm(forms.ModelForm):
    class Meta:
        model=TeamleadReturns
        fields='__all__'

class EngineerReturnsForm(forms.ModelForm):
    class Meta:
        model=EngineerReturns
        fields='__all__'
