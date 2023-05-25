from django.urls import path,include
from .auth import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI
from .views import Grade_API,Question_API,GradeDetail,QuestionDetail
urlpatterns = [
    # auth urls
   path('stu-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('teacher-registration', TeacherRegistration.as_view(), name='TeacherRegistration'),
   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),
   path('login-user', LoginAPI.as_view(), name='loginUser'),
   # views urls
   path('grade-api', Grade_API.as_view(), name='Grade_API'),
   path('question-api', Question_API.as_view(), name='Question_API'),
   path('grade-detail/<int:pk>/', GradeDetail.as_view(), name='GradeDetail'),
   path('question-detail/<int:pk>/', GradeDetail.as_view(), name='QuestionDetail'),

]