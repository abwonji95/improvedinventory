from django import forms
from django.db.models import fields
import django_filters 
from .models import *
from django_filters import DateFilter,CharFilter
from django import forms

class PurchaseFilter(django_filters.FilterSet):
    start_date= DateFilter(field_name='date_created',lookup_expr='gte')
    end_date= DateFilter(field_name='date_created',lookup_expr='lte')
    #item= CharFilter(field_name='item',lookup_expr='icontains')
    export_to_CSV=forms.BooleanField()
    class Meta:
        model=Purchase
        fields='__all__'
        exclude=['purchased_qty','price','date_created']