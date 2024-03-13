from django.shortcuts import render, redirect
from django.views import View
from .models import *

from django.contrib.auth import authenticate, login, logout

# Create your views here.

class LoginView(View):
    
    def get(self, request):

        return render(request, 'login.html')
    
    def post(self, request):
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('index')
        
        else:

            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
        
class LogoutView(View):

    def get(self, request):
        
        logout(request)

        return redirect('login')

class IndexView(View):

    def get(self, request):

        imoveis = {
            'imoveis':Imovel.objects.all()
        }

        return render(request, 'index.html', imoveis)
    
    def post(self, request):

        pass