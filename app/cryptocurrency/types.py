import uuid

from pydantic import BaseModel


class TransactionRequest(BaseModel):
    sender: str
    receiver: str
    amount: float


class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "id": self.id,
        }

    @staticmethod
    def from_dict(data: dict):
        tx = Transaction(
            sender=data["sender"],
            receiver=data["receiver"],
            amount=data["amount"],
        )
        tx.id = data["id"]
        return tx
