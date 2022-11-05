from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('donators/',searchDonators),
    oath('register/',)

]