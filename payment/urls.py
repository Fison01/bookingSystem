from django.urls import path
from payment import views

urlpatterns=[
   path('paymentTransactions/',views.paymentsList,name='payment-list') ,
   path('payementInitiation/',views.createPayment,name='payment-create') ,
]