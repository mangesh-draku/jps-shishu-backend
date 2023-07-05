from django.urls import path,include
from .auth import UserRegistration,StudentRegistration,TeacherRegistration,LoginAPI,TeacherDetail,TeacherList, StudentList, StudentDetail
from .views import Grade_API,Question_API,Assessment_API,GradeDetail,QuestionDetail,\
   AssessmentDetail,QuestionSelectReleventPictureAPI,QuestionMatchThePairsAPI,QuestionMultipleChoiceQuestionsAPI,\
   Chapter_API,ChapterDetail,Subject_API,SubjectDetail,List_Chapter_API,List_Subject_API,SubjectList,ChapterList,QuestionListAPI,TeacherAssessmentList,StudentAssessessmetList
urlpatterns = [
   path('login-user', LoginAPI.as_view(), name='loginUser'),
   
    # Student urls
   path('student-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('student-list',StudentList.as_view(),name="Student list"),
   path('student-detail/<int:pk>/', StudentDetail.as_view(), name='StudentDetail'),
   
    # Teacher urls
   path('teacher-registration', TeacherRegistration.as_view(), name='TeacherRegistration'),
   path('teacher-list',TeacherList.as_view(),name="Teacher list"),
   path('teacher-detail/<int:pk>/', TeacherDetail.as_view(), name='TeacherDetail'),
   path('teacher/assessment/<int:teacher_id>/',TeacherAssessmentList.as_view(),name="teacher assessment"),
   
   # Grade urls
   path('grade-api', Grade_API.as_view(), name='Grade_API'),
   path('grade-detail/<int:pk>/', GradeDetail.as_view(), name='GradeDetail'),

   # chapter urls
   path('chapter-api', Chapter_API.as_view(), name='Chapter_API'),
   path('list-chapter-api', List_Chapter_API.as_view(), name='List_Chapter_API'),
   path('chapter-detail/<int:pk>/', ChapterDetail.as_view(), name='GradeDetail'),
   path('chapter-list/<int:subject_id>/', ChapterList.as_view(), name='ChapterList'),


   # Subject urls
   path('subject-api', Subject_API.as_view(), name='Subject_API'),
   path('list-subject-api', List_Subject_API.as_view(), name='Subject_API'),
   path('subject-detail/<int:pk>/', SubjectDetail.as_view(), name='SubjectDetail'),
   path('subject-list/<int:grade_id>/', SubjectList.as_view(), name='SubjectList'),
   
    # Question urls
   path('question-api', Question_API.as_view(), name='Question_API'),
   path('relevent-pic-api', QuestionSelectReleventPictureAPI.as_view(), name='QuestionSelectReleventPictureAPI'),
   path('match-pairs-api', QuestionMatchThePairsAPI.as_view(), name='QuestionMatchThePairsAPI'),
   path('mcq-api', QuestionMultipleChoiceQuestionsAPI.as_view(), name='QuestionMultipleChoiceQuestionsAPI'),
   path('question-detail/<int:pk>/', QuestionDetail.as_view(), name='QuestionDetail'),
   path('question-list', QuestionListAPI.as_view(), name='QuestionListAPI'),

   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),

   # Assessment urls
   path('assessment-api', Assessment_API.as_view(), name='Assessment_Api'),
   path('assessment-detail/<int:pk>/', AssessmentDetail.as_view(), name='AssessmentDetail'),
   path('student/assessment/',StudentAssessessmetList.as_view(),name="assessment list"),
]