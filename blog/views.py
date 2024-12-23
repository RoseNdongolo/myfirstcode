from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@permission_classes(IsAuthenticated)
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
        
@api_view(['GET','PUT','DELETE'])
def post_view(request,id)
    try:
        post_image=post.object.get(id=id)
    except po.DoesNotExist:
        return Response ({'message:ID not found'})
    
    if request.method=='GET':
        serializer=postSerializer(post_image,partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        serializer=postSerializer(data=request.data)
        if serializer .is_valid():
            serializer .save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='DELETE':
        post_image()
        return Response(status=status.HTTP_204_NO_COMMENT)


