from django.urls import path,include
from .views import UserRegistration,StudentRegistration,LoginAPI
urlpatterns = [
   path('stu-registration', StudentRegistration.as_view(), name='StudentRegistration'),
   path('user-registration', UserRegistration.as_view(), name='UserRegistration'),
   path('login-user', LoginAPI.as_view(), name='loginUser')
]