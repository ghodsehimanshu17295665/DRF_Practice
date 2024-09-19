from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1')
    serializer_class = StudentSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['city']
    # search_fields = ['city', 'name']
    filter_backends = [OrderingFilter]
    search_fields = ['city']
