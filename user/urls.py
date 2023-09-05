from django.urls import path
from . import views

urlpatterns=[
   path('clientList/',views.userList,name='users_list') ,
   path('createClient/',views.createUser,name='create_user') ,
   path('updateClient/<int:id>/',views.updateUser,name='update_user') ,
   path('deleteClient/<int:id>/',views.deleteUser,name='delete_user') 
]