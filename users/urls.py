from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.sign_in, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.out, name='logout')
]