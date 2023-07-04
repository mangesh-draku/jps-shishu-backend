from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, filters, status,serializers
from .models import GradeTableStructure,QuestionTableStructure,AssessmentTableStructure,QuestionMatchThePairs,QuestionMultipleChoiceQuestions,QuestionSelectReleventPicture,ChapterTableStructure,SubjectTableStructure
from .serializer import GradeTableStructureSerilizer,QuestionTableStructureSerilizer,AssessmentTableStructureSerilizer,\
    QuestionSelectReleventPicture,QuestionMultipleChoiceQuestionsSerilizer,QuestionMatchThePairsSerilizer,\
    QuestionSelectReleventPictureSerilizer,QuestionTableStructureSerilizerCreate,ChapterTableStructureSerilizer,\
    SubjectTableStructureSerilizer,ListChapterTableStructureSerilizer,ListSubjectTableStructureSerilizer,SubjectListSerilizer,ChapterListSerilizer,SubjectListAllserializer,ChapterListAllSerializer, SubjectTableStructureSerilizerUpdate, ChapterTableStructureSerilizerUpdate,AssessmentTableStructureSerilizerCreate,TeacherAsessessmentSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework import generics, mixins, pagination, filters
from rest_framework_jwt.settings import api_settings
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import login,authenticate,logout
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
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
    # queryset=QuestionTableStructure.objects.all()
    # serializer_class=QuestionTableStructureSerilizerCreate
    def get(self, request, format=None):
        queryset = QuestionTableStructure.objects.all()
        serializer = QuestionTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionTableStructureSerilizerCreate(data=request.data)
        print("serializer",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response( status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
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
    
class QuestionListAPI(generics.ListAPIView):
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question_type', 'chapter_id']
    queryset = QuestionTableStructure.objects.all()
    serializer_class = QuestionTableStructureSerilizer
      
class Assessment_API(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        queryset = AssessmentTableStructure.objects.all()
        serializer = AssessmentTableStructureSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssessmentTableStructureSerilizerCreate(data=request.data)
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
    
class QuestionMatchThePairsAPI(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = QuestionMatchThePairs.objects.all()
    serializer_class = QuestionMatchThePairsSerilizer

class QuestionMultipleChoiceQuestionsAPI(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = QuestionMultipleChoiceQuestions.objects.all()
    serializer_class = QuestionMultipleChoiceQuestionsSerilizer

class QuestionSelectReleventPictureAPI(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = QuestionSelectReleventPicture.objects.all()
    serializer_class = QuestionSelectReleventPictureSerilizer

class List_Chapter_API(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ChapterTableStructure.objects.all()
    serializer_class = ChapterListAllSerializer

class List_Subject_API(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = SubjectTableStructure.objects.all()
    serializer_class = ListSubjectTableStructureSerilizer

class Chapter_API(APIView):
    permission_classes = (AllowAny,)
    queryset = ChapterTableStructure.objects.all()
    serializer_class = ChapterTableStructureSerilizer
    def get(self, request, format=None):
        queryset = ChapterTableStructure.objects.all()
        serializer = ChapterListAllSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ChapterTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChapterDetail(APIView):
    """
    Retrieve, update or delete a question instance.
    """
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return ChapterTableStructure.objects.get(pk=pk)
        except ChapterTableStructure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ChapterTableStructure = self.get_object(pk)
        serializer = ChapterTableStructureSerilizerUpdate(ChapterTableStructure)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ChapterTableStructure = self.get_object(pk)
        serializer = ChapterTableStructureSerilizerUpdate(ChapterTableStructure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
            chapter = self.get_object(pk)
            chapter.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class Subject_API(APIView):
    permission_classes = (AllowAny,)
    queryset = SubjectTableStructure.objects.all()
    serializer_class = SubjectTableStructureSerilizer
    def get(self, request, format=None):
        queryset = SubjectTableStructure.objects.all()
        serializer = SubjectListAllserializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print("serializer:", request.data)
        serializer = SubjectTableStructureSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectDetail(APIView):
    """
    Retrieve, update or delete a question instance.
    """
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            return SubjectTableStructure.objects.get(pk=pk)
        except SubjectTableStructure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        SubjectTableStructure = self.get_object(pk)
        serializer = SubjectTableStructureSerilizerUpdate(SubjectTableStructure)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        SubjectTableStructure = self.get_object(pk)
        serializer = SubjectTableStructureSerilizerUpdate(SubjectTableStructure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubjectList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SubjectListSerilizer

    def get_queryset(self):
        grade_id = self.kwargs['grade_id']
        return SubjectTableStructure.objects.filter(grade_id=grade_id)
    
class ChapterList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ChapterListSerilizer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return ChapterTableStructure.objects.filter(subject_id=subject_id)

class TeacherAssessmentList(generics.ListAPIView):
    permission_classes=(AllowAny,)
    serializer_class=TeacherAsessessmentSerializer

    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        return AssessmentTableStructure.objects.filter(teacher_id=teacher_id)