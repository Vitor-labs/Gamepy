"""Views and Endpoints logics Definitions"""
import os
import jwt

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import HttpResponsePermanentRedirect

from rest_framework import generics, status, views, viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    RegisterSerializer, SetNewPasswordSerializer,
    ResetPasswordEmailRequestSerializer, EmailVerificationSerializer,
    LoginSerializer, LogoutSerializer, UserSerializer )
from .models import CustomUser
from .renderers import UserRenderer
from .utils import Utils


class CustomRedirect(HttpResponsePermanentRedirect):
    """Class to dinamic redirect"""
    allowed_schemes = [os.getenv('APP_SCHEME'), 'http', 'https']


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class RegisterView(generics.GenericAPIView):
    """
    API endpoint that sends users an email to be varified.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = (UserRenderer,)

    def post(self, request):
        """POST Method"""
        user = request.data
        serializer = self.serializer_class(data=user)

        if serializer.is_valid():
            serializer.save()

            user_data = serializer.data

            user = CustomUser.objects.get(email=user_data['email'])
            refresh = RefreshToken.for_user(user)
            current_site = get_current_site(request)
            relative_link = reverse('email-verification')

            absolute_url = 'http://' + \
                str(current_site.domain) + relative_link + \
                '?token=' + str(refresh.access_token)
            body = 'Hello' + user.username + ',\n\n' + \
                'Please click on the link below to verify your email:\n\n' + \
                absolute_url + '\n\n' + 'Thank you!'

            data = {
                'email_body': body,
                'email_subject': 'Email Verification',
                'email_to': user.email
            }
            Utils.send_email(data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(views.APIView):
    """
    API endpoint that verifies user tokens and validateds him.
    """
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        """GET Method"""
        token = request.GET.get('token')
        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(pk=data['id'])
            user.is_verified = True
            user.save()

            return Response({'email': 'activation succeful'},
                            status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as exc:
            return Response({'error': 'Expired Signature', 'message': str(exc)},
                            status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError as exc:
            return Response({'error': 'Fail to Decode', 'message': str(exc)},
                            status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError as exc:
            return Response({'error': 'Invalid Token', 'message': str(exc)},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    """
    API endpoint that allows user to login.
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """POST Method"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(email=serializer.data['email'])
            if user.is_verified:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh.access_token),
                                 'access': str(refresh.access_token)},
                                status=status.HTTP_200_OK)
            return Response({'error': 'Email not verified'},
                            status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    """
    API endpoint that allows user to reques an reset password email.
    """
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """POST Method"""
        data = {'request':request, 'data':request.data}
        serializer = self.serializer_class(data=data)

        email = request.data.get('email', '')

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request=request)
            relative_link  = reverse('password-reset-confirm', 
                                   kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absolute_url  = 'http://'+ str(current_site.domain) + \
                             relative_link  +"?redirect_url=" + redirect_url
            
            body = 'Hello' + user.username + ',\n\n' + \
                   'Please click on the link below to reset your password: \n\n' + \
                    absolute_url + '\n\n' + 'Thank you!'
            
            data = {'email_body': body, 
                    'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            
            Utils.send_email(data)

        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    """
    API endpoint that allows user to check his tokens.
    """
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):
        """GET Method"""
        redirect_url = request.GET.get('redirect_url')

        try:
            _id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url+'?token_valid=False')
                return CustomRedirect(os.getenv('FRONTEND_URL', '')+'?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(redirect_url+'?token_valid=True&message=Credentials Valid&uidb64='+uidb64+'&token='+token)

            return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

        except DjangoUnicodeDecodeError:
            message={'Error': 'Token Invalid, request a new token'}        
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)

class SetNewPasswordAPIView(generics.GenericAPIView):
    """
    API endpoint that confirms if user changed his password.
    """
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        """PATCH Method"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            message = {'Success': True, 'Message': 'Password Reseted successfully'}
            return Response(message, status=status.HTTP_200_OK)

        message = {'Success': False, 'Message': 'Password not changed'}

        return Response(message, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(generics.GenericAPIView):
    """
    API endpoint that allows user to logout and clean tokens.
    """
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        "POST Method"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
