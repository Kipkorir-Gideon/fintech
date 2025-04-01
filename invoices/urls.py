from django.urls import path
from .views import InvoiceCreateView, InvoiceListView



urlpatterns = [
    path('create-invoice/', InvoiceCreateView.as_view(), name='create_invoices'),
    path('list/', InvoiceListView.as_view(), name='invoices_list'),
]