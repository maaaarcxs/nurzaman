from rest_framework.generics import (GenericAPIView,
                                    CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from accounts.models import User, OTPVerification
from .serializers import (RegisterSerializer,
                          ProfileSerializer,
                          LoginSerializer,
                          GenericChangePasswordSerializer,
                          DeactivateAccountSerializer,
                           SendResetPasswordSerializer,
                        ResetPasswordSerializer,
                        VerifyPasswordResetOTPSerializer,)
from api.main.serializers import ApartmentSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accounts.models import PasswordResetCode
import random
from django.utils.timezone import now
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

 
class ProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializers_class = ProfileSerializer
    permission_classes = (IsAuthenticated)

    def get_object(self):
        return self.request.user
    

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    

class ChangePasswordView(GenericAPIView):
    serializer_class = GenericChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        request.user.set_password(serializer.validated_data['new_password'])
        request.user_save()

        return Response({"message": "Пароль успешно изменён"})
    

class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({"message": "Вы вышли из аккаунта"})
    

class DeactivateAccountView(GenericAPIView):
    serializer_class = DeactivateAccountSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not serializer.validated_data('confirm'):
            return Response({"error": "Подтвердите деактивацию"}, status=400)
        
        request.user.is_activate = False
        request.user.save()

        return Response({"message": "Аккаунт деактивирован"})


class RequestPasswordResetView(GenericAPIView):
    serializer_class = SendResetPasswordSerializer
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)

        email = serializer.validated_data.get('email', None)

        if not email:
            return Response({"message":"Необходимо указать email"}, status=status.HTTP_400_BAD_REQUEST)
        
        if email and not User.objects.filter(email=email).exists():
            return Response({"message":" Пользователь с таким именем не найден"}, status=status.HTTP_400_BAD_REQUEST)
        
        code = str(random.randint(1000, 9999))
        OTPVerification.objects.update_or_create(
            email=email,
            defaults={'code':code, 'created_at':now()}
        )

        message = f"Ваш код для сброса пароля: {code}"

        if email:
            response = send_mail(
                subject="Востановление пароля",
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )

            if response == 0:
                return Response({"message":"Неудалось отправить код на email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"message":"Код успешно отправлен на email"}, status=status.HTTP_200_OK)



class VerifyPasswordResetOTPView(GenericAPIView):
    serializer_class = VerifyPasswordResetOTPSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        email = serializer.validated_data.get('email', None)
        code = serializer.validated_data['code']

        try:
            if email:
                code_record = OTPVerification.objects.get(email=email, code=code)
            else:
                return Response({"message":"Необходимо указать email"}, status=status.HTTP_400_BAD_REQUEST)
            
            if code_record.is_expired():
                code_record.delete()
                return Response({"message":"Срок действий кода истек"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message":"Код успешно проверен"}, status=status.HTTP_200_OK)
        
        except OTPVerification.DoesNotExist:
            return Response({"message":"Неверный код"}, status=status.HTTP_400_BAD_REQUEST)



class ResetPasswordView(GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        email = serializer.validated_data.get('email', None)
        code = serializer.validated_data['code']
        new_password = serializer.validated_data['new_password']

        try:
            if email:
                code_record = OTPVerification.objects.get(email=email, code=code)
                user = User.objects.get(email=email)
            else:
                return Response({"message":"Необходимо указать email"}, status=status.HTTP_400_BAD_REQUEST)
            
            if code_record.is_expired():
                code_record.delete()
                return Response({"message":"Срок действий кода истек"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            code_record.delete()

            return Response({"message":"Код успешно проверен"}, status=status.HTTP_200_OK)
        
        except OTPVerification.DoesNotExist:
            return Response({"message":"Неверный код"}, status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response({"message":"Пользователь не найден"}, status=status.HTTP_400_BAD_REQUEST)