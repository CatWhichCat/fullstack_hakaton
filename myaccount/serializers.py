from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6,
                                     required=True,
                                     write_only=True    #pri vozvrawenii ne budem ispol'zovat'
                                     )

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with given email already exists')
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
     pass


class ActivationSerializer(serializers.Serializer):
    activation_code = serializers.CharField(required=True, write_only=True, max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'