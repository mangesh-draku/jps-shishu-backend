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


def upload_file_to_s3(files):
    print("inside s3")
    s3 = boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    try:
        file_name = files.name
        tmpdir = tempfile.mkdtemp()
        predictable_filename = 'story_images.' + str(file_name)
        path = os.path.join(tmpdir, predictable_filename)
        try:
            with open(path, "wb+") as tmp:
                tmp.write(files.read())
        except Exception as e:
            print(e) 
        
        # Create the folder on S3
        folder_name = 'match_the_pair_images/'
        s3.put_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=folder_name)

        # Generate a unique file name
        ct = datetime.datetime.now()
        ts = ct.timestamp()
        Final_name = file_name.replace(' ', '_')
        S3file_name = str(ts) + "_" + str(Final_name)

        # Upload the file to the folder on S3
        s3.upload_file(path, settings.AWS_STORAGE_BUCKET_NAME, folder_name + S3file_name)

        os.remove(path)
        # os.remove(tmpdir)

        # Return the URL of the uploaded file
        url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{folder_name}{S3file_name}"
        print("url =", url)
        return url
    except Exception as e:
        print("e=======", e)