from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from classroom.models import ClassRoom
from .serializers import ClassRoomSerializer
from course.models import Course
from .serializers import CourseSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response

class StudentListView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
class CourseListView(APIView):
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
class ClassRoomListView(APIView):
    def get(self,request):
        classroom = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classroom, many=True)
        return Response(serializer.data)
    

    

