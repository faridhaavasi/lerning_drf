from rest_framework import serializers
from .models import Post
class postserializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    body = serializers.CharField()
    status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

