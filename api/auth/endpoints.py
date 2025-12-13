from django.urls import path
from .api import custom_login, custom_register, custom_logout, profile
from .generic_api import RegisterView, ProfileView, LoginView, ChangePasswordView, DeactivateAccountView
url_patterns = [
    path('login/', LoginView.as_view(), name="custom_login"),
    path('register/', RegisterView.as_view(), name="custom_register"),
    path('logout/', custom_logout, name="custom_logout"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('change-password/', ChangePasswordView.as_view(), name="change_password"),
    path("deactivate-account/", DeactivateAccountView.as_view())
]
