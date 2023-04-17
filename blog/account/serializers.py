from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterUserSerializer(ModelSerializer):
    password_confirm = CharField(min_length=7, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confirm')

    def validate(self, attrs):
        super().validate(attrs)
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')
        if p1 != p2:
            raise ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
