import json
import uuid

from django.http import JsonResponse
from pydantic import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView as RestAPIView

from blockchain.blockchain import blockchain
from cryptocurrency.momocoin import MomoCoin
from cryptocurrency.types import Transaction, MemPool, TransactionRequest

mem_pool = MemPool()
node_address = str(uuid.uuid4()).replace('-', '')


class MomoMineView(RestAPIView):
    def post(self, request):
        ready_transactions = list(mem_pool.pending_transactions.values())
        if len(ready_transactions) == 0:
            return JsonResponse({"errors": ["no ready transaction found"]}, status=500)

        new_block = MomoCoin(ready_transactions, blockchain.get_previous_block())
        blockchain.append(new_block)
        mem_pool.confirm(ready_transactions)
        mem_pool.add(Transaction(node_address, 'mohammad', 1))  # reward of mining

        return Response(data=new_block.__dict__, status=status.HTTP_201_CREATED)

class AddTransactionView(RestAPIView):
    def post(self, request):
        try:
            body = json.loads(request.body)
            data = TransactionRequest(**body)
            transaction = mem_pool.add(Transaction(sender=data.sender, receiver=data.receiver, amount=data.amount))
            return Response(data=transaction.__dict__, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return JsonResponse({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)
