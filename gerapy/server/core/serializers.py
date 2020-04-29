'''
serializers user client project
'''

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Spider, Project, Client


class UserSerializer(serializers.ModelSerializer):
    '''user register'''
    username = serializers.CharField(
        label="用户名",
        help_text="用户名",
        required=True,
        allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'groups', 'password')

    def create(self, validated_data):
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        group = Group.objects.get(name='visitor')
        user.groups.add(group)
        return user


class ClientSerializer(serializers.ModelSerializer):
    '''serializers client'''
    class Meta:
        model = Client
        fields = ['id', 'name', 'open']


class ProjectSerializer(serializers.ModelSerializer):
    '''serializers project'''
    class Meta:
        model = Project
        fields = ['id', 'name', 'open']


class SpiderSerializer(serializers.ModelSerializer):
    '''serializers spider'''
    project = ProjectSerializer(read_only=True)
    client = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Spider
        fields = '__all__'
