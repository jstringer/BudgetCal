from django.urls import path

from . import views

app_name = 'budget'
urlpatterns = [
    path('api/accounts', views.AccountList.as_view(), name='accounts'),
    path('api/transactions', views.TransactionList.as_view(), name='transactions')
]
