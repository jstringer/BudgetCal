# BudgetCal
A web app for tracking your expenses in a daily calendar format.

# Motivation
This personal project is being developed as a means for me to learn Django and React and improve my full stack development skills with a fun, practical application.

# Features
- Keeps track of balances in each account and updates them on-the-fly as your transactions happen.
- Allows you to see where your money is going on each day and where you stand with your finances.
- Simple interface for adding new accounts, transactions, and looking ahead at the coming months day by day.

# Interface

![Sample Interface](https://github.com/jstringer/BudgetCal/blob/master/BudgetCal/images/sample_design.png)

# Frameworks used
* Back end:
... Django with [Django Rest Framework](https://www.django-rest-framework.org/)

* Front end:
... React

# Design
On the backend, there are two database models for this app: `Account` and `Transaction`. Each `Transaction` is associated with a single `Account` and each `Account` has multiple `Transactions`.

The API provides two views that handle GET and POST requests for all `Transaction` and `Account` data. The `Transaction` model has an overridden `get_queryset` method that is invoked every time a GET request is made on the `TransactionList` class-based view:

```python
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
```

Each time a GET request is made on the `TransactionList` view, this method checks the date, collects all old `Transaction` objects whose `date` field has passed, updates the object's associated `Account` balance, and removes the transaction from the database.  This ensures that a user's account is up-to-date every time they open the app.

The API then returns all updated `Transaction` and `Account` data to the front end.

The front end portion of this app is still in development and will be written using React.
