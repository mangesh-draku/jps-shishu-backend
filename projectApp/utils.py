from django.forms.models import model_to_dict

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
