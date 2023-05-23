from django.urls import path,include
from .views import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI
urlpatterns = [
   path('stu-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('teacher-registration', TeacherRegistration.as_view(), name='TeacherRegistration'),
   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),
   path('login-user', LoginAPI.as_view(), name='loginUser')
]