import datetime
from django.db import models
from django.contrib import admin

from django.utils import timezone


# Create your models here.
# LA CLASE VA EN SINGULAR
class Question(models.Model):
    # ATRIBUTOS DE LA CLASE
    # El id por automático Django lo crea
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # MÉTODOS DE LA CLASE
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # SI SE ELIMINA UNA PREGUNTA, SE ELIMINAN TODAS LAS OPCIONES
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # MÉTODOS DE LA CLASE
    def __str__(self):
        return self.choice_text
