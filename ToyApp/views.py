from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Toy
from .serializers import ToySerializer,AuthUserSerializer
from .helper import GetallObjectsMixin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Create your views here
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin
)

from rest_framework import generics,permissions
from .permissions import IsOwnerorReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication,JWTTokenUserAuthentication
#
class Test_view(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return HttpResponse('Hello world')

class GenericToyList(generics.ListCreateAPIView):
   # authentication_classes = [JWTAuthentication]
   # permission_classes = [IsOwnerorReadOnly]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

    def perform_create(self, serializer):
        print('perform',self.request.user.is_superuser)
        serializer.save(owner=self.request.user)

class GenericToyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerorReadOnly]
    queryset = Toy.objects.all()
    serializer_class = ToySerializer


class ToyListMixins(generics.GenericAPIView,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     #RetrieveModelMixin,  # handles GETs for 1 Toy
                     #  UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Toys
      serializer_class = ToySerializer
      queryset = Toy.objects.all()

      def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)

      def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)

class ToyDetailMixins(generics.GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    serializer_class = ToySerializer
    queryset = Toy.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UserList(GetallObjectsMixin,APIView):
        model = User
        serializer = AuthUserSerializer

class ToyList(GetallObjectsMixin,APIView):
    model = Toy
    serializer = ToySerializer
    def post(self,request):
        toydata = JSONParser().parse(request.data)
        serializer = ToySerializer(data=toydata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET - get a toy instance
#PUT - update a toy instance
#DELETE - delete a toy instance

class ToyDetail(APIView):
    def get_object(self,id):
        try:
            toyobject = Toy.objects.get(id=id)
            return toyobject
        except Toy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id,format=None):
        toyobject = self.get_object(id)
        serializer = ToySerializer(toyobject)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        toyobject = Toy.objects.get(id=id)
        toydata = JSONParser().parse(request)
        serializer = ToySerializer(data=toydata,instance=toyobject)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        toyobject = Toy.objects.get(id=id)
        toyobject.delete()
        return Response('deleted',status=status.HTTP_204_NO_CONTENT)

