from django.urls import path
from. import views
from django.views.generic import TemplateView  
from .views import contact_view

urlpatterns = [
    path('driverP', views.index, name='homeP'),  # URL pattern name is 'home'
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='editprofile'),
    path('loginD/', views.login_user, name='loginD'),
    path('registerD/', views.register_user, name='registerD'),
    path('logoutD/', views.logout_user, name='logoutD'),
     path('contact/', contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name='profileapp/success.html'), name='success'),
        path('mark-interested/<int:car_id>/', views.mark_interested, name='mark_interested'),
    path('interested-cars/', views.interested_cars, name='interested_cars'),
    path('search-carsD/', views.CarSearchView.as_view(), name='search_carsD'),
]