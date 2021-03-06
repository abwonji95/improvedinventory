from inv.decorators import *
from django.core import serializers
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, UserCreationForm
from django.contrib.auth.views import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models import Count
from django.db.models.query_utils import Q
from .models import *
from .forms import *
from inv.forms import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .filters import *
from django.urls import reverse_lazy
import csv
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.views.generic import View


def sidebar(request):
    if request.user.groups.all()[0].name=='admin':
        group=admin
    elif request.user.groups.all()[1].name=='teamleader':
        group=teamleader_approval
    else :
        group=engineer
    context={'group':group }
    return render(request,'inv/sidebar.html',context)


def base(request):
    return render(request,'inv/base.html')


class Passwords_ChangeView(PasswordChangeView):
    form_class=ChangingPasswordForm
    success_url=reverse_lazy('password_success')

def password_reset_request(request):
    if request.method=="POST":
        form= PasswordResetForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data['email']
            user_email=User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject=" request password request "
                    email_template_name="inv/reset_password_email.html"
                    parameters={
                        'email':user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name':'BTN ',
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'token':default_token_generator.make_token(user),
                        'protocol':'http',


                    }
                    email=render_to_string(email_template_name,parameters)
                    try:
                        send_mail(subject,email,'',[user.email],fail_silently=False)
                    except:
                        return HttpResponse('Invalid Header')
                    return redirect('password_reset_done')
            else:
                messages.info(request,'Error! Email is does not Exist. .')
                return render(request,'inv/password_reset.html')
        else:
            messages.info(request,'Error! Email is not Valid ')
            return render(request,'inv/password_reset.html')

    else:
        form=PasswordResetForm()
        context={
            'form':form

        }
        return render (request,'inv/password_reset.html',context)


def password_reset_form(request):
    if request.method=='POST':
        form=ResetPasswordForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('loginpage')
        else:
            messages.info(request,'Passwords do not match .')
            return render(request,'inv/password_reset_form.html')
    else:
         form=ResetPasswordForm()

    context={
            'form':form}
    return render (request,'inv/password_reset_form.html',context)



def password_reset_done(request):
    return render(request,'inv/password_reset_done.html')

def password_success(request):
    return render(request,'inv/password_success.html')  

def test(request):
    return render(request,'inv/test.html')



def account_created(request):
    template=render_to_string('inv/account_created_email.html',{'name':request.user})
    email=EmailMessage(
        'Account Created ',
        template,
        settings.EMAIL_HOST_USER,
        ['ABWONJI95@OUTLOOK.COM']
    )
    email.fail_silently=False;
    email.send()
    
    return render(request,'inv/account_created_email.html')

def request_created(request):
    template=render_to_string('inv/request_created_email.html',{'name':request.user})
    email=EmailMessage(
        'Request Created ',
        template,
        settings.EMAIL_HOST_USER,
        ['ABWONJI95@OUTLOOK.COM']
    )
    email.fail_silently=False;
    email.send()
    
    return render(request,'inv/account_created_email.html')



@login_required(login_url='loginpage')
@admin_only
def vendorprice_list(request):
    list=VendorPrice.objects.all()
    return render(request,'inv/vendorprice_list.html',{'list':list})

@login_required(login_url='loginpage')
@admin_only
def vendorpriceform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=VendorPriceForm()
        else:
            vendorprice=VendorPrice.objects.get(pk=id)
            form=VendorPriceForm(instance=vendorprice)
        context={
                'form':form,
            }
        return render(request,'inv/vendorpriceform.html',context)
    else:
        if id==0:
            form=VendorPriceForm(request.POST)
        else:
           vendorprice=VendorPrice.objects.get(pk=id)
           form=VendorPriceForm(request.POST,instance=vendorprice)
        if form.is_valid():
            form.save()
        return redirect('/vendorprice_list')

@login_required(login_url='loginpage')
@admin_only
def viewvendorpriceform(request,id=0):
    if request.method=="GET":
        vendorprice=VendorPrice.objects.get(pk=id)
        item =  vendorprice.item
        price =  vendorprice.price
        vendor =  vendorprice.vendor
        date_created=vendorprice.date_created
        date_updated=vendorprice.date_updated
        list=VendorPrice.objects.all()

        context={
            
           'item':item ,
           'price':price,
           'vendor':vendor,
           'list':list,
            'date_created':date_created,
            'date_updated':date_updated,
          
            
        }
        return render(request,'inv/viewvendorpriceform.html',context)

