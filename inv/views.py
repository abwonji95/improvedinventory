from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, UserCreationForm
from django.contrib.auth.views import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import *
from .forms import *
from inv.forms import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .filters import *
from django.urls import reverse_lazy




def main(request):
    return render(request,'inv/main.html')
def main2(request):
    return render(request,'inv/main2.html')
def main3(request):
    return render(request,'inv/main3.html')
def home(request):
    return render(request,'inv/main.html')
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

def logoutpage(request):
    user=authenticate(request)
    if request.method=='POST':
        logout(request)
        messages.info(request,'you have been logged out successfully')
    return redirect('loginpage')

def stock(request):
    purchases=Purchase.objects.all()
    #issued=Issuance.objects.get()
    return render(request,'inv/stock.html',{'purchases':purchases})

def purchases_card(request):
    purchases_recent=Purchase.objects.all()[:5]
    return render(request,'inv/purchases_card.html',{'purchases_recent':purchases_recent})

def engineer_cards(request):
    return render(request,'inv/engineer_cards.html')
def teamleader_cards(request):
    return render(request,'inv/teamleader_cards.html')


@login_required(login_url='loginpage')
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
def engineers(request):
    engineers = Engineer.objects.all()
    engineercount = Engineer.objects.count()
    engineer_tm=Engineer.objects.all().filter(role='Team leader')
    engineer_en=Engineer.objects.all().filter(role='Engineer')
    return render(request,'inv/engineers.html',{'engineers':engineers,
    'engineercount':engineercount,'engineer_tm':engineer_tm,'engineer_en':engineer_en})

def cards(request):
    purchases_recent=Purchase.objects.all()[:5]
    stores=Store.objects.all().count()
    itemscount=Item.objects.all().count()
    vendorscount = Vendor.objects.all().count()
    purchasescount=Purchase.objects.all().count()
    users=User.objects.all().count()
    engineercount = Engineer.objects.all().count()
    context={'itemscount':itemscount,'vendorscount':vendorscount,  'purchases_recent' : purchases_recent,
    'purchasescount':purchasescount,'users':users,'engineercount':engineercount, 'stores':stores}
    return render(request,'inv/cards.html',context)

@login_required(login_url='loginpage')
def teamleader_issuance(request):
    form =TeamleaderissuanceForm
    if request.method=='POST':
        form =TeamleaderissuanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teamleader_dashboard')
    context={'form':form}
    return render(request,'inv/teamleader_issuance.html',context)


@login_required(login_url='loginpage')
def create_issuance(request):

    form =IssuanceForm()
    if request.method=='POST':
        form =IssuanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issuance')
    context={'form':form}
    return render(request,'inv/create_issuance.html',context)


@login_required(login_url='loginpage')
def create_issuance_tm(request):
    form =TeamleaderissuanceForm()
    if request.method=='POST':
        form =TeamleaderissuanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issuance_tm')
    context={'form':form}
    return render(request,'inv/teamleader_issuance.html',context)



@login_required(login_url='loginpage')
def create_purchase(request):

    form =PurchaseForm()
    if request.method=='POST':
        form =PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock')
    context={'form':form}
    return render(request,'inv/create_purchase.html',context)





def loginpage(request):
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

# Create your views here.

def delete_all(request):
    queryset = Engineer.objects.all()
    if request.method=='POST':
        queryset.delete()
        return redirect('engineers')
    return render(request,'inv/delete_all.html')

#new


def engineerlist(request):
    list=Engineer.objects.all()
    context={
        'list':list
    }
    return render(request,'inv/engineers.html',context)


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

def engineerdelete(request,id):
    employee=Engineer.objects.get(pk=id)
    employee.delete()
    return redirect('/engineerlist')


def vendorlist(request):
    list=Vendor.objects.all()
    return render(request,'inv/vendors.html',{'list':list})


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
        return redirect('/vendorslist')

def vendordelete(request,id):
    vendor=Vendor.objects.get(pk=id)
    vendor.delete()
    return redirect('/vendorslist')



def userslist(request):
    list=User.objects.all()
    return render(request,'inv/accounts.html',{'list':list})


def register(request,id=0):
    if request.method=="GET":
        if id==0:
            form=UserCreationForm()
        else:
            user=User.objects.get(pk=id)
            form=UserCreationForm(instance=user)
        return render(request,'inv/register.html',{'form':form})
    else:
        if id==0:
            form=UserCreationForm(request.POST)
        else:
           user=User.objects.get(pk=id)
           form=UserCreationForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/accounts')

def userdelete(request,id):
    user=User.objects.get(pk=id)
    user.delete()
    return redirect('/accounts')



def storeslist(request):
    list=Store.objects.all()
    return render(request,'inv/stores.html',{'list':list})


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

def storedelete(request,id):
    store=Store.objects.get(pk=id)
    store.delete()
    return redirect('/storeslist')


def itemslist(request):
    list=Item.objects.all()
    return render(request,'inv/items.html',{'list':list})


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

def itemdelete(request,id):
    item=Item.objects.get(pk=id)
    item.delete()
    return redirect('/itemslist')

def sidebar(request):
    return render(request,'inv/sidebar.html')
    
def purchaseslist(request):
    list=Purchase.objects.all()
    return render(request,'inv/purchases.html',{'list':list})


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
        return redirect('/purchaseslist')

def purchasedelete(request,id):
    purchase=Purchase.objects.get(pk=id)
    purchase.delete()
    return redirect('/purchaseslist')

    
def issuancelist(request):
    list=Issuance.objects.all()
    return render(request,'inv/issuance.html',{'list':list})


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

def issuancedelete(request,id):
    issuance=Issuance.objects.get(pk=id)
    issuance.delete()
    return redirect('/issuancelist')


def returneditems(request):
    return render (request,'inv/returneditems.html')

   
def returneditemslist(request):
    list=Returneditems.objects.all()
    return render(request,'inv/returneditems.html',{'list':list})


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

def returneditemsdelete(request,id):
    returneditems=Issuance.objects.get(pk=id)
    returneditems.delete()
    return redirect('/returneditemslist')