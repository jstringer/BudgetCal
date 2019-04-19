from django.test import TestCase
from budget.models import Account, Transaction
from datetime import date

# Create your tests here.

class TransactionTestCase(TestCase):
    '''
    Tests the account object's update method 
    '''
    def setUp(self):
        acct = Account.objects.create(name="TestAccount", balance=100)
        trans = Transaction.objects.create(memo="TestTransaction", amount=-50, date=date.today(), account=acct)

    def test_update(self):
        transactions = Transaction.objects.all()
        acct = Account.objects.get(name="TestAccount")
        self.assertEqual(acct.balance, 50)
