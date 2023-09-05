from django.urls import path
from meal import views

urlpatterns=[
   path('menuList/',views.menuList,name='menu_list') ,
   path('createNewMeal/',views.createNewMeal,name='create_new_meal') ,
   path('updateExistingMeal/<int:id>/',views.updateExistingMeal,name='update_existing_meal') ,
   path('deleteMeal/<int:id>/',views.deleteMeal,name='delete_meal') 
]