from receitas.models import Receita
from django.shortcuts import get_list_or_404, get_object_or_404, render


def busca(request):
    """Busca receita especifica"""
    lista_receitas = Receita.objects.order_by(
        '-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(
            nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', dados)
