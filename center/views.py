from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
# Create your views here.

from .serializer import CenterSerializer
from .models import Center
from .permissions import permissionsClass

class CenterListView(ListAPIView, CreateAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
    permission_classes = (permissionsClass,)

class CenterDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
    permission_classes = (permissionsClass,)
