# serializers.py
from rest_framework import serializers
from .models import User, Tag

class UserSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'tags']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        user = User.objects.create(**validated_data)
        for tag_data in tags_data:
            user.tags.add(tag_data)
        return user