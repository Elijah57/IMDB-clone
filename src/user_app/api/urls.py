from django.urls import path
from user_app.api.views import registerview, logoutview
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", registerview, name="register"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", logoutview, name="logout")
]