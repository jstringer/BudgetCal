from django.shortcuts import render
from django.http import HttpResponse
from budget.models import Account, Transaction
from rest_framework import generics
from budget.serializers import AccountSerializer, TransactionSerializer
#from django.views import generic

# Create your views here.
class AccountList(generics.ListCreateAPIView):
    '''
    GET and POST reqeust for all accounts
    '''
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class TransactionList(generics.ListCreateAPIView):
    '''
    GET and POST requests for all Transactions
    '''
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
