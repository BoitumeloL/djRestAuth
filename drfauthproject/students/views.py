from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer

 

# Create your views here.

class StudentList(ListCreateAPIView):
    '''
    This view returns a list of students and their details, privided that a user is ligged in and their email is verified
    '''
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(RetrieveUpdateDestroyAPIView):
    '''
    This view returns the details of a student - specified by a primary key representing the student
    '''
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

