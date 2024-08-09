from django.db import models
from django.contrib.auth.models import AbstractUser
from shared.models import BaseModel

ORDINARY_USER, MANAGER, ADMIN = 'ordinary_user', 'manager', 'admin'

VIA_PHONE, VIA_EMAIL = 'via_phone', 'via_email'

NEW, CODE_VERIFIED, DONE, PHOTO_STEP = 'new', 'code_verified', 'done', 'photo_step'

class UserModel(AbstractUser, BaseModel):

    USER_ROLES = (
        (ORDINARY_USER, ORDINARY_USER),
        (MANAGER, MANAGER),
        (ADMIN, ADMIN)
    )
    
    AUTH_TYPE = (
        (VIA_PHONE, VIA_PHONE),
        (VIA_EMAIL, VIA_EMAIL)
    )

    AUTH_STATUS = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
        (PHOTO_STEP, PHOTO_STEP)
    )

    user_roles = models.CharField(max_length=50, choices=USER_ROLES, default=ORDINARY_USER)
    auth_type = models.CharField(max_length=50, choices=AUTH_TYPE)
    auth_status = models.CharField(max_length=50, choices=AUTH_STATUS, default=NEW)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
    photo = models.ImageField(upload_to='users_image/', null=True, blank=True)
    