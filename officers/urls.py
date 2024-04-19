from django.urls import path
from officers.views import *

urlpatterns = [
    path('sign_in/',sign_in, name='sign_in'),
    path('sign_out/',sign_out, name='sign_out'),
    path('events/',events, name='events'),
    path('add_event/',add_event, name='add_event'),
]