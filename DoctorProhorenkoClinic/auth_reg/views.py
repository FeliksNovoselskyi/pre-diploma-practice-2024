from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from main.models import *

# Create your views here.
def auth_view(request):
    context = {}
    
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context['show_footer'] = False
    context['show_sign_in'] = False
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
        context['leave_btn'] = True
    
    if 'join_btn' in request.POST:
        if request.user.is_authenticated:
            context['error'] = 'Ви вже зареєстровані'
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('main_page')
                else:
                    context['error'] = 'Пошта або пароль невірні'
            else:
                context['error'] = 'Заповніть усі поля'
    if 'leave_btn' in request.POST:
        logout(request)
        return redirect('auth_page')
    
    return render(request, 'auth_reg/auth.html', context)

def reg_view(request):
    context = {}
    
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context['show_footer'] = False
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
    
    if request.method == 'POST':
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if username and surname and phone and email and password:
            if len(password) >= 8:
                try:
                    User.objects.create_user(
                        username=username,
                        last_name=surname,
                        # phone=phone,
                        email=email,
                        password=password,
                    )
                    return redirect('auth_page')
                except IntegrityError:
                    context['error'] = 'Такий користувач вже існує'
            else:
                context['error'] = 'Пароль занадто малий'
        else:
            context['error'] = 'Заповніть усі поля'
    
    return render(request, 'auth_reg/reg.html', context)