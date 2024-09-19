from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from .mypaginations import MyLimitOffsetPagination
from .mypaginations import MyCursorPagination


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyLimitOffsetPagination
    pagination_class = MyCursorPagination
