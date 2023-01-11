# custom_serializers.py
from django.contrib.auth import get_user_model, authenticate
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

#class CustomRegisterSerializer(RegisterSerializer):
#    def create(self, validated_data):
#       email = validated_data['email']
#        password = validated_data['password']
#        user = user.objects.create_user(email=email, password=password)
#        return user

class CustomLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['username']
        self.fields['email'] = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # try to authenticate with email and password
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if user:
                # login was successful
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs

