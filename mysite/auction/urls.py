from django.urls import path
from .views import *

urlpatterns = [
    path('car/', CarViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='car_list'),
    path('car/<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),


    path('bet/', BetViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='bet_list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='bet_detail'),

    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='user_list'),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),
    ]

