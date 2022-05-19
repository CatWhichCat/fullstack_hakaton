from rest_framework import serializers
from .models import Product

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'description', 'made_in', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # if instance.category:
        #     representation['category'] = instance.category.title
        # representation['likes'] = instance.likes.all().count()
        # action = self.context.get('action')
        # if action == 'retrieve':
        #     # детализация
        #     representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        # else:
        #     representation['comments'] = instance.comments.all().count()
        return representation

    def validate_name(self, name):
        if Product.objects.filter(slug=name.lower().replace(' ', '-')).exists():
            raise serializers.ValidationError('Product with such name already exists')
        return name

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         exclude = ('product',)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user'] = instance.user.username
#         return representation