from django.urls import path
from . import views



urlpatterns = [
   path('main', views.show_car, name='main'),
   path('addCar/', views.post_car, name='addcar'),
   path('updateCar/<int:car_id>', views.update_car, name="updatecar"),
  path('deletecar/<int:car_id>', views.delete_car, name='deletecar'),

     
]
