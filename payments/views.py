import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from core.models import Transaction
from .serializers import PaymentSerializer


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            api_key = settings.PAYMENT_API_KEY
            data = {
                'amount': str(serializer.validated_data['amount']),
                'currency': serializer.validated_data['currency'],
                'source': serializer.validated_data['source']
            }
            
            response = request.post(
                'https://api.paymentprovider.com/charges',
                data=data,
                headers={'Authorization': f'Bearer {api_key}'}
            )
            
            if response.status_code == 200:
                Transaction.objects.create(
                    user=request.user,
                    amount=serializer.validated_data['amount'],
                    currency=serializer.validated_data['currency'],
                    transaction_type='PAYMENT',
                    status='COMPLETED'
                )
                return Response(response.json(), status=status.HTTP_201_CREATED)
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)