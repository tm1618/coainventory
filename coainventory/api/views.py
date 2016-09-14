from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from inventory.models import *


# Serializers define the API representation.
class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ('name',)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# Serializers define the API representation.
class ComputerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Device
        fields = ('id', 'UniqueID', 'department', 'Location')


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = ComputerSerializer


# Serializers define the API representation.
class ServerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Server
        fields = ('Name', 'Role')


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

