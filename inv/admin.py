from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Vendor)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Engineer)
admin.site.register(Issuance)
admin.site.register(Store)
admin.site.register(Account)
