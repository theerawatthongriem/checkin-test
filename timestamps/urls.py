from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('list/',list_events, name='list'),
    ]