@login_required(login_url='loginpage')
@admin_only
def vendorpricedelete(request,id):
    vendorprice=VendorPrice.objects.get(pk=id)
    vendorprice.delete()
    return redirect('/vendorprice_list')

@login_required(login_url='loginpage')
@admin_only
def admin_approval(request):
    return render(request,'inv/admin_approval.html')

@login_required(login_url='loginpage')
@admin_only
def admin_return(request):
    return render(request,'inv/admin_return.html')


@login_required(login_url='loginpage')
@admin_only
def admin_stock(request):
    list=Stock.objects.all()
    return render(request,'inv/admin_stock.html',{'list':list})


@login_required(login_url='loginpage')
@admin_only
def admin_report(request):
    return render(request,'inv/admin_report.html')


@login_required(login_url='loginpage')
def engineer_report(request):
    return render(request,'inv/engineer_report.html')

@login_required(login_url='loginpage')
def teamleader_report(request):
    return render(request,'inv/teamleader_report.html')


@login_required(login_url='loginpage')
def teamleader_request(request,id=0):
    if request.method=="GET":
        if id==0:
            form=TeamleaderRequestForm()
        else:
            myrequest=TeamleaderRequest.objects.get(pk=id)
            form=TeamleaderRequest(instance=myrequest)
        return render(request,'inv/teamleader_request.html',{'form':form})
    else:
        if id==0:
            form=TeamleaderRequest(request.POST)
        else:
           myrequest=TeamleaderRequest.objects.get(pk=id)
           form=TeamleaderRequestForm(request.POST,instance=myrequest)
        if form.is_valid():
            form.save()
       
    return render(request,'inv/teamleader_request_form.html')

@login_required(login_url='loginpage')
def teamleader_request_list(request):
    list=TeamleaderRequest.objects.all()
    return render(request,'inv/teamleader_request.html',{'list':list})


@login_required(login_url='loginpage')
def teamleader_approval(request):
    return render(request,'inv/teamleader_approval.html')


@login_required(login_url='loginpage')
def teamleader_stock(request):
    return render(request,'inv/teamleader_stock.html')

@login_required(login_url='loginpage')
def teamleader_return(request):
    return render(request,'inv/teamleader_return.html')

@login_required(login_url='loginpage')
def teamleader_make_return(request,id=0):
    if request.method=="GET":
        if id==0:
            form=TeamleadReturnsForm
        else:
            myreturn=TeamleadReturns.objects.get(pk=id)
            form=TeamleadReturnsForm(instance=myreturn)
        return render(request,'inv/teamleader_make_return.html',{'form':form})
    else:
        if id==0:
            form=TeamleadReturnsForm(request.POST)
        else:
           myrequest=TeamleadReturns.objects.get(pk=id)
           form=TeamleadReturnsForm(request.POST,instance=myreturn)
        if form.is_valid():
            form.save()
        return redirect('teamleader_return')
       
    return render(request,'inv/teamleader_make_return.html')

@login_required(login_url='loginpage')
def engineer_stock(request):
    return render(request,'inv/engineer_stock.html')

@login_required(login_url='loginpage')
def engineer_make_request(request,id=0):
    if request.method=="GET":
        if id==0:
            form=EngineerRequestForm()
        else:
            myrequest=EngineerRequest.objects.get(pk=id)
            form=EngineerRequest(instance=myrequest)
        return render(request,'inv/engineer_make_request.html',{'form':form})
    else:
        if id==0:
            form=EngineerRequest(request.POST)
        else:
           myrequest=EngineerRequest.objects.get(pk=id)
           form=EngineerRequestForm(request.POST,instance=myrequest)
           if form.is_valid():
                form.save()
                messages.info(request,'Request successful .')
                return render(request,'inv/engineer_dashboard.html')
        return redirect('engineer_dashboard')
       

    return render(request,'inv/engineer_make_request.html')


