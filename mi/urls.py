from mi.views import *
from django.urls import path

app_name='everything'

urlpatterns=[


    path('rohit/',rohit,name='rohit'),
    path('ishan/',ishan,name='ishan'),
]