from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Toy
from .serializers import ToySerializer
# Create your views here.
@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        serializer = ToySerializer(toys,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        toydata = JSONParser().parse(request)
        serializer = ToySerializer(data=toydata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET - get a toy instance
#PUT - update a toy instance
#DELETE - delete a toy instance
@csrf_exempt
def toy_detail(request,id):

    try:
        toyobject = Toy.objects.get(id=id)
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ToySerializer(toyobject)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        toydata = JSONParser().parse(request)
        serializer = ToySerializer(data=toydata,instance=toyobject)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        toyobject.delete()
        return HttpResponse('deleted',status=status.HTTP_204_NO_CONTENT)

