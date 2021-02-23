from django.db import transaction
from rest_framework import serializers
from accounts.models import Profile, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ """

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'id': {'read_only': True}, 'password': {'write_only': True}}

    def create(self, validated_data):
        """ Get validated data and create user or profile. """
        with transaction.atomic():
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            profile = Profile(user=user)
            profile.save()

        return user

