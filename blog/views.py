from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import listpost_serializer
from .models import Post


class PostlistviewApi(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = listpost_serializer(instance=queryset, many=True)
        return Response(serializer.data)


class detailpostviewApi(APIView):
    def get(self, request, pk):
        queryset = Post.objects.get(pk=pk)
        serializer = listpost_serializer(instance=queryset)
        return Response(serializer.data)

class addpostApi(APIView):
    def post(self, request):
        serializer = listpost_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'down'})
        return Response(serializer.errors)


