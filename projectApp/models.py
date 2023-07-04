from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(
        max_length=20, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin_user = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_date = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    phone_otp = models.CharField(max_length=4, default="")
    email_otp = models.CharField(max_length=4, default="")
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    first_time = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length=20, null=True, blank=True,default="")

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        db_table = "User"
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class StudentTableStructure(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255,null=True,default=None)
    middlename = models.CharField(max_length=255,null=True,default=None)
    lastname = models.CharField(max_length=255,null=True,default=None)
    age = models.CharField(max_length=255,null=True,default=None)
    email = models.CharField(max_length=255,null=True,default=None)
    # avatar = models.CharField(max_length=255,null=True,default=None)
    # birthplace = models.CharField(max_length=255,null=True,default=None)
    blood_group = models.CharField(max_length=255,null=True,default=None)
    # caste = models.CharField(max_length=255,null=True,default=None)
    city = models.CharField(max_length=255,null=True,default=None)
    country = models.CharField(max_length=255,null=True,default=None)
    gender = models.CharField(max_length=255,null=True,default=None)
    height = models.CharField(max_length=255,null=True,default=None)
    weight = models.CharField(max_length=255,null=True,default=None)
    aadhar_number =  models.CharField(max_length=255,null=True, default=None)
    address_line_1 = models.CharField(max_length=255,null=True, default=None)
    # admission_number = models.CharField(max_length=255,null=True,default=None)
    date_of_admission= models.DateTimeField (default=timezone.now, null=True, blank=True)
    date_of_birth = models.DateTimeField (default=timezone.now, null=True, blank=True)
    # app_token= models.CharField(max_length=255,null=True,default=None)
    # mode_of_transport = models.CharField(max_length=255,null=True,default=None)
    # mother_tongue = models.CharField(max_length=255,null=True,default=None)
    # nationality = models.CharField(max_length=255,null=True,default=None)
    # permanent_registration_number = models.CharField(max_length=255,null=True,default=None)
    phone = models.CharField(max_length=255,null=True,default=None)
    pincode = models.CharField(max_length=255,null=True,default=None)
    religion = models.CharField(max_length=255,null=True,default=None)
    # school_house = models.CharField(max_length=255,null=True,default=None)
    state = models.CharField(max_length=255,null=True,default=None)
    grade_id = models.IntegerField(default=None, null=True, blank=True)
    user_id = models.IntegerField(default=None, null=True, blank=True)
    cast_category =models.CharField(max_length=255,null=True,default=None)
    # sub_cast =models.CharField(max_length=255,null=True,default=None)
    createddate = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updateddate  = models.DateField(default=None, null=True, blank=True)
    createdby = models.IntegerField(default=None, null=True, blank=True)
    updatedby = models.IntegerField(default=None, null=True, blank=True)
    class Meta:
        db_table = "student_table_structure"

