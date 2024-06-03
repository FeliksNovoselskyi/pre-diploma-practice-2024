from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError

# Create your views here.
def auth_view(request):
    context = {} 
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
    
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
                else:
                    context['error'] = 'Пошта або пароль невірні'
            else:
                context['error'] = 'Заповніть усі поля'
    if 'leave_btn' in request.POST:
        logout(request)
        
    
    return render(request, 'auth_reg/auth.html', context)

def reg_view(request):
    context = {}
    
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
                except IntegrityError:
                    context['error'] = 'Такий користувач вже існує'
            else:
                context['error'] = 'Пароль занадто малий'
        else:
            context['error'] = 'Заповніть усі поля'
    
    return render(request, 'auth_reg/reg.html', context)