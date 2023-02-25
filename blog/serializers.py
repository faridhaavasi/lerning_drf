from rest_framework import serializers
from .models import Post
'''
class listpost_serializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    status = serializers.BooleanField(required=False)
    def create(self, validated_data):
        return Post.objects.create(title=validated_data['title'], body=validated_data['body'], status=validated_data['status'])
'''
class listpost_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
