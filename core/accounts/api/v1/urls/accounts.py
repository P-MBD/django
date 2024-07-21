from django.urls import path, include
from .. import views

# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "api-v1"
urlpatterns = [
    # registrtion
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    path("test-email", views.TestEmailSend.as_view(), name="test-email"),
    # activation
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    # resend activation
    path(
        "activation/resend/",
        views.ActivationResendApiView.as_view(),
        name="activation-resend",
    ),
    # path('activation/resend')
    # change password
    path(
        "password-change/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # reset password
    # login token
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token-login",
    ),
    path(
        "token/logout",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    # login jwt
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenRefreshView.as_view(), name="jwt-verify"),
]
