from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import *
from .forms import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def main(request):
    return render(request,'inv/main.html')
def main2(request):
    return render(request,'inv/main2.html')
def main3(request):
    return render(request,'inv/main3.html')
def home(request):
    return render(request,'inv/main.html')

@login_required(login_url='loginpage')
def admin_dashboard(request):
    
    engineers=Engineer.objects.all().order_by('-id')
    vendors=Vendor.objects.all().order_by('-id')
    engineerscount=Engineer.objects.all().count()
    vendorscount=Vendor.objects.all().count()
    userscount=User.objects.all().count()
    users=User.objects.all().count()

    mydict={
    'engineers':engineers,
    'vendors':vendors,
    'vendorscount':vendorscount,
    'engineerscount':engineerscount,
    'userscount':userscount,
    'users':users,
    
    }
    return render(request,'inv/admin_dashboard.html',context=mydict)
@login_required(login_url='loginpage')
def engineer_dashboard(request):
    return render(request,'inv/engineer_dashboard.html')

@login_required(login_url='loginpage')
def teamleader_dashboard(request):
    return render(request,'inv/teamleader_dashboard.html')

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

@login_required(login_url='loginpage')
def products(request):
    products=Product.objects.all()
    return render(request,'inv/products.html',{'products':products})


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
def stores(request):
    stores = Store.objects.all()
    return render(request,'inv/stores.html',{'stores':stores})

@login_required(login_url='loginpage')
def requests(request):
    return render(request,'inv/requests.html')

@login_required(login_url='loginpage')
def teamleader_request(request):
    return render(request,'inv/teamleader_request.html')

@login_required(login_url='loginpage')
def teamleader_issuance(request):
    return render(request,'inv/teamleader_issuance.html')
@login_required(login_url='loginpage')
def issuance(request):
    issuances = Issuance.objects.all()
    return render(request,'inv/issuance.html',{'issuances':issuances})

@login_required(login_url='loginpage')
def create_engineer(request):

    form =EngineerForm()
    if request.method=='POST':
        form =EngineerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('engineers')
    context={'form':form}
    return render(request,'inv/engineer_form.html',context)

@login_required(login_url='loginpage')
def create_vendor(request):

    form =VendorForm()
    if request.method=='POST':
        form =VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendors')
    context={'form':form}
    return render(request,'inv/create_vendor.html',context)

@login_required(login_url='loginpage')
def create_store(request):

    form =StoreForm()
    if request.method=='POST':
        form =StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stores')
    context={'form':form}
    return render(request,'inv/create_store.html',context)

@login_required(login_url='loginpage')
def create_product(request):

    form =ProductForm()
    if request.method=='POST':
        form =ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context={'form':form}
    return render(request,'inv/create_product.html',context)


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
    return render(request,'inv/create_issuance_tm.html',context)



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

@login_required(login_url='loginpage')
def teamleader_request(request):

    form =RequestForm()
    if request.method=='POST':
        form =RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teamleader_request')
    context={'form':form}
    return render(request,'inv/create_request_tm.html',context)

@login_required(login_url='loginpage')
def engineer_request(request):

    form =RequestForm()
    if request.method=='POST':
        form =RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('engineer_request')
    context={'form':form}
    return render(request,'inv/create_request_eng.html',context)



@login_required(login_url='loginpage')
def register(request):

    form=CreateUserForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for'+ user )
            return redirect('admin_dashboard')
    context={'form':form}
    return render (request,'inv/register.html',context)


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

def logoutpage(request):
    user=authenticate(request)
    if request.method=='POST':
        logout(request)
        messages.info(request,'you have been logged out successfully')
    return redirect('loginpage')

@login_required(login_url='loginpage')
def request_product_tm(request):
    return render(request,'inv/request_product_tm.html')

@login_required(login_url='loginpage')
def request_product_en(request):
    return render(request,'inv/request_product_en.html')
# Create your views here.

@login_required(login_url='loginpage')
def update_engineer(request,id):
	queryset = Engineer.objects.get_object_or_404(id=id)
	form = EngineerUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = EngineerUpdateForm(request.POST or None, instance=queryset)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("engineers"+id)

	context = {
		'form':form
	}
	return render(request, 'create_engineer', context)

@login_required(login_url='loginpage')
def delete_engineer(request, id):
	queryset = Engineer.objects.get(id=id)
	if request.method == 'POST':
		queryset.delete()
		return redirect('engineers'+ id)
	return render(request, 'inv/delete_engineer.html')

def stock(request):
    purchases=Purchase.objects.all()
    #issued=Issuance.objects.get()
    return render(request,'inv/stock.html',{'purchases':purchases})

def delete_all(request):
    queryset = Engineer.objects.all()
    if request.method=='POST':
        queryset.delete()
        return redirect('engineers')
    return render(request,'inv/delete_all.html')

