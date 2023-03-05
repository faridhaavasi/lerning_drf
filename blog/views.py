from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import postserializer
from .models import Post
# used class base view

class List_post_API(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = postserializer(instance=queryset, many=True)
        return Response(serializer.data)
class Detail_post_API(APIView):
    def get(self, request, pk):
        queryset = Post.objects.get(id=pk)
        serializer = postserializer(instance=queryset)
        return Response(serializer.data)


class addpost(APIView):
    def post(self, request):
        serializer = postserializer(data=request.data)
        if serializer.is_valid():
            return Response({'massage': 'down'})
        else:
            return Response(serializer.errors)