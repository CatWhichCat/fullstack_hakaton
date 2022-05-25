from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken , TokenError

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,
                                     required=True,
                                     write_only=True    #pri vozvrawenii ne budem ispol'zovat'
                                     )

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError('User with given email already exists')
        return value

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    pass


class ActivationSerializer(serializers.Serializer):
    activation_code = serializers.CharField(required=True, write_only=True, max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError as exc:
            self.fail('bad_token')


class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True,
                                        min_length=8, 
                                        write_only=True)