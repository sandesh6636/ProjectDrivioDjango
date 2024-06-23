from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='home'),  # URL pattern name is 'home'
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='editprofile'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]