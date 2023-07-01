from django.forms.models import model_to_dict
import boto3
import random
import datetime
import tempfile
import os
import string
from django.conf import settings

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


def upload_file_to_s3(files):
    s3 = boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )
    try:
        file_name = files.name
        get_file_extension=file_ext
        file_ext = get_file_extension(file_name)
        tmpdir = tempfile.mkdtemp()
        predictable_filename = 'story_images.'+str(file_ext)
        path = os.path.join(tmpdir, predictable_filename)
        try:
            with open(path, "wb+") as tmp:
                tmp.write(files.read())
        except Exception as e:
            print(e) 
        ct = datetime.now()
        ts = ct.timestamp()
        Final_name = file_name.replace(' ', '_')
        S3file_name = str(ts)+"_"+str(Final_name)
        print("====S3====", S3file_name)
        urls = []
        s3.upload_file(path,"jps-shishu", S3file_name,
                       ExtraArgs={'ACL': 'public-read'})
        os.remove(path)
        # os.remove(tmpdir)
        return S3file_name
    except Exception as e:
         print("e=======", e)