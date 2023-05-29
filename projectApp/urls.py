from django.urls import path,include
from .auth import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI,TeacherDetail,TeacherList, StudentList, StudentDetail
from .views import Grade_API,Question_API,GradeDetail,QuestionDetail
urlpatterns = [
   path('login-user', LoginAPI.as_view(), name='loginUser'),
   
    # Student urls
   path('student-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('student-list',StudentList.as_view(),name="Teacher list"),
   path('student-detail/<int:pk>/', StudentDetail.as_view(), name='StudentDetail'),
   
    # Teacher urls
   path('teacher-registration', TeacherRegistration.as_view(), name='TeacherRegistration'),
   path('teacher-list',TeacherList.as_view(),name="Teacher list"),
   path('teacher-detail/<int:pk>/', TeacherDetail.as_view(), name='TeacherDetail'),
   
   # Grade urls
   path('grade-api', Grade_API.as_view(), name='Grade_API'),
   path('grade-detail/<int:pk>/', GradeDetail.as_view(), name='GradeDetail'),
   
    # Question urls
   path('question-api', Question_API.as_view(), name='Question_API'),
   path('question-detail/<int:pk>/', QuestionDetail.as_view(), name='QuestionDetail'),

   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),
]