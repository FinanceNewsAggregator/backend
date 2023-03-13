from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer that defines the fields for the user registration form
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    tags = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = User
        fields = ('email', 'password', 'tags')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
