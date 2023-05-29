from django.urls import path,include
from .auth import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI,TeacherDetail,TeacherList
from .auth import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI,TeacherDetail,StudentDetail
from .views import Grade_API,Question_API,GradeDetail,QuestionDetail
urlpatterns = [
    # auth urls
   path('stu-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('teacher-registration', TeacherRegistration.as_view(), name='TeacherRegistration'),
   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),
   path('teacher-list',TeacherList.as_view(),name="Teacher list"),
   path('login-user', LoginAPI.as_view(), name='loginUser'),
   # views urls
   path('grade-api', Grade_API.as_view(), name='Grade_API'),
   path('question-api', Question_API.as_view(), name='Question_API'),
   path('grade-detail/<int:pk>/', GradeDetail.as_view(), name='GradeDetail'),
   path('question-detail/<int:pk>/', QuestionDetail.as_view(), name='QuestionDetail'),
   path('teacher-detail/<int:pk>/', TeacherDetail.as_view(), name='TeacherDetail'),
   path('student-detail/<int:pk>/', StudentDetail.as_view(), name='StudentDetail'),

]