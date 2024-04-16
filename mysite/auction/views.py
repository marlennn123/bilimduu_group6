from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import *
from rest_framework.pagination import PageNumberPagination
from django_filters. rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response


class CarAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = CarAPIListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('category', 'marka', 'model', 'price', 'year', 'color', 'country', 'volume',)
    search_fields = ['name', 'category', 'marka', 'model', ]
    ordering_fields = ('price', 'mileage', 'year',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Применяем сортировку
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CarDetailViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Получаем все ставки для данного автомобиля
        bets = Bet.objects.filter(car=instance)
        bet_serializer = BetSerializer(bets, many=True)

        data = serializer.data
        data['bets'] = bet_serializer.data  # Добавляем ставки к данным об автомобиле

        return Response(data)


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CarAPIListPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = CarAPIListPagination



