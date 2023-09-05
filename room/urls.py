from django.urls import path
from room import views

urlpatterns=[
   path('rooms/',views.roomApi,name='room_detail') ,
   path('createRoom/',views.createRoom,name='create_Room') ,
   path('updateRoom/<int:id>/',views.updateRoom,name='update_room') ,
   path('deleteRoom/<int:id>/',views.deleteRoom,name='delete_room') 
]
