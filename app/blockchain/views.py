from dataclasses import asdict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView as RestAPIView

from blockchain.blockchain import blockchain



# Create your views here.
class BlockchainView(RestAPIView):
    def get(self, request):
        return Response(data=list(map(vars, blockchain.chains)), status=status.HTTP_200_OK)


class BlockchainCheckView(RestAPIView):
    def get(self, request):
        result = blockchain.is_chain_valid()
        return Response({
            'valid': result,
        })
