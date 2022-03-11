from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

    def create(self, validate_data):
        user = User.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            first_name = validate_data['first_name'],
            last_name = validate_data['last_name'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','password']
    

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidatonError({'email':'This email is already Taken'})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({'username':'This Username is already taken'})
        return value

    def update(self, instance, valide_data):
        instance.first_name = valide_data['first_name']
        instance.last_name = valide_data['last_name']
        instance.username = valide_data['username']
        instance.email = valide_data['email']

        instance.save()

        return instance
