from dataclasses import asdict

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView as RestAPIView

from blockchain.blockchain import Blockchain

blockchain = Blockchain()


# Create your views here.
class BlockchainView(RestAPIView):
    def get(self, request):
        return Response(data=list(map(asdict, blockchain.chains)), status=status.HTTP_200_OK)


class BlockchainCheckView(RestAPIView):
    def get(self, request):
        result = blockchain.is_chain_valid()
        return Response({
            'valid': result,
        })


class BlockchainBlockView(RestAPIView):
    def put(self, request):
        previous_block = blockchain.get_previous_block()
        proof = blockchain.proof_of_work(previous_block.proof)
        previous_hash = blockchain.hash(previous_block)
        new_block = blockchain.create_block(proof, previous_hash)

        return Response(data=asdict(new_block), status=status.HTTP_200_OK)
