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

class StockCreateAdmin(admin.ModelAdmin):
    list_display=['item','purchased_qty','issued_qty','returned_qty','current_qty']

admin.site.register(Vendor,VendorCreateAdmin)
admin.site.register(Purchase,SimpleHistoryAdmin)
admin.site.register(Engineer)
admin.site.register(Issuance)
admin.site.register(Store)
admin.site.register(Stock,StockCreateAdmin)
admin.site.register(Returneditems)
