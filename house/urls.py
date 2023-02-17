from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/house<int:pk>', views.create_house, name='create_house'),
    path('create/apartment/<int:pk>', views.create_apartment, name='create_apartment'),
]
