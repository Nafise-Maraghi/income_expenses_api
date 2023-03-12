from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=7, max_length=80, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def validate(self, attrs):
        username = attrs.get('username', '')
        email = attrs.get('email', '')

        # is username is not alphanumeric
        if not username.isalnum():
            raise serializers.ValidationError("The username should only contain alphanumeric characters.")

        return super().validate(attrs)

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
