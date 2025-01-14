from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('pending_order/', views.pending_order, name='pending_order'),
    path('accepted/', views.accepted, name='accepted'),
    path('pending_view_order/<int:order_filter>', views.pending_view_order, name='pending_view_order'),
    path('accepted_view_order/<int:order_filter>', views.accepted_view_order, name='accepted_view_order'),
    path('download_invoice/<int:order_filter>', views.download_invoice, name="download_invoice"),
]