from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
def get_and_post(request):
    if request.method=='GET':
        post_image=post.objects.all()
        serializer=postSerializer(post_image,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=postSerializer(data=request.data)
        if serializer .is_valid():
            serializer .save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)