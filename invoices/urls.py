from django.urls import path
from .views import InvoiceCreateView, InvoiceListView



urlpatterns = [
    path('create/', InvoiceCreateView.as_view(), name='create_invoices'),
    path('invoices/', InvoiceListView.as_view(), name='invoices_list'),
]