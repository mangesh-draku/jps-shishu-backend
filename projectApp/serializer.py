from rest_framework import serializers
from .models import User, StudentTableStructure,TeacherTableStructure,GradeTableStructure,QuestionTableStructure

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StudentTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
        model = StudentTableStructure
        fields = '__all__'

class TeacherTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTableStructure
        fields = '__all__'
class GradeTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GradeTableStructure
        fields = '__all__'
class QuestionTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTableStructure
        fields = '__all__'