from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'description', 'made_in', 'image' )

    def validate_name(self, name):
        if Product.objects.filter(slug=name.lower().replace(' ', '-')).exists():
            raise serializers.ValidationError('Product with such name already exists')
        return name

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.category:
            representation['category'] = instance.category.name
        representation['likes'] = instance.likes.all().count()
        return representation

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['user'] = instance.user.email
    #     return representation


