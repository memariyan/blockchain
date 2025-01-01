import json

from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView as RestAPIView

from blockchain.blockchain import blockchain
from blockchain.types import NodeConnectionRequest


# Create your views here.
class BlockchainView(RestAPIView):
    def get(self, request):
        return Response({
            'chain': list(map(vars, blockchain.chains))
        })

class BlockchainCheckView(RestAPIView):
    def get(self, request):
        result = blockchain.is_chain_valid()
        return Response({
            'valid': result,
        })

class BlockchainUpdateView(RestAPIView):
    def get(self, request):
        result = blockchain.replace_chain()
        return Response({
            'changed': result,
        })

class BlockchainConnectNodeView(RestAPIView):
    def post(self, request):
        try:
            data = NodeConnectionRequest(**json.loads(request.body))
            for node in data.nodes:
                blockchain.add_node(node)

            return JsonResponse({"nodes": list(blockchain.nodes)}, status=status.HTTP_200_OK)

        except ValidationError as e:
            return JsonResponse({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)
