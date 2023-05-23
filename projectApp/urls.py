from django.urls import path,include
from .views import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI,Grade_API,Question_API
urlpatterns = [
   path('stu-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('teacher-registration', TeacherRegistration.as_view(), name='TeacherRegistration'),
   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),
   path('grade-api', Grade_API.as_view(), name='Grade_API'),
   path('question-api', Question_API.as_view(), name='Question_API'),
   path('login-user', LoginAPI.as_view(), name='loginUser')
]