from django.contrib.auth import authenticate

from django.core import exceptions
from rest_framework import serializers
from .models import *



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class UserLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'email', 'username']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = '__all__'



class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email', 'password']


class LoginSerializer(serializers.Serializer):
  
   def validate(self, data):
      username=data.get("username","")
      password=data.get("password","")
   
      if username and password:
           user=authenticate(username=username, password=password)
           if user:
                  if user.is_active:
                   data["user"]=user
                  else:
                   msg="user is deactivated."
                   raise exceptions.ValidationError(msg)
           else:
            msg="unable to login with given credentials"
            raise exceptions.ValidationError(msg)
      else:
            msg="must provide username and password"
            raise exceptions.ValidationError(msg)
      return data


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



# Role serializer for user

# class RoleSerializerforuserSerializer(serializers.ModelSerializer):
#     role_user=UsersSerializer
#     class Meta:
#         model = RoleSerializer
#         fields = ('role','name')

# class GroupSerializerforuserSerializer(serializers.ModelSerializer):
#     role=UsersSerializer
#     class Meta:
#         model = GroupSerializer
#         fields = ('role','name')


# # group serializer for user
# class GroupSerializerforuserSerializer(serializers.ModelSerializer):
#     group_user=UsersSerializer
#     class Meta:
#         model = GroupSerializer
#         fields = ('role','name','group_user')










# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields =['name']

# #from company.serializers import CompanySerializer
# class Company_UsersSeializer(serializers.ModelSerializer):
#     company=CompanySerializer()
#     class Meta:
#         model = Company_Users
#         fields =['User','company']