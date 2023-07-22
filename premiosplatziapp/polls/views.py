from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all()
#     # return HttpResponse("Estás en la página principal de Premios Platzi App")
#     return render(
#         request,
#         "polls/index.html",
#         {"latest_question_list": latest_question_list}
#     )
#
#
# # FUNCTION BASED VIEW
# def detail(request, question_id):
#     # return HttpResponse(f"Estás viendo la pregunta número {question_id}")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
#
#
# def results(request, question_id):
#     # return HttpResponse(f"Estás viendo los resultados de pregunta número {question_id}")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[0:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # return HttpResponse(f"Estás votando a la pregunta número {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        # OBTENEMOS LA OPCIÓN SELECCIONADA, DEL CONJUNTO DE OPCIONES DE LA PREGUNTA
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        pass
    # SI NO SE HA SELECCIONADO NINGUNA OPCIÓN O EXISTE UN ERROR
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No has seleccionado una opción"
        })
    # EL ELSE ES PARA CUANDO NO HAYA ERRORES
    else:
        # AUMENTAMOS EN 1 EL VOTO DE LA OPCIÓN SELECCIONADA
        selected_choice.votes += 1
        selected_choice.save()
        # REDIRECCIONAMOS A LA PÁGINA DE RESULTADOS
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
        )
