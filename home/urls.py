from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cancellations_and_refunds/', views.cancellations_and_refunds, name='cancellations_and_refunds'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('view_customer_order/<int:order_filter>', views.view_customer_order, name='view_customer_order'),
    path('order/', views.order, name='order'),
    path('item_details/<int:id>', views.item_details, name='item_details'),
    path('contact_us/', views.contact_us_view, name='contact_us'),
    path('shipping-policy/', views.shipping_policy_view, name='shipping_policy'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions_view, name='terms_and_conditions'),
]