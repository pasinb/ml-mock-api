from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters, pagination, exceptions
from .models import *
from .serializers import *

class ScmUserViewset(viewsets.ModelViewSet):
    queryset = ScmUser.objects.all()
    serializer_class = ScmUserSerializer

