from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.
from .models import *
from .forms import *

class VendorCreateAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','date_created','date_updated']
    form =VendorForm
    list_filter=['name','phone','email','date_created','date_updated']
    search_fields=['name']



class ItemCreateAdmin(admin.ModelAdmin):
    list_display=['name','item_description','item_type','sku','reorder_level','date_created','date_updated']
    form =ItemForm

class VendorPriceCreateAdmin(admin.ModelAdmin):
    list_display=['item','vendor','price','date_created','date_updated']
    form =VendorForm

class StockCreateAdmin(admin.ModelAdmin):
    list_display=['item','purchased_qty','issued_qty','returned_qty','current_qty','date_updated']
    

admin.site.register(Vendor,VendorCreateAdmin)
admin.site.register(Purchase,SimpleHistoryAdmin)
admin.site.register(Engineer,SimpleHistoryAdmin)
admin.site.register(Teamleader,SimpleHistoryAdmin)
admin.site.register(Staff,SimpleHistoryAdmin)
admin.site.register(VendorPrice,VendorPriceCreateAdmin)
admin.site.register(Store,SimpleHistoryAdmin)
admin.site.register(Item,ItemCreateAdmin)
admin.site.register(Stock,StockCreateAdmin)

