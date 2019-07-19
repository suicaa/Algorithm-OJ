class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []  #上一笔交易发生了什么

    def new_block(self):
        pass

    def new_transaction(self):
        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass

class Blockchain(object):

    block = {
        'index':len(self.chain) + 1,
        'timestamp':time(),
        'transactions':self.current_transaction,
        'proof':proof,
        'previous_hash' or self.hash(self.chain[-1]),
    }

