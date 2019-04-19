from django.db import models
import datetime

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def update(self, amount):
        '''
        '''
        self.balance += amount
        self.save()

class TransactionManager(models.Manager):
    '''
    Custom manager to override get_queryset method
    overridden method removes old transactions and calls 'update'
    on all old transactions' accounts to update balance.
    '''
    def get_queryset(self):
        '''
        '''
        now = datetime.date.today()
        old = super(TransactionManager, self).get_queryset().filter(date__lte=now)

        for transaction in old:
            print(transaction.memo)
            transaction.account.update(transaction.amount)

        super(TransactionManager, self).get_queryset().filter(date__lte=now).delete()

        return super(TransactionManager, self).get_queryset()

class Transaction(models.Model):
    memo = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    objects = TransactionManager()

    def __str__(self):
        return self.memo
