import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import VirtualCard
from .serializers import VirtualCardSerializer


class VirtualCardCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        api_key = settings.CARD_API_KEY   
        data = {
            'user_id': request.user.id,
            'currency': request.data.get('currency', 'USD'),
        } 
        
        response = request.post(
            'https://api.cardissuer.com/cards',
            data=data,
            headers={'Authorization': f'Bearer {api_key}'}
        )
        
        if response.status_code == 200:
            card_data = response.json()
            card = VirtualCard.objects.create(
                user=request.user,
                card_number=card_data['card_number'],
                expiry_date=card_data['expiry_date'],
                cvv=card_data['cvv'],
                currency=card_data['currency']
            )
            serializer = VirtualCardSerializer(card)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
