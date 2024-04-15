from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from .models import *
from .permissions import *
from rest_framework.pagination import PageNumberPagination
from django_filters. rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class CarAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CarAPIListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('category', 'marka', 'model', 'price', 'year', 'color', 'country', 'volume',)
    search_fields = ['category', 'marka', 'model', 'price', 'year', 'color', 'country', 'volume',]



class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CarAPIListPagination



