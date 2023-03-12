from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username == None:
            raise TypeError("Username not provided.")

        if email == None:
            raise TypeError("Email not provided.")

        if password == None:
            raise TypeError("Password not provided.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, email, password=None):

        if username == None:
            raise TypeError("Username not provided.")

        if email == None:
            raise TypeError("Email not provided.")

        if password == None:
            raise TypeError("Password not provided.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # we want to login using the email.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


    def __str__(self):
        return self.email

    
    def tokens(self):
        return ""

