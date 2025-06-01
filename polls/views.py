from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form, Section, Question, TypeChoice
from .serializers import *

class FormView(APIView):
    def get(self, request, search=None):
        if search:
            forms = Form.objects.filter(name__icontains=search)
        else:
            forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, search=None):
        data = request.data
        # Suponiendo que 'name' es el campo único para identificar el formulario
        form, created = Form.objects.update_or_create(
            name=data.get('name'),
            defaults=data
        )
        serializer = FormSerializer(form)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code)


class SectionView(APIView):
    def get(self, request, search=None):
        if search:
            sections = Section.objects.filter(name__icontains=search)
        else:
            sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, search=None):
        data = request.data
        # Suponiendo que 'name' es el campo único para identificar la sección
        section, created = Section.objects.update_or_create(
            name=data.get('name'),
            defaults=data
        )
        serializer = SectionSerializer(section)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code)

class QuestionView(APIView):
    def get(self, request, search=None):
        if search:
            questions = Question.objects.filter(question__icontains=search)
        else:
            questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, search=None):
        data = request.data
        
        # Obtener el typeChoice del request
        type_choice_id = data.get('typeChoice')
        
        # Buscar el TypeChoice según el ID (número) o nombre (string)
        type_choice = None
        if type_choice_id:
            try:
                # Intentar buscar por ID (número)
                type_choice = TypeChoice.objects.get(id=type_choice_id)
            except (ValueError, TypeChoice.DoesNotExist):
                return Response(
                    {'error': 'TypeChoice no encontrado'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        
        # Crear o actualizar la pregunta
        question, created = Question.objects.update_or_create(
            question=data.get('question'),
            defaults={
                'question': data.get('question'),
                'options': data.get('options', ''),
                'typeChoice': type_choice
            }
        )
        
        serializer = QuestionSerializer(question)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code)
    

class QuestionTypeView(APIView):
    def get(self, request):
        question_types = TypeChoice.objects.all()
        serializer = TypeChoiceSerializer(question_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    