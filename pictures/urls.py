from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('donators/',searchDonators),
    path('register/',registerView),
    path('login/',loginView),
    path('logout/',logoutView),
    path('category/',category),
    path('user/<str:pk>/',userView),

]