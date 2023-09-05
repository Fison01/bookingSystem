from django.urls import path
from reservation import views

urlpatterns=[
   path('roomReservations/',views.roomReservations,name='reservation-list') ,
   path('createRoomReservations/',views.createRoomReservation,name='reservation-create') ,
   path('updateRoomReservations/<int:id>/',views.updateRoomReservation,name='reservation-update') ,
   path('deleteRoomReservations/<int:id>/',views.deleteRoomReservation,name='reservation-delete') 
]