class TeacherTableStructure(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updateddate = models.DateField(default=None, null=True, blank=True)
    createdby = models.IntegerField(default=None, null=True, blank=True)
    updatedby = models.IntegerField(default=None, null=True, blank=True)
    aadhar_number = models.CharField(max_length=255,null=True, default=None)
    address_line_1 = models.CharField(max_length=255,null=True, default=None)
    app_token = models.CharField(max_length=255,null=True,default=None)
    # avatar = models.CharField(max_length=255,null=True,default=None)
    city = models.CharField(max_length=255,null=True,default=None)
    country = models.CharField(max_length=255,null=True,default=None)
    date_of_birth = models.DateTimeField (default=timezone.now, null=True, blank=True)
    date_of_joining = models.DateTimeField (default=timezone.now, null=True, blank=True)
    email= models.CharField(max_length=255,null=True,default=None)
    employee_id= models.CharField(max_length=255,null=True,default=None)
    designation= models.CharField(max_length=255,null=True,default=None)
    father_name= models.CharField(max_length=255,null=True,default=None)
    firstname= models.CharField(max_length=255,null=True,default=None)
    gender= models.CharField(max_length=255,null=True,default=None)
    height = models.CharField(max_length=255,null=True,default=None)
    lastname = models.CharField(max_length=255,null=True,default=None)
    marital_status = models.CharField(max_length=255,null=True,default=None)
    middlename = models.CharField(max_length=255,null=True,default=None)
    mobile = models.CharField(max_length=255,null=True,default=None)
    pan_number = models.CharField(max_length=255,null=True,default=None)
    phone = models.CharField(max_length=255,null=True,default=None)
    pincode = models.CharField(max_length=255,null=True,default=None)
    spause_name = models.CharField(max_length=255,null=True,default=None)
    state = models.CharField(max_length=255,null=True,default=None)
    weight = models.CharField(max_length=255,null=True,default=None)
    user_id =  models.IntegerField(default=None, null=True, blank=True)
    batch_id =  models.IntegerField(default=None, null=True, blank=True)
    class Meta:
        db_table = "teacher_table_structure"




class QuestionSelectReleventPicture(models.Model):
    option1 = models.TextField(max_length=500, blank=True, null=True)
    option2 = models.TextField(max_length=500, blank=True, null=True)
    option3 = models.TextField(max_length=500, blank=True, null=True)
    option4 = models.TextField(max_length=500, blank=True, null=True)
    option5 = models.TextField(max_length=500, blank=True, null=True)
    option6 = models.TextField(max_length=500, blank=True, null=True)
    question = models.TextField(max_length=500, blank=True, null=True)
    option_count = models.TextField(max_length=500, blank=True, null=True)
    mark = models.IntegerField(default=None, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, default=None)
    class Meta:
        db_table = "select_relevent_picture_table_structure"
    

class QuestionMatchThePairs(models.Model):
    question1 = models.TextField(max_length=500, blank=True, null=True)
    question2 = models.TextField(max_length=500, blank=True, null=True)
    question3 = models.TextField(max_length=500, blank=True, null=True)
    question4 = models.TextField(max_length=500, blank=True, null=True)
    question5 = models.TextField(max_length=500, blank=True, null=True)
    question6 = models.TextField(max_length=500, blank=True, null=True)
    option1 = models.TextField(max_length=500, blank=True, null=True)
    option2 = models.TextField(max_length=500, blank=True, null=True)
    option3 = models.TextField(max_length=500, blank=True, null=True)
    option4 = models.TextField(max_length=500, blank=True, null=True)
    option5 = models.TextField(max_length=500, blank=True, null=True)
    option6 = models.TextField(max_length=500, blank=True, null=True)
    question1 = models.TextField(max_length=500, blank=True, null=True)
    question2 = models.TextField(max_length=500, blank=True, null=True)
    question3 = models.TextField(max_length=500, blank=True, null=True)
    question4 = models.TextField(max_length=500, blank=True, null=True)
    question5 = models.TextField(max_length=500, blank=True, null=True)
    question6 = models.TextField(max_length=500, blank=True, null=True)
    question = models.TextField(max_length=500, blank=True, null=True)
    option_count = models.TextField(max_length=500, blank=True, null=True)
    mark = models.IntegerField(default=None, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, default=None)
    chapter_name = models.CharField(max_length=255, null=True, default=None)
    grade = models.CharField(max_length=255, null=True, default=None)
    subject_name = models.CharField(max_length=255, null=True, default=None)
    class Meta:
        db_table = "match_the_pair_table_structure"


class QuestionMultipleChoiceQuestions(models.Model):
    option1 = models.TextField(max_length=500, blank=True, null=True)
    option2 = models.TextField(max_length=500, blank=True, null=True)
    option3 = models.TextField(max_length=500, blank=True, null=True)
    option4 = models.TextField(max_length=500, blank=True, null=True)
    option5 = models.TextField(max_length=500, blank=True, null=True)
    option6 = models.TextField(max_length=500, blank=True, null=True)
    question = models.TextField(max_length=500, blank=True, null=True)
    option_count = models.TextField(max_length=500, blank=True, null=True)
    mark = models.IntegerField(default=None, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, default=None)
    class Meta:
        db_table = "multiple_choice_question_table_structure"


class GradeTableStructure(models.Model):
     grade_id=models.AutoField(primary_key=True, db_column='grade_id')
     createddate = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
     updateddate  = models.DateField(default=None, null=True, blank=True)
     createdby = models.IntegerField(default=None, null=True, blank=True)
     updatedby = models.IntegerField(default=None, null=True, blank=True)
     name = models.CharField(max_length=255,null=True, default=None)
     grade_code = models.CharField(max_length=255,null=True, default=None)
     student = models.ManyToManyField(StudentTableStructure,blank=True)
     teacher = models.ManyToManyField(TeacherTableStructure,blank=True)
     class Meta:
        db_table = "grade_table_structure"  
        
class SubjectTableStructure(models.Model):
    subject_id = models.AutoField(primary_key=True, db_column='subject_id')
    createddate = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updateddate = models.DateField(default=None, null=True, blank=True)
    createdby = models.IntegerField(default=None, null=True, blank=True)
    updatedby = models.IntegerField(default=None, null=True, blank=True)
    grade_id = models.ForeignKey(GradeTableStructure, on_delete=models.CASCADE,related_name="grade",null=True,blank=True)
    name = models.CharField(max_length=255,null=True, default=None)
    subject_code = models.CharField(max_length=255,null=True, default=None)

    class Meta:
        db_table = "subject_table_structure"

class ChapterTableStructure(models.Model):
    chapter_id = models.AutoField(primary_key=True, db_column='chapter_id')
    createddate = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updateddate = models.DateField(default=None, null=True, blank=True)
    createdby = models.IntegerField(default=None, null=True, blank=True)
    updatedby = models.IntegerField(default=None, null=True, blank=True)
    subject_id = models.ForeignKey(SubjectTableStructure, on_delete=models.CASCADE,related_name="subject",null=True,blank=True)
    name = models.CharField(max_length=255,null=True, default=None)
    chapter_code = models.CharField(max_length=255,null=True, default=None)

    class Meta:
        db_table = "chapter_table_structure"

class AssessmentTableStructure(models.Model):
    name= models.CharField(max_length=255,null=True,default=None)
    standard= models.CharField(max_length=255,null=True,default=None)
    subject= models.CharField(max_length=255,null=True,default=None)
    subject_id= models.IntegerField(default=None, null=True, blank=True)
    teacher_id = models.ForeignKey(TeacherTableStructure, on_delete=models.CASCADE,related_name="teacher_assessment",null=True,blank=True)
    question_type= models.CharField(max_length=255,null=True,default=None)
    start_time= models.TimeField(default=None, null=True, blank=True)
    end_time= models.TimeField(default=None, null=True, blank=True)
    date= models.DateTimeField(default=timezone.now, null=True, blank=True)
    marks= models.IntegerField(default=None, null=True, blank=True)
    grade_id= models.IntegerField(default=None, null=True, blank=True)
    test_duration= models.IntegerField(default=None, null=True, blank=True)
    title = models.CharField(max_length=255,null=True,default="Assessment")
    chapter_id = models.ForeignKey(ChapterTableStructure, on_delete=models.CASCADE,related_name="chapter_assesment",null=True,blank=True)
    test_type = models.CharField(max_length=255,null=True,default=None)
    test_category = models.CharField(max_length=255,null=True,default=None)
    int_ext_type = models.CharField(max_length=255,null=True,default=None)

    class Meta:
        db_table = "assessment_table_structure"

class QuestionTableStructure(models.Model):
    question_id = models.AutoField(primary_key=True, db_column='question_id')
    createddate = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updateddate = models.DateField(default=None, null=True, blank=True)
    createdby = models.IntegerField(default=None, null=True, blank=True)
    updatedby = models.IntegerField(default=None, null=True, blank=True)
    question_type = models.CharField(max_length=255,null=True,default=None)
    grade_id = models.IntegerField(default=None, null=True, blank=True)
    subject_id = models.IntegerField(default=None, null=True, blank=True)
    assessment = models.ForeignKey(AssessmentTableStructure, on_delete=models.CASCADE,related_name="questions",null=True,blank=True)
    chapter_id = models.ForeignKey(ChapterTableStructure, on_delete=models.CASCADE,related_name="chapter",null=True,blank=True)
    select_relevent_picture_question = models.ForeignKey(QuestionSelectReleventPicture, on_delete=models.CASCADE,related_name="select_relevent_picture_question",null=True,blank=True)
    match_the_pairs_question = models.ForeignKey(QuestionMatchThePairs, on_delete=models.CASCADE,related_name="match_the_pairs_question",null=True,blank=True)
    multiple_choice_question = models.ForeignKey(QuestionMultipleChoiceQuestions, on_delete=models.CASCADE,related_name="multiple_choice_question",null=True,blank=True)

    class Meta:
        db_table = "question_table_structure"




  
