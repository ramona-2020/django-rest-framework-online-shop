from django.db.models import Count, Sum, IntegerField, DecimalField
from django.db.models.functions import TruncMonth
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from online_store.main_app.models import Product, Order
from online_store.main_app.serializers import ProductSerializer, MySerializer
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationDataOnly(PageNumberPagination):
    # Set any other options you want here like page_size
    page_size = 5

    def get_paginated_response(self, data):
        return Response(data)


# Product list
class ProductListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPaginationDataOnly


"""
    Monthly sales distribution for the selected period between 'date_start' and 'date_end'.
"""
class ListOrdersView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = MySerializer
    pagination_class = PageNumberPaginationDataOnly

    def get_queryset(self):

        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        metric = self.request.query_params.get('metric')

        if date_start and date_end and metric:
            if metric == 'count':
                queryset = Order.objects \
                                .filter(date__range=(date_start, date_end)) \
                                .annotate(month=TruncMonth('date')) \
                                .values('month') \
                                .annotate(value=Count('products__id'))\
                                .values('month', 'value') \
                                .order_by('month')

                print(queryset.query)

            elif metric == 'price':
                queryset = Order.objects \
                    .filter(date__range=(date_start, date_end)) \
                    .annotate(month=TruncMonth('date')) \
                    .values('month') \
                    .annotate(value=Sum('products__price')) \
                    .values('month', 'value') \
                    .order_by('month')
            else:
                raise ValidationError({'error': 'Parameter metric not valid.'})

            return queryset

        else:
            raise ValidationError({'error': 'Missing required parameters.'})
