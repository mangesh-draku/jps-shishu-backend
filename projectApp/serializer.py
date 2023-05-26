from rest_framework import serializers
from .models import User, StudentTableStructure,TeacherTableStructure,GradeTableStructure,QuestionTableStructure

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
                    username=validated_data['username'],
                    email=validated_data['email'],
                    phone=validated_data['phone'],
                    is_active=validated_data['is_active'],
                    is_admin_user=validated_data['is_admin_user'],
                    is_student=validated_data['is_student'],
                    is_teacher=validated_data['is_teacher'],
                    is_staff=validated_data['is_staff'],
                    user_type=validated_data['user_type'],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    class Meta:
        model = User
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']
        
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