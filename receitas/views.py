from django.shortcuts import render


def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de Legumes',
        3: 'Sorvete de chocolate',
        4: 'Panqueca',
        5: 'Ovo frito'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)


def receita(request):
    return render(request, 'receita.html')
