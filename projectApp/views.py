from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, filters, status,serializers
from .models import GradeTableStructure,QuestionTableStructure,AssessmentTableStructure
from .serializer import GradeTableStructureSerilizer,QuestionTableStructureSerilizer,AssessmentTableStructureSerilizer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, pagination, filters
from rest_framework_jwt.settings import api_settings
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import login,authenticate,logout
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import get_user_object
import copy
from django.http import Http404


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
    
class GradeDetail(APIView):
    """
    Retrieve, update or delete a grade instance.
    """
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return GradeTableStructure.objects.get(pk=pk)
        except GradeTableStructure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        GradeTableStructure = self.get_object(pk)
        serializer = GradeTableStructureSerilizer(GradeTableStructure)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        GradeTableStructure = self.get_object(pk)
        serializer = GradeTableStructureSerilizer(GradeTableStructure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        GradeTableStructure = self.get_object(pk)
        GradeTableStructure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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

class QuestionDetail(APIView):
    """
    Retrieve, update or delete a question instance.
    """
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return QuestionTableStructure.objects.get(pk=pk)
        except QuestionTableStructure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        QuestionTableStructure = self.get_object(pk)
        serializer = QuestionTableStructureSerilizer(QuestionTableStructure)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        QuestionTableStructure = self.get_object(pk)
        serializer = QuestionTableStructureSerilizer(QuestionTableStructure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Assessment_API(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = AssessmentTableStructure.objects.all()
        serializer = AssessmentTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssessmentTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AssessmentDetail(APIView):
    """
    Retrieve, update or delete a Assessment instance.
    """
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return AssessmentTableStructure.objects.get(pk=pk)
        except AssessmentTableStructure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        AssessmentTableStructure = self.get_object(pk)
        serializer = AssessmentTableStructureSerilizer(AssessmentTableStructure)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        AssessmentTableStructure = self.get_object(pk)
        serializer = AssessmentTableStructureSerilizer(AssessmentTableStructure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    