@login_required(login_url='loginpage')
def engineer_make_return(request,id=0):
    if request.method=="GET":
        if id==0:
            form=EngineerReturnsForm()
        else:
            myreturn=EngineerReturns.objects.get(pk=id)
            form=EngineerReturnsForm(instance=myreturn)
        return render(request,'inv/engineer_make_return.html',{'form':form})
    else:
        if id==0:
            form=EngineerReturnsForm(request.POST)
        else:
           myreturn=EngineerReturns.objects.get(pk=id)
           form=EngineerReturnsForm(request.POST,instance=myreturn)
           if form.is_valid():
                form.save()
                messages.info(request,'Return successful .')
                return render(request,'inv/engineer_dashboard.html')
        return redirect('engineer_dashboard')
       
    return render(request,'inv/engineer_make_return.html')


@login_required(login_url='loginpage')
def restricted(request):
    return render(request,'inv/restricted.html')


@login_required(login_url='loginpage')
def error_404(request):
    return render(request,'inv/error_404.html')

@login_required(login_url='loginpage')
def stock(request):
    list=Stock.objects.all()
    context={
        'list':list
    }
    return render(request,'inv/stock.html',context)

@login_required(login_url='loginpage')
def home(request):
    return render(request,'inv/admin_dashboard.html')

@login_required(login_url='loginpage')
def reports(request):
    return render(request,'inv/reports.html')

@login_required(login_url='loginpage')
def engineer_dashboard(request):
    return render(request,'inv/engineer_dashboard.html')

@login_required(login_url='loginpage')
def teamleader_dashboard(request):
    return render(request,'inv/teamleader_dashboard.html')

@login_required(login_url='loginpage')
def items(request):
    items=Item.objects.all()
    return render(request,'inv/products.html',{'items':items})

@login_required(login_url='loginpage')
def accounts(request):
    users=User.objects.all()
    return render(request,'inv/accounts.html',{'users':users})
   
@login_required(login_url='loginpage')
def purchases(request):
    purchases=Purchase.objects.all()

    return render(request,'inv/purchases.html',{'purchases':purchases})


@login_required(login_url='loginpage')
def vendors(request):
    vendors = Vendor.objects.all()
    return render(request,'inv/vendors.html',{'vendors':vendors})

@login_required(login_url='loginpage')
def issuance(request):
    issuances = Issuance.objects.all()
    return render(request,'inv/issuance.html',{'issuances':issuances})

@login_required(login_url='loginpage')
def stores(request):
    stores = Store.objects.all()
    return render(request,'inv/stores.html',{'stores':stores})

def logout_view(request):
    logout(request)
    return redirect('loginpage')


@login_required(login_url='loginpage')
def purchases_card(request):
    purchases_recent=Purchase.objects.all()[:5]
    return render(request,'inv/purchases_card.html',{'purchases_recent':purchases_recent})

@login_required(login_url='loginpage')
def engineer_cards(request):
    return render(request,'inv/engineer_cards.html')

@login_required(login_url='loginpage')
def teamleader_cards(request):
    return render(request,'inv/teamleader_cards.html')


@login_required(login_url='loginpage')
@admin_only
def admin_dashboard(request):
    
    engineerscount=Engineer.objects.all().count()
    vendorscount=Vendor.objects.all().count()
    userscount=User.objects.all().count()
    users=User.objects.all().count()
    stores=Store.objects.all().count()
    purchases_recent=Purchase.objects.all()[:5]

    mydict={
    'engineers':engineers,
    'vendors':vendors,
    'vendorscount':vendorscount,
    'engineerscount':engineerscount,
    'userscount':userscount,
    'users':users,
    'purchases_recent':purchases_recent,
    'store':stores,
    
    }
    return render(request,'inv/admin_dashboard.html',context=mydict)

@login_required(login_url='loginpage')
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('admin_dashboard')
        else:
            messages.info(request,'username or password incorect')
            return render(request,'inv/loginpage.html')
    context={}
    return render(request,'inv/loginpage.html',context)


@login_required(login_url='loginpage')
@admin_only
def engineers(request):
    engineers = Engineer.objects.all()
    engineercount = Engineer.objects.count()
    engineer_tm=Engineer.objects.all().filter(role='Team leader')
    engineer_en=Engineer.objects.all().filter(role='Engineer')
    return render(request,'inv/engineers.html',{'engineers':engineers,
    'engineercount':engineercount,'engineer_tm':engineer_tm,'engineer_en':engineer_en})





