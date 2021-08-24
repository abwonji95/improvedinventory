from django.urls import path
from  . import views
from .views import *
from django.conf.urls import url

urlpatterns=[
    path('',views.home,name='home'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('engineer_dashboard/',views.engineer_dashboard,name='engineer_dashboard'),
    path('teamleader_dashboard/',views.teamleader_dashboard,name='teamleader_dashboard'),


    path('products/',views.products,name='products'),
    path('stock/',views.stock,name='stock'),
    path('register/',views.register,name='register'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('logoutpage/',views.logoutpage,name='logoutpage'),
    path('engineers/',views.engineers,name='engineers'),
    path('create_engineer/',views.create_engineer,name='create_engineer'),
    path('engineer/<id>/update',views.update_engineer,name='update_engineer'),
    path('engineer/<id>/delete',views.delete_engineer,name='delete_engineer'),

    

    path('purchases/',views.purchases,name='purchases'),
    path('requests/',views.requests,name='requests'),
    path('issuance/',views.issuance,name='issuance'),
    path('teamleader_issuance/',views.teamleader_issuance,name='teamleader_issuance'),
    path('vendors/',views.vendors,name='vendors'),
    path('accounts/',views.accounts,name='accounts'),
    path('stores/',views.stores,name='stores'),

    
    path('create_vendor/',views.create_vendor,name='create_vendor'),
    path('create_store/',views.create_store,name='create_store'),
    path('create_product/',views.create_product,name='create_product'),
    path('create_account/',views.register,name='create_account'),
    path('create_issuance/',views.create_issuance,name='create_issuance'),
    path('create_purchase/',views.create_purchase,name='create_purchase'),
    path('request_product_tm/',views.request_product_tm,name='request_product_tm'),
    path('request_product_en/',views.request_product_en,name='request_product_en'),







]