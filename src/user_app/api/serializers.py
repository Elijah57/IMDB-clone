from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)

    class Meta:
        model = User 
        fields = ["username", "email", "password", "password2"]

        extra_kwargs = {
            "password2": {"write_only": True}
        }

    def save(self):

        username = self.validated_data["username"]
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        email = self.validated_data["email"]

        if password != password2 :
            raise serializers.ValidationError({"Error": "password must be same"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Error": "Email already registered with a user"})
        
        account = User(username=username, email=email)
        account.set_password(password)
        account.save()

        token = Token.objects.create(user=account)
        token.save() 

        return account


                    

            