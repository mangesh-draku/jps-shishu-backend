from rest_framework import serializers
from .models import User, StudentTableStructure,TeacherTableStructure,GradeTableStructure,QuestionTableStructure,AssessmentTableStructure,QuestionMatchThePairs,QuestionMultipleChoiceQuestions,QuestionSelectReleventPicture,SubjectTableStructure,ChapterTableStructure
import string
import random
from django.forms.models import model_to_dict
from rest_framework.serializers import ModelSerializer, Serializer,SerializerMethodField
from django.db import transaction
import copy
from .utils import upload_file_to_s3
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("validated data",validated_data)
        # password = validated_data['firstname'][0:4] + \
        #             ''.join([random.choice(string.digits) for i in range(0, 4)])
        # validated_data['password'] = password 
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
        
# class StudentTableStructureSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentTableStructure
#         fields = '__all__'
        
class StudentTableStructureSerilizer(Serializer):
    # student = serializers.CharField(allow_null=True, allow_blank=True)
    firstname = serializers.CharField(allow_null=True, allow_blank=True)
    middlename = serializers.CharField(allow_null=True, allow_blank=True)
    lastname = serializers.CharField(allow_null=True, allow_blank=True)
    age = serializers.CharField(allow_null=True, allow_blank=True)
    email = serializers.CharField(allow_null=True, allow_blank=True)
    # avatar = serializers.CharField(allow_null=True, allow_blank=True)
    # birthplace=serializers.CharField(allow_null=True, allow_blank=True)
    blood_group=serializers.CharField(allow_null=True, allow_blank=True)
    country=serializers.CharField(allow_null=True, allow_blank=True)
    state=serializers.CharField(allow_null=True, allow_blank=True)
    city=serializers.CharField(allow_null=True, allow_blank=True)
    gender=serializers.CharField(allow_null=True, allow_blank=True)
    height=serializers.CharField(allow_null=True, allow_blank=True)
    weight=serializers.CharField(allow_null=True, allow_blank=True)
    aadhar_number=serializers.CharField(allow_null=True, allow_blank=True)
    address_line_1=serializers.CharField(allow_null=True, allow_blank=True)
    # admission_number = serializers.CharField(allow_null=True, allow_blank=True)
    date_of_admission= serializers.CharField(allow_null=True, allow_blank=True)
    date_of_birth=serializers.CharField(allow_null=True, allow_blank=True)
    phone = serializers.CharField(allow_null=True, allow_blank=True)
    pincode=serializers.CharField(allow_null=True, allow_blank=True)
    # date_of_joining=serializers.CharField(allow_null=True, allow_blank=True)
    grade_id=serializers.CharField(allow_null=True, allow_blank=True)
    user_id=serializers.CharField(allow_null=True, allow_blank=True)
    cast_category=serializers.CharField(allow_null=True, allow_blank=True)
    religion=serializers.CharField(allow_null=True, allow_blank=True)
    # sub_cast=serializers.CharField(allow_null=True, allow_blank=True)
    
    def to_internal_value(self, data):
        internal_data = copy.deepcopy(data)
        if internal_data.get("aadhar_number", None) == None:
            internal_data['aadhar_number'] = None
            
        if internal_data.get("firstname", None) == None:
            internal_data['firstname'] = None
        
        if internal_data.get("middlename", None) == None:
            internal_data['middlename'] = None

        if internal_data.get("lastname", None) == None:
            internal_data['lastname'] = None
        
        if internal_data.get("email", None) == None:
            internal_data['email'] = None

        if internal_data.get("phone", None) == None:
            internal_data['phone'] = None

        if internal_data.get("address_line_1", None) == None:
            internal_data['address_line_1'] = None
        
        if internal_data.get("country", None) == None:
            internal_data['country'] = None
        
        if internal_data.get("state", None) == None:
            internal_data['state'] = None
        
        if internal_data.get("city", None) == None:
            internal_data['city'] = None
        
        if internal_data.get("pincode", None) == None:
            internal_data['pincode'] = None
        
        if internal_data.get("date_of_birth", None) == None:
            internal_data['date_of_birth'] = None
        
        if internal_data.get("gender", None) == None:
            internal_data['gender'] = None
        
        if internal_data.get("date_of_admission", None) == None:
            internal_data['date_of_admission'] = None
        
        if internal_data.get("age", None) == None:
            internal_data['age'] = None
        
        if internal_data.get("height", None) == None:
            internal_data['height'] = None

        if internal_data.get("weight", None) == None:
            internal_data['weight'] = None
        
        if internal_data.get("blood_group", None) == None:
            internal_data['blood_group'] = None
        
        if internal_data.get("cast_category", None) == None:
            internal_data['cast_category'] = None
        
        if internal_data.get("religion", None) == None:
            internal_data['religion'] = None
        
        return super(StudentTableStructureSerilizer, self).to_internal_value(internal_data)
    def create(self, validated_data):
        request_data = copy.deepcopy(validated_data)
        
        with transaction.atomic():
                username = validated_data['firstname']+validated_data['lastname']+''.join([random.choice(string.digits) for i in range(0, 4)])
                password = request_data['firstname'][0:4] + \
                    ''.join([random.choice(string.digits) for i in range(0, 4)])
                password = "dummy@123"
                
                user = User.objects.create(username=username, email=validated_data['email'],
                                        phone=validated_data['phone'], is_student=True)
                user.set_password(password)
                user.save()
                StudentTableStructure.objects.create(
                    student=user,
                    aadhar_number=validated_data['aadhar_number'],
                    firstname=validated_data['firstname'],
                    middlename=validated_data['middlename'],
                    lastname=validated_data['lastname'],
                    email=validated_data['email'],
                    phone=validated_data['phone'],
                    address_line_1=validated_data['address_line_1'],
                    country=validated_data['country'],
                    state=validated_data['state'],
                    city=validated_data['city'],
                    pincode=validated_data['pincode'],
                    date_of_birth = validated_data['date_of_birth'],
                    gender=validated_data['gender'],
                    date_of_admission = validated_data['date_of_admission'],
                    age=validated_data['age'],
                    height=validated_data['height'],
                    weight=validated_data['weight'],
                    blood_group=validated_data['blood_group'],
                    cast_category=validated_data['cast_category'],
                    religion=validated_data['religion'],
                )
                return request_data
            
    def update(self, instance, validated_data):
        instance.aadhar_number = validated_data.get('aadhar_number', instance.aadhar_number)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.middlename = validated_data.get('middlename', instance.middlename)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.date_of_birth  = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_admission = validated_data.get('date_of_admission', instance.date_of_admission)
        instance.age = validated_data.get('age', instance.age)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.cast_category = validated_data.get('cast_category', instance.cast_category)
        instance.religion = validated_data.get('religion', instance.religion)
        
        instance.save()

        return instance
    class Meta:
        model = StudentTableStructure
        fields = '__all__'