@unauthenticated_user
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('admin_dashboard')
            else:
                messages.info(request,'Email or Password Incorrect .')
                return render(request,'inv/loginpage.html')
        
    context={}
    return render(request,'inv/loginpage.html',context)


@login_required(login_url='loginpage')
@admin_only
def engineerlist(request):
    list=Engineer.objects.all()
    context={
        'list':list
    }
    return render(request,'inv/engineers.html',context)

@login_required(login_url='loginpage')
@admin_only
def viewengineer(request,id=0):
    if request.method=="GET":
        engineer=Engineer.objects.get(pk=id)
        first_name=engineer.first_name
        last_name=engineer.last_name
        empnumber=engineer.employee_number
        email=engineer.email
        phone=engineer. phone
        role=engineer.role
        date_created=engineer.date_created
        date_updated=engineer.date_updated

        context={
            'first_name':first_name,
            'last_name':last_name,
            'employee_number':empnumber,
            'email':email,
            'phone': phone,
           'role':role,
            'date_created':date_created ,
            'date_updated':date_updated ,
            
        }
        return render(request,'inv/viewengineerform.html',context)



@login_required(login_url='loginpage')
@admin_only
def engineerform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=EngineerForm()
        else:
            engineer=Engineer.objects.get(pk=id)
            form=EngineerForm(instance=engineer)
        return render(request,'inv/engineer_form.html',{'form':form})
    else:
        if id==0:
            form=EngineerForm(request.POST)
        else:
           engineer=Engineer.objects.get(pk=id)
           form=EngineerForm(request.POST,instance=engineer)
        if form.is_valid():
            form.save()
        return redirect('/engineerlist')

@login_required(login_url='loginpage')
@admin_only
def engineerdelete(request,id):
    eng=Engineer.objects.get(pk=id)
    eng.delete()
    return redirect('/engineerlist')

@login_required(login_url='loginpage')
@admin_only
def vendorlist(request):
    list=Vendor.objects.all()
    return render(request,'inv/vendors.html',{'list':list})

@login_required(login_url='loginpage')
@admin_only
def viewvendor(request,id=0):
    if request.method=="GET":
        vendor=Vendor.objects.get(pk=id)
        name =  vendor.name
        items=vendor.items.all
    
        shippingaddress =  vendor.shipping_address
        billingaddress=  vendor.billing_address
        phone=  vendor.phone
        website=vendor.website
        email=vendor.email
        primarycontactperson=vendor.primary_contact_person
        otherdetails=vendor.other_details
        date_created=vendor.date_created
        date_updated=vendor.date_updated
        list=Vendor.objects.all()

        context={
            
           'name':name ,
           'list':list,
           'shippingaddress': shippingaddress ,
           'billingaddress':billingaddress ,
           'phone':phone,
           'website': website,
           'items':items,
           'email':email,
           'primarycontactperson': primarycontactperson,
           'otherdetails':otherdetails,
           'date_created':date_created,
           'date_updated':date_updated,
            
        }
        return render(request,'inv/viewvendorform.html',context)

@login_required(login_url='loginpage')
@admin_only
def vendorform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=VendorForm()
        else:
            vendor=Vendor.objects.get(pk=id)
            form=VendorForm(instance=vendor)
        return render(request,'inv/vendorform.html',{'form':form})
    else:
        if id==0:
            form=VendorForm(request.POST)
        else:
           vendor=Vendor.objects.get(pk=id)
           form=VendorForm(request.POST,instance=vendor)
        if form.is_valid():
            form.save()
            print("valid")
        else:
            print("invalid")
        
        return redirect('/vendorslist')



@login_required(login_url='loginpage')
@admin_only
def vendordelete(request,id):
    vendor=Vendor.objects.get(pk=id)
    vendor.delete()
    return redirect('/vendorslist')

@login_required(login_url='loginpage')
@admin_only
def userslist(request):
    list=User.objects.all()
    return render(request,'inv/accounts.html',{'list':list})

