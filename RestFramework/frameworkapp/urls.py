from django.urls import path

from .views import *

urlpatterns=[
path('getapi/',studentGetApi.as_view(),name='GetAPI'),
path('postapi/',studentPostApi.as_view(),name='PostAPI')
]
