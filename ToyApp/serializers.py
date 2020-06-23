from rest_framework import serializers
from .models import Toy,Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    get_absolute_url = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ['id','name','category','created','slug','get_absolute_url']

class ToySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Toy
        fields = ['id','name','category','created','owner']

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

# class ToySerializer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     name = serializers.CharField(max_length=150)
#     category = serializers.CharField(max_length=150)
#     created = serializers.DateTimeField(required=False)
#
#     def create(self, validated_data):
#         return Toy.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.category = validated_data.get('category', instance.category)
#         instance.save()
#         return instance