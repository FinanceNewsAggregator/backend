from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ('tags',)


# Serializer that defines the fields for the user registration form
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    preference = PreferenceSerializer()

    class Meta:
        model = User
        fields = ('email', 'password', 'preference')

    def create(self, validated_data):
        preference_data = validated_data.pop('preference')
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        preference = Preference.objects.create(user=user, **preference_data)
        user.save()
        return user