from typing import List

from cryptocurrency.types import Transaction


class MemPool:
    pending_transactions = dict()

    @classmethod
    def add(cls, transaction: Transaction) -> Transaction:
        cls.pending_transactions[transaction.id] = transaction
        return transaction

    @classmethod
    def confirm(cls, transactions: List[Transaction]) -> None:
        keys_to_delete = [t.id for t in transactions]
        for tid in keys_to_delete:
            cls.pending_transactions.pop(tid)
