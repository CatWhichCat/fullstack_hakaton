from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from product.serializers import *
from . models import Category, Product, Like
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, action


class MyPaginationClass(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class=MyPaginationClass

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

    @action(detail=False, methods=['get'])  #action dostupny tol'ko v ViewSet / router builds path/search/?q=paris
    def search(self, request, pk=None):
        q = request.query_params.get('q')    #request.query_params = request.GET
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(name__icontains=q) |
                                   Q(description__icontains=q)|
                                   Q(made_in__icontains=q))
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter(self, request):
        queryset = self.queryset

        price = request.query_params.get('price')
        category = request.query_params.get('category')
        made_in = request.query_params.get('made_in')
        print(request.query_params)
        if category:
            queryset = queryset.filter(category=category)
        elif made_in:
            queryset = queryset.filter(made_in=made_in)
        elif price == 'asc':
            queryset = self.get_queryset().order_by('price')
        elif price == 'desc':
            queryset = self.get_queryset().order_by('-price')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@login_required
def toggle_like(request, id):
    product = Product.objects.get(id=id)
    if Like.objects.filter(user=request.user, product=product):
        Like.objects.get(user=request.user, product=product).delete()
    else:
        Like.objects.create(user=request.user, product=product)
    serializer = ProductSerializer(product)
    return Response(serializer.data)