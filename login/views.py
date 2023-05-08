from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import asyncio
from django.contrib.auth.hashers import make_password
from .models import Users


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # Obter o corpo da solicitação POST
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Criar um novo usuário
        message = create_user(body)

        # Retornar uma resposta de sucesso
        return JsonResponse({'message': message}, status=200)

    # Retornar uma mensagem de erro para outras solicitações HTTP
    return JsonResponse({'error': 'Método HTTP não permitido'}, status=405)

def create_user(data):
    full_name = data.get('Customer', {}).get('full_name', '')
    name_parts = full_name.split(' ')
    first_name = name_parts[0] if name_parts else ''
    last_name = name_parts[-1] if name_parts else ''

    email = data.get('Customer', {}).get('email', '')
    username = email.split('@')[0] if email else ''
    password = username

    new_user = Users(
        name=first_name,
        lastname=last_name,
        username=username,
        email=email,
        password=make_password(password)
    )

    new_user.save()

    return 'Criado com sucesso!'


from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        q_email = Users.objects.filter(email=email)
  
        if q_email.exists():
            user = q_email.first()
            print(user.password)
            user = authenticate(request, email=email, password=password)
            print(user)
            if user != None:
                login(request, user)
                return redirect(reverse('homepage'))
            else:
                messages.error(request, 'Senha incorreta!')
        else:
            messages.error(request, 'Email não cadastrado!')
        return render(request, 'login.html')
    return render(request, 'login.html')

def g_hack(request):
    return render(request, '/home/home.html')








def singup():
 
    new_user = Users()
    new_user.name = 'admin'
    new_user.lastname = 'admin'
    new_user.username = 'admin'
    new_user.email = 'admin@admin.com'
    new_user.password =make_password('admin')

    new_user.save()
    return 'Criado com sucesso!'

from django.views.decorators.cache import cache_page
from django.http import HttpResponse
import os

from django.conf import settings


@cache_page(60 * 15) # cache por 15 minutos
def nostar(request):
    with open('static/mines/img/no-star.png', "rb") as f:
        image_data = f.read()
    response = HttpResponse(image_data, content_type="image/png")
    return response
    
@cache_page(60 * 15) # cache por 15 minutos
def star(request):
    with open('static/mines/img/star.png', "rb") as f:
        image_data = f.read()
    response = HttpResponse(image_data, content_type="image/png")
    return response


def notfound(request, undefined_path):
    return render(request, '404.html', status=404)