@login_required(login_url='loginpage')
@admin_only
def register(request,id=0):
    if request.method=="GET":
        if id==0:
            form=CreateUserForm()
        else:
            user=User.objects.get(pk=id)
            form=CreateUserForm(instance=user)
        return render(request,'inv/register.html',{'form':form})
    else:
        if id==0:
            form=CreateUserForm(request.POST)
        else:
           user=User.objects.get(pk=id)
           form=CreateUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            account_created(request)
            print('email sent')
            messages.info(request,'User was Created Successfully')
        else:
            print('email NOT sent')
            messages.info(request,'Error check the details and try again')
            return redirect('/register')
        return redirect('/')


@login_required(login_url='loginpage')
@admin_only
def userdelete(request,id):
    user=User.objects.get(pk=id)
    user.delete()
    return redirect('/')


@login_required(login_url='loginpage')
@admin_only
def storeslist(request):
    list=Store.objects.all()
    return render(request,'inv/stores.html',{'list':list})

@login_required(login_url='loginpage')
@admin_only
def viewstore(request,id=0):
    if request.method=="GET":
        store=Store.objects.get(pk=id)
        name=store.name
        engineer=store.engineer
        date_created=store.date_created
        date_updated=store.date_updated

        context={
            'name':name,
            'engineer':engineer,
            'date_created':date_created ,
            'date_updated':date_updated ,
            
        }
        return render(request,'inv/viewstoreform.html',context)


@login_required(login_url='loginpage')
#@allowed_users(allowed_roles=['admin'])
def storeform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=StoreForm()
        else:
            store=Store.objects.get(pk=id)
            form=StoreForm(instance=store)
        return render(request,'inv/storeform.html',{'form':form})
    else:
        if id==0:
            form=StoreForm(request.POST)
        else:
           store=Store.objects.get(pk=id)
           form=StoreForm(request.POST,instance=store)
        if form.is_valid():
            form.save()
        return redirect('/storeslist')

@login_required(login_url='loginpage')
#@allowed_users(allowed_roles=['admin'])
def storedelete(request,id):
    store=Store.objects.get(pk=id)
    store.delete()
    return redirect('/storeslist')

@login_required(login_url='loginpage')
#@allowed_users(allowed_roles=['admin'])

def itemslist(request):
    list=Item.objects.all()
    return render(request,'inv/items.html',{'list':list})

@login_required(login_url='loginpage')
#@allowed_users(allowed_roles=['admin'])
def viewitems(request,id=0):
    if request.method=="GET":
        item=Item.objects.get(pk=id)
        name=item.name
        units=item.units
        description=item.item_description
        date_created=item.date_created
        date_updated=item.date_updated

        context={
            'name':name,
            'units':item.units,
            'description':description ,
            'date_created':date_created ,
            'date_updated':date_updated ,
            
        }
        return render(request,'inv/viewitemsform.html',context)


@login_required(login_url='loginpage')
#@allowed_users(allowed_roles=['admin'])
def itemform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=ItemForm()
        else:
            item=Item.objects.get(pk=id)
            form=ItemForm(instance=item)
        return render(request,'inv/itemform.html',{'form':form})
    else:
        if id==0:
            form=ItemForm(request.POST)
        else:
           item=Item.objects.get(pk=id)
           form=ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('/itemslist')

@login_required(login_url='loginpage')
#@allowed_users(allowed_roles=['admin'])
def itemdelete(request,id):
    item=Item.objects.get(pk=id)
    item.delete()
    return redirect('/itemslist')




@login_required(login_url='loginpage')
@admin_only
def purchaseslist(request):
    list=Purchase.objects.all()

    myFilter=PurchaseFilter(request.GET,queryset=list)
    list=myFilter.qs
    context={'myFilter':myFilter ,'list':list  }

    return render(request,'inv/purchases.html',context)

@login_required(login_url='loginpage')
@admin_only
def viewpurchase(request,id=0):
    if request.method=="GET":
        purchase=Purchase.objects.get(pk=id)
        items=purchase.items
        po=purchase.po
        vendor=purchase.vendor
        purchased_qty=purchase.purchased_qty
        price=purchase.price
        date_created=purchase.date_created
        date_updated=purchase.date_updated

        context={
            'items':items,
            'po': po,
            'vendor': vendor,
            'purchased_qty':purchased_qty ,
            'price': price,
            
            'date_created':date_created ,
            'date_updated':date_updated ,
            


        }
        return render(request,'inv/viewpurchaseform.html',context)

