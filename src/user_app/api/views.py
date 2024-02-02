from rest_framework.decorators import api_view
from rest_framework.response import Response 
from user_app.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(["POST", ])
def registerview(request):

    if request.method == "POST":
        data = {}
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Sucessful"
            data["username"] = account.username
            data["email"] = account.email
            data["token"] = Token.objects.get(user=account).key

            return Response(data)
        data = serializer.errors
        return Response(data)

@api_view(["POST",])
def logoutview(request):

    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "Logout Sucessful"},status=status.HTTP_200_OK)