"""daddyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from myapp import views
# from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm, reset_password_validate_token
# from django.contrib.auth import views as auth_views


from rest_framework.authtoken import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('v1/admin/', admin.site.urls),
    path('',include('myapp.urls')),
    #path('login', views.login, name='login'),
    path('v1/api-token-auth', views.obtain_auth_token),
    #path('v1/api/password_reset', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('v1/api/password_reset', auth_views.password_reset, name='password_reset'),
    # path('v1/api/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # path('v1/api/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('accounts/', include('django.contrib.auth.urls')),    

    path('v1/api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/api/token/verify', TokenVerifyView.as_view(), name='token_verify'),

    # path('validate_token', reset_password_validate_token, name="reset-password-validate"),
    # path('^confirm', reset_password_confirm, name="reset-password-confirm"),
    # path('', reset_password_request_token, name="reset-password-request"),
]
