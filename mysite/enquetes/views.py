from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Pergunta
from django.shortcuts import render, get_object_or_404

def index(request):
    ultimas_perguntas = Pergunta.objects.order_by('-data_publicacao')[:5]
    template = loader.get_template('enquetes/index.html')
    contexto = {'ultimas_perguntas': ultimas_perguntas}
    return render(request, 'enquetes/index.html',contexto,)

def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except:
        raise Http404('A Pergunta não existe!')
    return render(request, 'enquetes/detalhes.html',{'pergunta': pergunta})

def resultados(request,pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/resultados.html", {"pergunta": pergunta})

def votos(request,pergunta_id):
    try: 
       escolha_selecionada = pergunta.escolha_set.get(pk=request.Post["escolha"])
    except render(keyError, Escolha.DoesNotExist):

        return render(
            request,
            "enquetes/detalhes.html",
            {
                "question": pergunta, 
                "error_message": "você não selecionou uma escolha.",
            },
        )
    else:
        escolha_selecionada.votos = f("votos") + 1
        escolha_selecionada.save()


        return HttpResponseRedirect(reverse("enquentes:resultados", *args=(pergunta.id,)))



    
    )
