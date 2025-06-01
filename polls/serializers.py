from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Form, Section, Question, TypeChoice

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        depth = 1
        
    
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'options': {'required': False},
            'typeChoice': {'required': False, 'allow_null': True}

        }

class TypeChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeChoice
        fields = '__all__'
        depth = 1