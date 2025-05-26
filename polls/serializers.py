from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        depth = 1
        