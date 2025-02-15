from django.urls import path
from . import views

urlpatterns = [
    path('owner_home/', views.owner_home, name='owner_home'),  # New URL pattern
    path('item/', views.item, name='item'),
    path('category/', views.category, name='category'),
    path('item_detail/<int:id>/', views.item_detail, name='item_detail'),
    path('print_address/', views.print_address, name='print_address'),
    path('print_bill_customer_address/<int:order_filter>', views.print_bill_customer_address, name='print_bill_customer_address'),

]