from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
    path('profile/', views.driver_profile, name='driver_profile'),
    path('express_interest/<int:car_id>/', views.express_interest, name='express_interest'),
]
