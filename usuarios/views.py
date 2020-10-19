from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        nome: str = request.POST['nome']
        email: str = request.POST['email']
        senha: str = request.POST['password']
        senha2: str = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if not email.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('usuário já cadastro')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        print('usuário cadastro com sucesso')

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def logout(request):
    """
    docstring
    """
    pass


def dashboard(request):
    """
    docstring
    """
    pass
