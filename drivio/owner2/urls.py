from django.urls import path
from . import views




urlpatterns = [
   path('main2', views.main2, name='main2'),
   path('show/', views.car_list, name='car_list'),
   path('car/', views.my_car, name='my_car'),
   path('addcar', views.car_add, name='car_add'),
   path('<int:car_id>/update/', views.car_update, name='car_update'),
   path('<int:car_id>/delete/', views.car_delete, name='car_delete'),
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
]
