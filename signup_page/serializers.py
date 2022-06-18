from rest_framework import serializers
from .models import signupModel

class signupFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = signupModel
        fields =['username', 'email','password']

