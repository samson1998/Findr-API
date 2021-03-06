from rest_framework import serializers
from .models import User,Apartment, Image
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    phone_number = serializers.CharField(min_length=11, required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],phone_number=validated_data['phone_number'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number')

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
