from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from .models import *
from .views import *

def engineer_profile(sender,instance,created, **kwargs):
   
    if created:
        #test if groups exists 
        #if exists assign to user
        #if not exist create new groups and assign to user
        group=Group.objects.get(name="staff")
        instance.groups.add(group)
        print("you are a genius")

post_save.connect(engineer_profile,sender=User)

def purchasestock(sender,instance,created,**kwargs):
    if created:
            stock=Stock() 
            if Stock.objects.all().filter(item=instance.items).exists():
                item=Stock.objects.get(item=instance.items)
                stock.purchased_qty=item.purchased_qty
                item.purchased_qty=stock.purchased_qty+instance.purchased_qty
                item.current_qty=stock.current_qty+item.purchased_qty
                if item.current_qty>100:
                    item.status='In stock'
                elif item.current_qty<=100:
                    item.status='Stock Running Low'
                    #send alert/email
                else:
                    item.status='Out of stock'
                item.save()

            else:
                stock.item=instance.items
                stock.purchased_qty=+instance.purchased_qty
                stock.current_qty=+stock.purchased_qty
                stock.status='In Stock'
                stock.save()

post_save.connect(purchasestock,sender=Purchase)

def issue_stock(sender,instance,created,**kwargs):
    if created:
         
            stock=Stock() 
            if Stock.objects.all().filter(item=instance.items).exists():
                item=Stock.objects.get(item=instance.items)

                if item.issued_qty>item.current_qty:
                    #send alert
                    print("cannot issue")
                else:
                    stock.issued_qty=+item.issued_qty
                    item.current_qty=stock.current_qty-item.issued_qty
                    if item.current_qty>100:
                        item.status='In stock'
                    elif item.current_qty<=100:
                        item.status='Stock Running Low'
                        #send alert/email
                    else:
                        item.status='Out of stock'
                item.save()


post_save.connect(issue_stock,sender=TeamleaderRequest)

def returned_stock(sender,instance,created,**kwargs):
    if created:
         
            stock=Stock() 
            if Stock.objects.all().filter(item=instance.items).exists():
                item=Stock.objects.get(item=instance.items)
                stock.returned_qty=+item.returned_qty
                item.current_qty=stock.current_qty+item.returned_qty
                if item.current_qty>100:
                    item.status='In stock'
                elif item.current_qty<=100:
                    item.status='Stock Running Low'
                    #send alert/email
                else:
                    item.status='Out of stock'
                item.save()


post_save.connect(returned_stock,sender=TeamleadReturns)