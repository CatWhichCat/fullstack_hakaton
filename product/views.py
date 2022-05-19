from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
from rest_framework import serializers
# from . models import Product, Likes, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

# @api_view(['GET'])
# @login_required
# def toggle_like(request, id):
#     product = Product.objects.get(id=id)
#     if Likes.objects.filter(user=request.user, product=product):
#         Likes.objects.get(user=request.user, product=product).delete()
#     else:
#         Likes.objects.create(user=request.user, product=product)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)

# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
