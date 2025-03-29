from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import VirtualAccount
from .serializers import VirtualAccountSerializer
import uuid


class VirtualAccountCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        account = VirtualAccount.objects.create(
            user=request.user,
            account_number=str(uuid.uuid4())[:10],
            bank_name=request.data.get('bank_name', 'FinTech Bank'),
            currency=request.data.get('currency', 'USD')
        )
        serializer = VirtualAccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
