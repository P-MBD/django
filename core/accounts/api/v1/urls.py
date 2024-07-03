from django.urls import path, include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
app_name = 'api-v1'
urlpatterns = [
    #registrtion
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login', ObtainAuthToken.as_view(), name='token-login')
    #change password
    #reset password
    #login token 
    #login jwt


]
                    