from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


# KTODO copy role and group models

# Create your models here.

class CofkUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, primary_key=True)

    surname = models.CharField(max_length=30, null=False, default='')
    forename = models.CharField(max_length=30, null=False, default='')
    failed_logins = models.IntegerField(null=False, default=0, blank=True)
    prev_login = models.DateTimeField(null=True, blank=True)
    login_time = models.DateTimeField(null=True, blank=True)

    # Active changed to boolean
    is_active = models.BooleanField(default=True, null=False)

    # Can be changed to email field
    email = models.EmailField(null=True)

    is_staff = models.BooleanField(default=False)  # KTODO required by django, can be remove?

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'cofk_user'


class CofkSessions(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_timestamp = models.DateTimeField()
    session_code = models.TextField(unique=True, blank=True, null=True)
    username = models.ForeignKey('CofkUser', models.DO_NOTHING, db_column='username', blank=True, null=True)

    class Meta:
        db_table = 'cofk_sessions'
