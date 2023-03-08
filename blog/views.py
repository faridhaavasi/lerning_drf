from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import postserializer, PostserializerModel
from .models import Post
# used class base view

class List_post_API(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = postserializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class Detail_post_API(APIView):
    def get(self, request, pk):
        queryset = Post.objects.get(id=pk)
        serializer = postserializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class addpost(APIView):
    def post(self, request):
        serializer = postserializer(data=request.data)
        if serializer.is_valid():
            return Response({'massage': 'down'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class updataApi(APIView):
    def put(self, request, pk):
        instance = Post.objects.get(id=pk)
        serializer = PostserializerModel(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'updated'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deleteApi(APIView):
    def DELETE(self, request, pk):
        instance = Post.objects.get(id=pk)
        instance.delete()
        return Response({'massage': 'deleted'}, status=status.HTTP_200_OK)






