from .models import Work,User,Companies
from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Şifreyi sadece yazılabilir yap

    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name', 'password','isManager']

    def create(self, validated_data):
        # Kullanıcıyı oluştur ve şifreyi hash'le
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user
    
    
class WorkSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Companies.objects.all())


    class Meta:
        model = Work
        fields = [
            "id",
            "user",
            "company",
            "work_hour",
            "date",
            "about",
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'company': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['user']
        work = Work.objects.create(user=user, **validated_data)
        return work