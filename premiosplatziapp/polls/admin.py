from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)

# IMPORTAR TODOS
admin.site.register([Question, Choice])