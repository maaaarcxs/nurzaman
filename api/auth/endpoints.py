from django.urls import path
from .api import custom_login, custom_register, custom_logout, test_email_send, profile, change_password
from .generic_api import RequestPasswordResetView, VerifyPasswordResetOTPView, ResetPasswordView


urlpatterns = [
    path('login/', custom_login, name='custom-login'),
    path('register/', custom_register, name='custom-register'),
    path('logout/', custom_logout, name='custom-logout'),
    path('test-email-send/', test_email_send, name='test-email-send'),
    path('password-reset/request/', RequestPasswordResetView.as_view(), name='request-password-reset'),
    path('password-reset/verify/', VerifyPasswordResetOTPView.as_view(), name='verify-password-reset'),
    path('password-reset/complete/', ResetPasswordView.as_view(), name='complete-password-reset'),
    path('profile/', profile, name='profile'),
    path('change-password/', change_password, name='change-password'),
]   