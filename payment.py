import uuid
from dataclasses import dataclass
import datetime

import pyqiwi

from data.config import QIWI_TOKEN, QIWI_WALLET, QIWI_PUBKEY

wallet = pyqiwi.Wallet(token=QIWI_TOKEN, number=QIWI_WALLET)


class NotEnoughMoney(Exception):
    pass


class NotFoundPayment(Exception):
    pass


@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())

    def check_payment(self):
        start_date = datetime.datetime.now() - datetime.timedelta(days=2)
        transactions = wallet.history(start_date=start_date).get('transaction')
        for transaction in transactions:
            if transaction.comment:
                if str(self.id) in transaction.comment:
                    if float(transaction.total.amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            raise NotFoundPayment

    @property
    def invoice(self):
        link = 'https://oplata.qiwi.com/create?publicKey={pubkey}&amount={amount}&comment={comment}'
        return link.format(pubkey=QIWI_PUBKEY, amount=self.amount, comment=self.id)
