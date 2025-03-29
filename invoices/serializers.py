from rest_framework import serializers
from .models import Invoice



class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'amount', 'currency', 'status', 'due_date', 'recipient_email', 'created_at']