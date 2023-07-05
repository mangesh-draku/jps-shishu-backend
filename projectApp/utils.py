from django.forms.models import model_to_dict
import os 
from django.conf import settings
import datetime
import tempfile
import boto3


def get_user_object(user):
    user = model_to_dict(user)
    del user['password']
    del user['phone_otp']
    userType = ''
    if user['is_student']:
        userType = "STUDENT"
    if user['is_teacher']:
        userType = "TEACHER"
    if user['is_admin_user'] or user['is_superuser']:
        userType = "SUPERADMIN"
    user['user_type'] = userType
    return user

# def upload_file_to_s3(files):
#     print("inside s3")
#     s3 = boto3.client('s3',
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#     )
#     try:
#         file_name = files.name
#         tmpdir = tempfile.mkdtemp()
#         predictable_filename = 'story_images.'+str(file_name)
#         path = os.path.join(tmpdir, predictable_filename)
#         try:
#             with open(path, "wb+") as tmp:
#                 tmp.write(files.read())
#         except Exception as e:
#             print(e) 
#         ct = datetime.datetime.now()
#         ts = ct.timestamp()
#         Final_name = file_name.replace(' ', '_')
#         S3file_name = str(ts)+"_"+str(Final_name)
#         urls = []
#         s3.upload_file(path,settings.AWS_STORAGE_BUCKET_NAME, S3file_name)
#         os.remove(path)
#         # os.remove(tmpdir)
#         print("url = ",f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{S3file_name}")
#         return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{S3file_name}"
#         return S3file_name
#     except Exception as e:
#          print("e=======", e)








def upload_file_to_s3(files,folderName):
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                         
                          )
        file_name = files.name
       
        tmpdir = tempfile.mkdtemp()
        predictable_filename = 'story_images.'+str(file_name)
        path = os.path.join(tmpdir, predictable_filename)
        try:
            with open(path, "wb+") as tmp:
                tmp.write(files.read())
        except Exception as e:
            print(e)
        ct = datetime.datetime.now()
        ts = ct.timestamp()
        Final_name = file_name.replace(' ', '_')
        S3file_name = folderName + '/' + str(ts)+"_"+str(Final_name)
        print("====S3====", S3file_name)
        urls = []
        s3.upload_file(path,settings.AWS_STORAGE_BUCKET_NAME, S3file_name,
                       ExtraArgs={'ACL': 'public-read'})
        os.remove(path)
        print("url = ",f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{S3file_name}")
        return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{S3file_name}"
        
        # os.remove(tmpdir)
        return S3file_name
    except Exception as e:
        print("e=======", e)

