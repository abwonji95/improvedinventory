from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from .models import *

def engineer_profile(sender,instance,created, **kwargs):
   
    if created:
        group=Group.objects.get(name="staff")
        instance.groups.add(group)
        print("you are a genius")

post_save.connect(engineer_profile,sender=User)

def purchasestock(sender,instance,created,**kwargs):
    if created:
            print("created successfully")
            print(instance.item)
    
    
post_save.connect(purchasestock,sender=Purchase)