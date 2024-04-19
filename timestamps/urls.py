from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('list/',list_events, name='list'),
    path('event_detail/<int:id>/',event_detail, name='event_detail'),
    ]