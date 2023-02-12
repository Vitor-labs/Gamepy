"""Serializers definitions for use cases"""
import re
from typing import Dict

from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """CustomUser model data serializer"""
    class Meta:
        """CustomUser model metadata"""
        model = CustomUser
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    """Registe a new user use case"""
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)

    class Meta:
        """CustomUser model metadata"""
        model = CustomUser
        fields = ['email', 'username', 'password']

    def validate(self, attrs:Dict)->Dict:
        """
        Validates data from resquest

        Args:
            attrs (Dict): Data to validate

        Raises:
            serializers.ValidationError: he username should only contain alphanumeric characters
            serializers.ValidationError: Not valid email format, please check if your email is correct
            serializers.ValidationError: Password too simple, add numbers, capital letters and more

        Returns:
            Dict: dictionary with validated data
        """
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('passwoed', '') | None

        email_pattern = re.compile(
            '/^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+)*\.(aero|arpa|biz|com|coop|edu|gov|info|int|mil|museum|name|net|org|pro|travel|mobi|[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/i'
            )
        password_pattern = re.compile('/^(?=[^a-z]*[a-z])(?=\D*\d)[^:&.~\s]{5,20}$/')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        if not re.fullmatch(email_pattern, email):
            raise serializers.ValidationError('Not valid email format, please check if your email is correct')
        if not password is None:
            if not re.fullmatch(password_pattern,password):
                raise serializers.ValidationError('Password too simple, add numbers, capital letters and more')
        
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    """Verify a user email use case"""
    token = serializers.CharField(max_length=555)

    class Meta:
        """CustomUser model metadata"""
        model = CustomUser
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    """Verify a user email use case"""
    email = serializers.EmailField(max_length=100, min_length=12)
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)
    username = serializers.CharField(max_length=32, min_length=8, read_only=True)

    tokens = serializers.SerializerMethodField() # read-only
    
    class Meta:
        """CustomUser model metadata"""
        model = CustomUser
        fields = ['email', 'password', 'username', 'tokens']

    def get_tokens(self, obj:Dict)->Dict:
        """
        Returns Access and Refresh tokes for an user

        Args:
            obj (Dict): json-like data of user

        Returns:
            Dict: dictionary with both tokes
        """
        user = CustomUser.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }


    def validate(self, attrs:Dict)->Dict:
        """
        Validates data from resquest

        Raises:
            AuthenticationFailed: Invalid credentials, please try again
            AuthenticationFailed: Yoyr account is disabled, contact an admin
            AuthenticationFailed: Email is not verified, please verify before login

        Args:
            attrs (Dict): Data to validate

        Returns:
            Dict: dictionary with validated data
        """
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, please try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified, please verify before login')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

#        return super().validate(attrs)
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    """Sends a email for user to reset password use case"""
    email = serializers.EmailField(min_length=2)
    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        """CustomUser model metadata"""
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    """Resets a user password use case"""
    password = serializers.CharField(min_length=8, max_length=32, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        """CustomUser model metadata"""
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs:Dict)->Dict:
        """
        Validates data from resquest

        Raises:
            AuthenticationFailed: Invalid credentials, please try again
            AuthenticationFailed: Yoyr account is disabled, contact an admin
            AuthenticationFailed: Email is not verified, please verify before login

        Args:
            attrs (Dict): Data to validate

        Returns:
            Dict: dictionary with validated data
        """
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            _id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return user

        except Exception as exc:
            raise AuthenticationFailed('The reset link is invalid', 401) from exc

#        return super().validate(attrs)
class LogoutSerializer(serializers.Serializer):
    """Logout user use case"""
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail({'bad_token':'Token is expired or invalid'})
