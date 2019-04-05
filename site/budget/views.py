from django.shortcuts import render
from django.http import HttpResponse
from budget.models import Account, Transaction
from rest_framework import generics
from budget.serializers import AccountSerializer, TransactionSerializer
#from django.views import generic

# Create your views here.
class AccountList(generics.ListCreateAPIView):
    '''
    Lists all accounts
    '''
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

#    def get_queryset(self):
        #context = super(AccountList, self).get_context_data(**kwargs)
#        account_list = {}
#        queryset = {}
#        queryset = super().get_queryset()

#        for item in Account.objects.all():
            #The trick here is using the actual account object
            #as the key and NOT just its name
#            account_list[item] = Transaction.objects.filter(account=item)

#        queryset['account_list'] = account_list

#        return queryset

class TransactionList(generics.ListCreateAPIView):
    '''
    Lists all Transactions
    '''
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
