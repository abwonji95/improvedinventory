from django.urls import path
from  . import views
from .views import PasswordsChangeView
from django.conf.urls import url
from django.contrib.auth import views as auth_views


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
    path('issuance/',views.issuance,name='issuance'),
    path('teamleader_issuance/',views.teamleader_issuance,name='teamleader_issuance'),
    path('vendors/',views.vendors,name='vendors'),
    path('accounts/',views.accounts,name='accounts'),
    path('stores/',views.stores,name='stores'),
    path('delete_all/',views.delete_all,name='delete_all'),

    path('create_vendor/',views.create_vendor,name='create_vendor'),
    path('create_return_en/',views.create_return_en,name='create_return_en'),
    path('create_request_en/',views.create_request_en,name='create_request_en'),
    path('create_store/',views.create_store,name='create_store'),
    path('create_product/',views.create_product,name='create_product'),
    path('create_account/',views.register,name='create_account'),
    path('create_issuance/',views.create_issuance,name='create_issuance'),
    path('create_purchase/',views.create_purchase,name='create_purchase'),
    path('request_product_tm/',views.request_product_tm,name='request_product_tm'),
    path('request_product_en/',views.request_product_en,name='request_product_en'),
    path('cards/',views.cards,name='cards'),
    path('purchases_card/',views.purchases_card,name='purchases_card'),
    path('engineer_cards/',views.engineer_cards,name='engineer_cards'),
    path('teamleader_cards/',views.teamleader_cards,name='teamleader_cards'),
    

    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

#path('password/',auth_views.PasswordChangeView.as_view(template_name='inv/changepassword.html')),
path('password/',views.PasswordsChangeView.as_view(template_name='inv/changepassword.html')),
path('password_change_done/',auth_views.PasswordChangeDoneView.as_view()),




]