@login_required(login_url='loginpage')
@admin_only
def purchaseform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=PurchaseForm()
        else:
            purchase=Purchase.objects.get(pk=id)
            form=PurchaseForm(instance=purchase)
        return render(request,'inv/purchaseform.html',{'form':form})
    else:
        if id==0:
            form=PurchaseForm(request.POST)
        else:
           purchase=Purchase.objects.get(pk=id)
           form=PurchaseForm(request.POST,instance=purchase)
        if form.is_valid():
    
            form.save()

            messages.success(request,'Purchase  Created Successfully')
            return redirect('/purchaseslist')

        else:
            messages.warning(request,'Error check the details and try again')
            return redirect('/purchases')





@login_required(login_url='loginpage')
@admin_only
def purchasedelete(request,id):
    purchase=Purchase.objects.get(pk=id)
    if request.method=='POST':
        purchase.delete()
        return redirect('/purchaseslist')
    return render(request,'inv/purchase_delete.html')

@login_required(login_url='loginpage')
@admin_only
def issuancelist(request):
    list=Issuance.objects.all()
    return render(request,'inv/issuance.html',{'list':list})

@login_required(login_url='loginpage')
@admin_only
def viewissuance(request,id=0):
    if request.method=="GET":
        issuance=Issuance.objects.get(pk=id)
        issued_to=  issuance.issued_to
        item=  issuance.item
        issued_qty=  issuance.issued_qty
        store= issuance.store
        date_created=  issuance.date_created
        date_updated=  issuance.date_updated

        context={
            
            'issued_to':issued_to,
            'item': item,
            'store':store,
            'issued_qty':issued_qty,
            'date_created':date_created ,
            'date_updated':date_updated ,
            
        }
        return render(request,'inv/viewissuanceform.html',context)

@login_required(login_url='loginpage')
@admin_only
def issuanceform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=IssuanceForm()
        else:
            issuance=Issuance.objects.get(pk=id)
            form=IssuanceForm(instance=issuance)
        return render(request,'inv/issuanceform.html',{'form':form})
    else:
        if id==0:
            form=IssuanceForm(request.POST)
        else:
           issuance=Issuance.objects.get(pk=id)
           form=IssuanceForm(request.POST,instance=issuance)
        if form.is_valid():
            form.save()
        return redirect('/issuancelist')

@login_required(login_url='loginpage')
@admin_only
def issuancedelete(request,id):
    issuance=Issuance.objects.get(pk=id)
    if request.method=='POST':
        issuance.delete()
        return redirect('/issuancelist')
    return render(request,'inv/issuance_delete.html')


@login_required(login_url='loginpage')
@admin_only
def returneditemslist(request):
    list=Returneditems.objects.all()
    return render(request,'inv/returneditems.html',{'list':list})

@login_required(login_url='loginpage')
@admin_only
def viewreturneditems(request,id=0):
    if request.method=="GET":
        returneditem=Returneditems.objects.get(pk=id)
        returnedby= returneditem.returnedby
        item= returneditem.item
        returnedqty= returneditem.returnedqty
        store=returneditem.store
        date_created= returneditem.date_created
        date_updated= returneditem.date_updated

        context={
            
            'returnedby':returnedby,
            'item': item,
            'store':store,
            'returnedqty':returnedqty,
            'date_created':date_created ,
            'date_updated':date_updated ,
        }
        return render(request,'inv/viewreturneditemsform.html',context)

@login_required(login_url='loginpage')
@admin_only
def returneditemsdelete(request,id):
    if request.method=='POST':
        returneditems=Returneditems.objects.get(pk=id)
        returneditems.delete()
        return redirect('/returneditems_list')
    return render(request,'inv/returneditems_delete.html')

@login_required(login_url='loginpage')
def returneditemsform(request,id=0):
    if request.method=="GET":
        if id==0:
            form=ReturneditemsForm()
        else:
            returneditems=Returneditems.objects.get(pk=id)
            form=ReturneditemsForm(instance=returneditems)
        return render(request,'inv/returneditemsform.html',{'form':form})
    else:
        if id==0:
            form=ReturneditemsForm(request.POST)
        else:
           returneditems=Returneditems.objects.get(pk=id)
           form=ReturneditemsForm(request.POST,instance=returneditems)
        if form.is_valid():
            form.save()
        return redirect('/returneditemslist')


         

