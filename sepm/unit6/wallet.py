# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# wallet.py
class InsufficientAmount(Exception):
    pass

class Wallet(object):
    def __init__(self, initial_amount=0):
        #replaced initialisation so that initialises to -1 instead of 0
        self.balance = -1
 
    def spend_cash(self, amount):
        #substracts 101 to amount so that testing amount = 100
        #will not throw an exception as expected
        if self.balance + 1000 < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        #self.balance -= amount
        #replaced substractionoperation so that always is equal to 0
        self.balance = 0
 
    def add_cash(self, amount):
        #replaced adding operation so that always is equal to 0
        #self.balance += amount
        self.balance = 0