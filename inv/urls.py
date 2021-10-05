from collections import namedtuple
from django.urls import path,include
from  . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns=[

#home
    path('',views.home,name='home'),
 

#stock
    path('stock/',views.stock,name='stock'),
    path('reports/',views.reports,name='reports'),

#engineer actions
    path('engineer_dashboard/',views.engineer_dashboard,name='engineer_dashboard'),
    path('engineers/',views.engineerform,name='engineer_insert'),
    path('engineers/<int:id>/',views.engineerform,name='engineer_update'),
    path('engineers/delete/<int:id>',views.engineerdelete,name='engineer_delete'),
    path('engineerlist/',views.engineerlist,name='engineer_list'),
    path('engineer_cards/',views.engineer_cards,name='engineer_cards'),
    path('engineers/view/<int:id>/',views.viewengineer,name='engineer_view'),
#teamleader actions

    path('teamleader_dashboard/',views.teamleader_dashboard,name='teamleader_dashboard'),
    path('teamleader_cards/',views.teamleader_cards,name='teamleader_cards'),
#vendor actions
    path('vendors/view/<int:id>/',views.viewvendor,name='vendor_view'),
    path('vendors/',views.vendorform,name='vendor_insert'),
    path('vendors/m/',views.vendorform,name='vendor_multiple'),
    path('vendors/<int:id>/',views.vendorform,name='vendor_update'),
    path('vendors/delete/<int:id>',views.vendordelete,name='vendor_delete'),
    path('vendorslist/',views.vendorlist,name='vendor_list'),
   

#admin actions
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('register/',views.register,name='register'),
    path('users/<int:id>/',views.register,name='user_update'),
    path('users/delete/<int:id>',views.userdelete,name='user_delete'),
    path('userslist/',views.userslist,name='userslist'),

#store actions
    path('stores/view/<int:id>/',views.viewstore,name='store_view'),
    path('store/',views.storeform,name='store_insert'),
    path('store/<int:id>/',views.storeform,name='store_update'),
    path('store/delete/<int:id>',views.storedelete,name='store_delete'),
    path('storeslist/',views.storeslist,name='storeslist'),

#product actions
    path('items/view/<int:id>/',views.viewitems,name='items_view'),
    path('items/',views.itemform,name='item_insert'),
    path('items/<int:id>/',views.itemform,name='item_update'),
    path('items/delete/<int:id>',views.itemdelete,name='item_delete'),
    path('itemslist/',views.itemslist,name='item_list'),


#purchases actions
    path('purchases/view/<int:id>/',views.viewpurchase,name='purchase_view'),
    path('purchases/',views.purchaseform,name='purchase_insert'),
    path('purchases/<int:id>/',views.purchaseform,name='purchase_update'),
    path('purchases/delete/<int:id>',views.purchasedelete,name='purchase_delete'),
    path('purchaseslist/',views.purchaseslist,name='purchase_list'),
    path('purchases_card/',views.purchases_card,name='purchases_card'),


#issuance for admin
    path('issuance/view/<int:id>/',views.viewissuance,name='issuance_view'),
    path('issuance/',views.issuanceform,name='issuance_insert'),
    path('issuance/<int:id>/',views.issuanceform,name='issuance_update'),
    path('issuance/delete/<int:id>',views.issuancedelete,name='issuance_delete'),
    path('issuancelist/',views.issuancelist,name='issuance_list'),

  

#returneditems for admin
    path('returneditems/view/<int:id>/',views.viewreturneditems,name='returneditems_view'),
    path('returneditems/',views.returneditemsform,name='returneditems_insert'),
    path('returneditems/<int:id>/',views.returneditemsform,name='returneditems_update'),
    path('returneditems/delete/<int:id>',views.returneditemsdelete,name='returneditems_delete'),
    path('returneditemslist/',views.returneditemslist,name='returneditems_list'),


    path('accounts/', include('django.contrib.auth.urls')),
   #common actions
    path('loginpage/',views.loginpage,name='loginpage'),
    path('logoutpage/',views.logout_view,name='logout_view'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view()),
    path('sidebar/',views.sidebar,name='sidebar'),
    path('base/',views.base,name='base'),

    #new
    path('price_list/',views.price_list,name='price_list'),
    path('vendorpriceform/',views.vendorpriceform,name='vendorpriceform'),
    path('admin_approval/',views.admin_approval,name='admin_approval'),
    path('admin_return/',views.admin_return,name='admin_return'),
    path('admin_stock/',views.admin_stock,name='admin_stock'),
    path('admin_report/',views.admin_report,name='admin_report'),
    path('teamleader_request/',views.teamleader_request,name='teamleader_request'),
    path('teamleader_request_list/',views.teamleader_request_list,name='teamleader_request_list'),
    path('teamleader_stock/',views.teamleader_stock,name='teamleader_stock'),
    path('teamleader_approval/',views.teamleader_approval,name='teamleader_approval'),
    path('teamleader_return/',views.teamleader_return,name='teamleader_return'),
    path('teamleader_make_return/',views.teamleader_make_return,name='teamleader_make_return'),
    path('engineer_stock/',views.engineer_stock,name='engineer_stock'),
    path('engineer_request/',views.engineer_request,name='engineer_request'),
    path('engineer_make_return/',views.engineer_make_return,name='engineer_make_return'),
    path('restricted/',views.restricted,name='restricted'),
    path('error_404/',views.error_404,name='error_404'),

]