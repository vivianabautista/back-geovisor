import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class ResponseType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    response_type = models.ForeignKey(ResponseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    # ToDo. Validar que la choice solo se asigne si la question es de tipo choice


class Visitor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.JSONField()


class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    visit_date = models.DateTimeField('date visited')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return self.visit_date

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
      
class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    address = models.CharField(max_length=200)
    phon1e = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

