from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from .models import Customer
from .serializers import CusSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CusView(APIView):

    def get_object(self,pk):
        try:
            return Customer.objects.get(pk=pk)
        except:
            return Http404


    def get(self,*args, **kwargs):
        try:
            _x=kwargs.get("pk")
            _data = self.get_object(_x)
            serializer = CusSerializer(_data)
            return Response({"data":serializer.data,"status":status.HTTP_200_OK})
        except:
            return Response({"data":"invalid username","status":status.HTTP_400_BAD_REQUEST})