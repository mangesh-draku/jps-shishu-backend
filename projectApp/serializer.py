from rest_framework import serializers
from .models import User, StudentTableStructure,TeacherTableStructure,GradeTableStructure,QuestionTableStructure
import string
import random
from rest_framework.serializers import ModelSerializer, Serializer
from django.db import transaction
import copy
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("validated data",validated_data)
        password = validated_data['firstname'][0:4] + \
                    ''.join([random.choice(string.digits) for i in range(0, 4)])
        validated_data['password'] = password 
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

class TeacherTableStructureSerilizer(Serializer):
    # id = serializers.IntegerField(required=False)
    email = serializers.CharField(allow_null=True, allow_blank=True)
    phone = serializers.CharField(allow_null=True, allow_blank=True)
    firstname = serializers.CharField(allow_null=True, allow_blank=True)
    lastname = serializers.CharField(allow_null=True, allow_blank=True)
    aadhar_number=serializers.CharField(allow_null=True, allow_blank=True)
    address_line_1=serializers.CharField(allow_null=True, allow_blank=True)
    city=serializers.CharField(allow_null=True, allow_blank=True)
    country=serializers.CharField(allow_null=True, allow_blank=True)
    date_of_joining=serializers.CharField(allow_null=True, allow_blank=True)
    designation=serializers.CharField(allow_null=True, allow_blank=True)
    father_name=serializers.CharField(allow_null=True, allow_blank=True)
    gender=serializers.CharField(allow_null=True, allow_blank=True)
    height=serializers.CharField(allow_null=True, allow_blank=True)
    lastname=serializers.CharField(allow_null=True, allow_blank=True)
    marital_status=serializers.CharField(allow_null=True, allow_blank=True)
    middlename=serializers.CharField(allow_null=True, allow_blank=True)    
    pan_number=serializers.CharField(allow_null=True, allow_blank=True)
    pincode=serializers.CharField(allow_null=True, allow_blank=True)
    spause_name=serializers.CharField(allow_null=True, allow_blank=True)
    state=serializers.CharField(allow_null=True, allow_blank=True)
    weight=serializers.CharField(allow_null=True, allow_blank=True)

    def to_internal_value(self, data):
        internal_data = copy.deepcopy(data)
        if internal_data.get("aadhar_number", None) == None:
            internal_data['aadhar_number'] = None

        if internal_data.get("address_line_1", None) == None:
            internal_data['address_line_1'] = None
        
        if internal_data.get("city", None) == None:
            internal_data['city'] = None
        
        if internal_data.get("country", None) == None:
            internal_data['country'] = None
        
        if internal_data.get("father_name", None) == None:
            internal_data['father_name'] = None
        
        if internal_data.get("gender", None) == None:
            internal_data['gender'] = None
        
        if internal_data.get("height", None) == None:
            internal_data['height'] = None
        
        if internal_data.get("marital_status", None) == None:
            internal_data['marital_status'] = None
        
        if internal_data.get("middlename", None) == None:
            internal_data['middlename'] = None
        
        if internal_data.get("pan_number", None) == None:
            internal_data['pan_number'] = None
        
        if internal_data.get("pincode", None) == None:
            internal_data['pincode'] = None

        if internal_data.get("spause_name", None) == None:
            internal_data['spause_name'] = None
        
        if internal_data.get("state", None) == None:
            internal_data['state'] = None

        if internal_data.get("weight", None) == None:
            internal_data['weight'] = None

        # if internal_data.get("id", None) == None:
        #     internal_data['id'] = None

        return super(TeacherTableStructureSerilizer, self).to_internal_value(internal_data)
    def create(self, validated_data):
        request_data = copy.deepcopy(validated_data)
        
        with transaction.atomic():
                username = validated_data['firstname']+validated_data['lastname']+''.join([random.choice(string.digits) for i in range(0, 4)])
                password = request_data['firstname'][0:4] + \
                    ''.join([random.choice(string.digits) for i in range(0, 4)])
                user = User.objects.create(username=username, email=validated_data['email'],
                                        phone=validated_data['phone'], is_teacher=True)
                user.set_password(password)
                user.save()
                TeacherTableStructure.objects.create(
                    teacher=user,aadhar_number=validated_data['aadhar_number'],
                    address_line_1=validated_data['address_line_1'],
                    city=validated_data['city'],
                    country=validated_data['country'],
                    date_of_joining=validated_data['date_of_joining'],
                    email=validated_data['email'],
                    designation=validated_data['designation'],
                    father_name=validated_data['father_name'],
                    firstname=validated_data['firstname'],
                    gender=validated_data['gender'],
                    height=validated_data['height'],
                    lastname=validated_data['lastname'],
                    marital_status=validated_data['marital_status'],
                    middlename=validated_data['middlename'],
                    phone=validated_data['phone'],
                    pan_number=validated_data['pan_number'],
                    pincode=validated_data['pincode'],
                    spause_name=validated_data['spause_name'],
                    state=validated_data['state'],
                    weight=validated_data['weight'],
                )
                return request_data
    class Meta:
        model = TeacherTableStructure
        fields = '__all__'
    
class TeacherSerilizer(serializers.ModelSerializer):
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