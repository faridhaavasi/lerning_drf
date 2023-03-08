from rest_framework import serializers
from .models import Post

# custom validitor
def Chek_title(value):
    if value == 'html':
        raise serializers.ValidationError({'title': 'title cont html'})


class postserializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(validators=[Chek_title(), ])
    body = serializers.CharField()
    status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class PostserializerModel(serializers.ModelSerializer):
    class Meta:
        model = Post
       # fields = '__all__'
        exclude = ('status',)
        read_only_fields = ['id']
        validators = [
            Chek_title,
        ]
