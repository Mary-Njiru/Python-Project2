from django.urls import path
from api.views import StudentListView
from api.views import CourseListView
from api.views import TeacherListView
from api.views import ClassRoomListView
from api.views import ClassPeriodListView



urlpatterns = [
    path("student/", StudentListView.as_view(), name = "student_list-view"),
    path("teacher/", TeacherListView.as_view(), name = "teacher_list-view"),
    path("course/", CourseListView.as_view(), name = "course_list-view"),
    path("classroom/", ClassRoomListView.as_view(), name = "classroom_list-view"),
    path("classperiod/", ClassPeriodListView.as_view(), name = "classperiod_list-view"),

]


