from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Invoice
from .serializers import InvoiceSerializer
import uuid


class InvoiceCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data.copy()
        data['invoice_number'] = str(uuid.uuid4())[:8].upper()
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class InvoiceListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        invoices = Invoice.objects.filter(user=request.user).order_by('-created_at')
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
