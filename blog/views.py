from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
@api_view(['GET','POST'])
def hello_world(request):
    p = [
        {'name':' laptop', 'price': 22},
        {'name': 'mobile', 'price': 11}
    ]
    return Response(data=p)

class Cbv(APIView):
    def get(self, request):
        p = [
            {'name': 'amprela', 'peice': 11},
            {'name': 'camera', 'price': 222}
        ]
        return Response(data=p)

    def post(self, request):
        p = [
            {'name': 'amprela', 'peice': 11},
            {'name': 'camera', 'price': 222}
        ]
        return Response(data=p)

