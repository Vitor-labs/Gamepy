"""Custom models for authentication app"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    """Class to model a custom manager for user model"""
    def create_user(self, username:str, email:str, password:str=None):
        """
        Creates a basic user. no admin

        Args:
            username (str): user name
            email (str): user email
            password (str, optional): user password. Defaults to None.

        Raises:
            TypeError: Username is required
            TypeError: Email is required

        Returns:
            User: user created
        """
        if username is None:
            raise TypeError('Username is required')
        if email is None:
            raise TypeError('Email is required')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, username:str, email:str, password:str=None):
        """
        Creates a super user with admin permissions

        Args:
            username (str): admin name
            email (str): admin email
            password (str, optional): admin password. If None, raises TypeError.

        Raises:
            TypeError: Password is required for superuser

        Returns:
            User: super user data
        """
        if password is None:
            raise TypeError('Password is required for superuser')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Class to model users instances in database"""
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = 'Users'

    def tokens(self):
        """Tokes for auth api. Access and Refresh"""
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
