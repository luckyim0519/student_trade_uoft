from rest_framework import serializers
from .models import signupForm

class signupFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = signupForm
        fields =['username', 'email','password']

