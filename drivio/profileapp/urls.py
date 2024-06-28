from django.urls import path
from. import views

urlpatterns = [
    path('driverP', views.index, name='homeP'),  # URL pattern name is 'home'
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='editprofile'),
    path('loginD/', views.login_user, name='loginD'),
    path('registerD/', views.register_user, name='registerD'),
    path('logoutD/', views.logout_user, name='logoutD'),
]