class StudentSerilizer(serializers.ModelSerializer):
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
    date_of_birth=serializers.CharField(allow_null=True, allow_blank=True)
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
                # password = request_data['firstname'][0:4] + \
                #     ''.join([random.choice(string.digits) for i in range(0, 4)])
                password = "dummy@123"

                user = User.objects.create(username=username, email=validated_data['email'],
                                        phone=validated_data['phone'], is_teacher=True)
                user.set_password(password)
                user.save()
                TeacherTableStructure.objects.create(
                    teacher=user,aadhar_number=validated_data['aadhar_number'],
                    address_line_1=validated_data['address_line_1'],
                    city=validated_data['city'],
                    country=validated_data['country'],
                    date_of_birth = validated_data['date_of_birth'],
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
        
    def update(self, instance, validated_data):
        instance.aadhar_number = validated_data.get('aadhar_number', instance.aadhar_number)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.country = validated_data.get('country', instance.country)
        instance.email = validated_data.get('email', instance.email)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.height = validated_data.get('height', instance.height)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.middlename = validated_data.get('middlename', instance.middlename)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.pan_number = validated_data.get('pan_number', instance.pan_number)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.date_of_birth  = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.date_of_joining  = validated_data.get('date_of_joining', instance.date_of_joining)
        
        instance.save()

        return instance
    class Meta:
        model = TeacherTableStructure
        fields = '__all__'
    


class TeacherShortProfileSerilizer(serializers.ModelSerializer):
     class Meta:
        model = TeacherTableStructure
        fields = ["id","email","firstname","lastname"]

class GradeTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GradeTableStructure
        fields = '__all__'

class QuestionMatchThePairsSerilizer(serializers.ModelSerializer):
    option1 = serializers.FileField(allow_null=True)
    option2 = serializers.FileField(allow_null=True)
    option3 = serializers.FileField(allow_null=True)
    option4 = serializers.FileField(allow_null=True)
    option5 = serializers.FileField(allow_null=True)
    option6 = serializers.FileField(allow_null=True)
    question1 = serializers.FileField(allow_null=True)
    question2 = serializers.FileField(allow_null=True)
    question3 = serializers.FileField(allow_null=True)
    question4 = serializers.FileField(allow_null=True)
    question5 = serializers.FileField(allow_null=True)
    question6 = serializers.FileField(allow_null=True)
    def create(self, validated_data):
        file_fields = [
            'option1', 'option2', 'option3', 'option4', 'option5', 'option6',
            'question1', 'question2', 'question3', 'question4', 'question5', 'question6'
        ]
        for field_name in file_fields:
            file_obj = validated_data.pop(field_name, None)
            if file_obj:
                filename = upload_file_to_s3(file_obj,"match_the_pair_images")
                validated_data[field_name] = filename 
        instance = QuestionMatchThePairs.objects.create(**validated_data)

        return instance
    class Meta:
        model = QuestionMatchThePairs
        fields = '__all__'

class QuestionMatchThePairsSerilizerView(serializers.ModelSerializer):
    class Meta:
      
        model = QuestionMatchThePairs
        fields = '__all__'

class QuestionMultipleChoiceQuestionsSerilizer(serializers.ModelSerializer):

    class Meta:
        model = QuestionMultipleChoiceQuestions
        fields = '__all__'

class QuestionSelectReleventPictureSerilizer(serializers.ModelSerializer):
    option1 = serializers.FileField(allow_null=True)
    option2 = serializers.FileField(allow_null=True)
    option3 = serializers.FileField(allow_null=True)
    option4 = serializers.FileField(allow_null=True)
    option5 = serializers.FileField(allow_null=True)
    option6 = serializers.FileField(allow_null=True)
    question_image=serializers.FileField(allow_null=True)
    question = serializers.CharField(allow_null=True)
    
    def create(self, validated_data):
        file_fields = [
            'option1', 'option2', 'option3', 'option4', 'option5', 'option6',
            'question_image'
        ]
        char_fields = ['question']

        for field_name in file_fields:
            file_obj = validated_data.pop(field_name, None)
            if file_obj:
                filename = upload_file_to_s3(file_obj,"relevent_picture")
                validated_data[field_name] = filename 
            
        for field_name in char_fields:
            field_value = validated_data.pop(field_name, None)
            if field_value:
                validated_data[field_name] = field_value
    
        instance = QuestionSelectReleventPicture.objects.create(**validated_data)

        return instance

    class Meta:
        model = QuestionSelectReleventPicture
        fields = '__all__'


class QuestionTableStructureSerilizerCreate(serializers.ModelSerializer):
    match_the_pairs_question = QuestionMatchThePairsSerilizer(many=False,required=False)
    multiple_choice_question = QuestionMultipleChoiceQuestionsSerilizer(many=False,required=False)
    select_relevent_picture_question = QuestionSelectReleventPictureSerilizer(read_only=False,required=False)
    chapter_id = serializers.IntegerField()
    # grade = GradeTableStructureSerilizer(read_only=False)

    def create(self, validated_data):
        # print("validated_data*******",validated_data)
        # return_data = copy.deepcopy(validated_data)
        # return super().create(validated_data)
        # print("return_data",return_data)
        if "objective" == validated_data['question_type']:
            print("inside 1st")
            objective = validated_data.pop('multiple_choice_question')
            grade_id = validated_data.pop('grade_id')
            subject_id = validated_data.pop('subject_id')
            serializer = QuestionMultipleChoiceQuestionsSerilizer(data=objective)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            id = QuestionMultipleChoiceQuestions.objects.get(id=serializer.data['id'])
            print("id**************",type(id))
            chapter_id = ChapterTableStructure.objects.get(chapter_id=validated_data['chapter_id'])
            que = QuestionTableStructure.objects.create(multiple_choice_question=id,question_type='objective',chapter_id=chapter_id, grade_id=grade_id, subject_id=subject_id)

        elif "matching_question" == validated_data['question_type']:
            print("inside matching_question")
            matching_question = validated_data.pop('match_the_pairs_question')
            grade_id = validated_data.pop('grade_id')
            subject_id = validated_data.pop('subject_id')
            serializer = QuestionMatchThePairsSerilizer(data=matching_question)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            id = QuestionMatchThePairs.objects.get(id=serializer.data['id'])
            chapter_id = ChapterTableStructure.objects.get(chapter_id=validated_data['chapter_id'])
            # id = QuestionMatchThePairsSerilizerRead(id)
            print("id**************",type(id))
            que = QuestionTableStructure.objects.create(match_the_pairs_question=id,question_type='matching_question',chapter_id=chapter_id, grade_id=grade_id, subject_id=subject_id)

        elif "relevent_picture" == validated_data['question_type']:

            relevent_picture = validated_data.pop('select_relevent_picture_question')
            print(relevent_picture,"relevent_picture")
            grade_id = validated_data.pop('grade_id')
            subject_id = validated_data.pop('subject_id')
            serializer = QuestionSelectReleventPictureSerilizer(data=relevent_picture)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            id = QuestionSelectReleventPicture.objects.get(id=serializer.data['id'])
            
            chapter_id = ChapterTableStructure.objects.get(chapter_id=validated_data['chapter_id'])
            que = QuestionTableStructure.objects.create(select_relevent_picture_question=id,question_type='relevent_picture',chapter_id=chapter_id, grade_id=grade_id, subject_id=subject_id)
        
        return que
    class Meta:
        model = QuestionTableStructure
        fields = '__all__'


class SubjectTableStructureSerilizer(serializers.ModelSerializer):
    grade_id = serializers.IntegerField()
    # updateddate = serializers.DateField(allow_null=True)
    # createdby = serializers.IntegerField(allow_null=True)
    # updatedby = serializers.IntegerField(allow_null=True)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    # subject_code = serializers.CharField(allow_null=True)


    def create(self, validated_data):
        return_data = copy.deepcopy(validated_data)
        grade_id = GradeTableStructure.objects.get(grade_id=validated_data['grade_id'])
        SubjectTableStructure.objects.create(name=validated_data['name'], grade_id=grade_id)
        return return_data
    class Meta:
            model = SubjectTableStructure
            fields =  '__all__'

class ChapterTableStructureSerilizer(serializers.ModelSerializer):
    subject_id = serializers.IntegerField()
    # updateddate = serializers.DateField(allow_null=True)
    # createdby = serializers.IntegerField(allow_null=True)
    # updatedby = serializers.IntegerField(allow_null=True)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    # chapter_code = serializers.CharField(allow_null=True)
    def create(self, validated_data):
        return_data = copy.deepcopy(validated_data)
        subject_id = SubjectTableStructure.objects.get(subject_id=validated_data['subject_id'])
        ChapterTableStructure.objects.create(name=validated_data['name'], subject_id=subject_id)
        return return_data
    class Meta:
            model = ChapterTableStructure
            fields =  '__all__'


class ListSubjectTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
            model = SubjectTableStructure
            fields =  '__all__'

class ListChapterTableStructureSerilizer(serializers.ModelSerializer):
    class Meta:
            model = ChapterTableStructure
            fields =  '__all__'

class SubjectListSerilizer(serializers.Serializer):
    name = serializers.CharField()
    subject_id = serializers.IntegerField()

class ChapterListSerilizer(serializers.Serializer):
    name = serializers.CharField()
    chapter_id = serializers.IntegerField()
    
class SubjectListAllserializer(serializers.ModelSerializer):
    grade_id = GradeTableStructureSerilizer()
    class Meta:
            model = SubjectTableStructure
            fields =  '__all__'
            
class SubjectTableStructureSerilizerForChapter(serializers.ModelSerializer):
    grade_id = GradeTableStructureSerilizer()
    class Meta:
            model = SubjectTableStructure
            fields =  ["name","subject_id","grade_id","subject_code"]
            
class ChapterListAllSerializer(serializers.ModelSerializer):
    subject_id = SubjectTableStructureSerilizerForChapter()
    class Meta:
            model = ChapterTableStructure
            fields =  ["name","chapter_id","subject_id","chapter_code"]
class QuestionTableStructureSerilizer(serializers.ModelSerializer):
    match_the_pairs_question = QuestionMatchThePairsSerilizerView(read_only=True)
    multiple_choice_question = QuestionMultipleChoiceQuestionsSerilizer(read_only=True)
    select_relevent_picture_question = QuestionSelectReleventPictureSerilizer(read_only=True)
    chapter_id = ChapterListAllSerializer()

    class Meta:
        model = QuestionTableStructure
        fields = '__all__'
        
class AssessmentTableStructureSerilizer(serializers.ModelSerializer):
    chapter_id = ChapterListAllSerializer()
    teacher_id = TeacherShortProfileSerilizer()
    questions = QuestionTableStructureSerilizer(many=True, read_only=True)
    class Meta:
            model = AssessmentTableStructure
            fields =  '__all__'
            
class TeacherSerilizer(serializers.ModelSerializer):
    teacher_assessment = AssessmentTableStructureSerilizer(many=True)
    class Meta:
        model = TeacherTableStructure
        fields = '__all__'
        
class AssessmentTableStructureSerilizerCreate(serializers.ModelSerializer):
    chapter_id = serializers.IntegerField()
    teacher_id = serializers.IntegerField()
    questions =  serializers.ListField()
    def create(self, validated_data):
        return_data = copy.deepcopy(validated_data)

        related_ids = validated_data.get('questions', [])
        related_objects = QuestionTableStructure.objects.filter(pk__in=related_ids)
        print("related_objects",related_objects)

        chapter_id = ChapterTableStructure.objects.get(chapter_id=validated_data['chapter_id'])
        teacher_id = TeacherTableStructure.objects.get(id=validated_data['teacher_id'])
        assessment = AssessmentTableStructure.objects.create(name=validated_data['name'], chapter_id = chapter_id,standard = validated_data['standard'],subject = validated_data['subject'], teacher_id = teacher_id,question_type = validated_data['question_type'], date = validated_data['date'], end_time = validated_data['end_time'], start_time = validated_data['start_time'], marks = validated_data['marks'], grade_id = validated_data['grade_id'], test_duration = validated_data['test_duration'], title = validated_data['title'], test_type = validated_data['test_type'], test_category = validated_data['test_category'], int_ext_type = validated_data['int_ext_type'])
        assessment.questions.set(related_objects)
        return return_data
    class Meta:
            model = AssessmentTableStructure
            fields =  '__all__'

class ChapterTableStructureSerilizerUpdate(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.updateddate = validated_data.get('updateddate', instance.updateddate)
        instance.createdby = validated_data.get('createdby', instance.createdby)
        instance.updatedby = validated_data.get('updatedby', instance.updatedby)
        instance.subject_id = validated_data.get('subject_id', instance.subject_id)
        instance.chapter_code = validated_data.get('chapter_code', instance.chapter_code)
        instance.save()
        return instance
    class Meta:
            model = ChapterTableStructure
            fields =  '__all__'
            
class SubjectTableStructureSerilizerUpdate(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.updateddate = validated_data.get('updateddate', instance.updateddate)
        instance.createdby = validated_data.get('createdby', instance.createdby)
        instance.updatedby = validated_data.get('updatedby', instance.updatedby)
        instance.grade_id = validated_data.get('grade_id', instance.grade_id)
        instance.subject_code = validated_data.get('subject_code', instance.subject_code)
        instance.save()
        return instance
    class Meta:
            model = SubjectTableStructure
            fields =  '__all__'

class TeacherAsessessmentSerializer(serializers.ModelSerializer):
    chapter_id = ChapterListAllSerializer()
    teacher_id = TeacherShortProfileSerilizer()
    questions = QuestionTableStructureSerilizer(many=True, read_only=True)
    class Meta:
        model=AssessmentTableStructure
        fields='__all__'        


class QuestionMultipleChoiceQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionMultipleChoiceQuestions
        fields="__all__"


class QuestionSelectReleventPictureSerilizer1(serializers.ModelSerializer):
    class Meta:
        model=QuestionSelectReleventPicture
        fields="__all__"

class QuestionTableStructureSerilizer1(serializers.ModelSerializer):
    multiple_choice_question=SerializerMethodField('match_the_pairs')
    select_relevent_picture_question=SerializerMethodField('select_relevent_picture_question1')
    def match_the_pairs(self,obj):
        print("obj",obj)
        obj1=model_to_dict(obj)
        print("obj",obj1)
        try:           
                math = QuestionMultipleChoiceQuestions.objects.get(
                id=obj1['multiple_choice_question'],)
                return QuestionMultipleChoiceQuestionsSerializer(math).data
        except Exception as error:
            print("doctor catgory error", error)
            return None

    def select_relevent_picture_question1(self,obj):
        print("obj1",obj)
        obj1=model_to_dict(obj)
        print("obj1",obj1)
        try:
            math = QuestionSelectReleventPicture.objects.get(
                id=obj1['select_relevent_picture_question'])
            return QuestionSelectReleventPictureSerilizer1(math).data
        except Exception as error:
            print("doctor catgory error", error)
            return None
    class Meta:
        model = QuestionTableStructure
        fields = '__all__'
        
class StudentSideAssessmentListSerializer(serializers.ModelSerializer):
    questions = QuestionTableStructureSerilizer1(many=True, read_only=True)
    class Meta:
        model=AssessmentTableStructure
        fields='__all__'  


class ListQuestionSelectReleventPictureSerilizer(serializers.ModelSerializer):
    select_relevent_picture_question=SerializerMethodField('question_details')
    def question_details(self,obj):
        print("obj",obj)
        obj1=model_to_dict(obj)
        print("obj",obj1)
        class QuestionTableStructureSerilizer(serializers.ModelSerializer):
            chapter_id = ChapterListAllSerializer()            
            class Meta:
                model = QuestionTableStructure
                fields = '__all__'
        try:
            question = QuestionTableStructure.objects.get(
                select_relevent_picture_question_id=obj.id)
            print("question",question)
            return QuestionTableStructureSerilizer(question).data
        except Exception as error:
            print("error", error)
            return None
    class Meta:
        model=QuestionSelectReleventPicture
        fields='__all__'