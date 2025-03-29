from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Wallet
from .serializers import WalletSerializer


class WalletView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        wallets = Wallet.objects.filter(user=request.user)
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        currency = request.data.get('currency', 'USD')
        wallet, created = Wallet.objects.get_or_create(user=request.user, currency=currency)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
