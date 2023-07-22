from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)

#  ESTO PARA AGREGAR DIRECTAMENTE LAS RESPUESTAS EN LA PREGUNTA
class ChoiceInline(admin.TabularInline):
    # QUE MODELO
    model = Choice

    # CUANTAS RESPUESTAS
    extra = 3


# EDITAR EL MODELO EN EL ADMIN
class QuestionAdmin(admin.ModelAdmin):
    # DEFINIMOS ORDEN DE LOS CAMPOS
    fields = ["pub_date", "question_text"]

    # AGREGAMOS EL MODELO PARA LAS RESPUESTAS
    inlines = [ChoiceInline]

    # AGREGAMOS LOS CAMPOS QUE QUEREMOS VER EN LA LISTA DE PREGUNTAS
    list_display = ("question_text", "pub_date", "was_published_recently")

    # AGREGAMOS UN FILTRO PARA LAS PREGUNTAS
    list_filter = ["pub_date"]

    # AGREGAMOS UN BUSCADOR PARA LAS PREGUNTAS (CUADRO DE BÚSQUEDA)
    search_fields = ["question_text"]

# IMPORTAR TODOS
# admin.site.register([Question, Choice])

# IMPORTAR EL MODELO CON LA PERSONALIZACIÓN
admin.site.register(Question, QuestionAdmin)