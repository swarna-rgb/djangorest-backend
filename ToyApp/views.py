from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Toy
from .serializers import ToySerializer
# Create your views here.
@api_view(['GET','POST'])
def toy_list(request,format=None):
    if request.method == 'GET':
        toys = Toy.objects.all()
        serializer = ToySerializer(toys,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        toydata = JSONParser().parse(request)
        serializer = ToySerializer(data=toydata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET - get a toy instance
#PUT - update a toy instance
#DELETE - delete a toy instance
@api_view(['GET','PUT','DELETE'])
def toy_detail(request,id,format=None):

    try:
        toyobject = Toy.objects.get(id=id)
    except Toy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ToySerializer(toyobject)
        return Response(serializer.data)

    if request.method == 'PUT':
        toydata = JSONParser().parse(request)
        serializer = ToySerializer(data=toydata,instance=toyobject)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        toyobject.delete()
        return Response('deleted',status=status.HTTP_204_NO_CONTENT)

