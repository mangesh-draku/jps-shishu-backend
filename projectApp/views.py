from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, filters, status,serializers
from .models import StudentTableStructure,User,TeacherTableStructure,GradeTableStructure,QuestionTableStructure
from .serializer import StudentTableStructureSerilizer,UserSerializer,UserLoginSerializer,TeacherTableStructureSerilizer,GradeTableStructureSerilizer,QuestionTableStructureSerilizer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, pagination, filters
from rest_framework_jwt.settings import api_settings
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import login,authenticate,logout
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import get_user_object
import copy


class UserRegistration(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRegistration(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = StudentTableStructure.objects.all()
        serializer = StudentTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherRegistration(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = TeacherTableStructure.objects.all()
        serializer = TeacherTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Grade_API(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = GradeTableStructure.objects.all()
        serializer = GradeTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GradeTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Question_API(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = QuestionTableStructure.objects.all()
        serializer = QuestionTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class LoginAPI(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            print("email",email,"password",password)
            user = authenticate(email=email, password=password)
            print("user",user)
            if user is not None:
                if user.is_active:
                    print("user login success")
                    login(request, user)
            if user is None or user.is_active == False:
                raise serializers.ValidationError(
                    'A user with this email and password is not found.'
                )
        try:
            refresh = RefreshToken.for_user(user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        copyUser = copy.deepcopy(user)
        if copyUser.first_time:
            copyUser.first_time = False
            copyUser.save()
        user = get_user_object(user)

        return Response({
            'user': user,
            'token': str(refresh.access_token),
        }, status=status.HTTP_200_OK)