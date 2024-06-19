from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
import DoctorProhorenkoClinic.settings as settings

# Create your views here.
def service_first_view(request):
    context = {}
    
    all_service1 = Service1.objects.all()
    
    context["all_service1"] = all_service1
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True

    if request.method == "POST":
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        
        if username and surname and phone:
            send_mail(subject='enroll',
                    message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER]
            )

    return render(request, 'services/service_first.html', context)

def service_second_view(request):
    context = {}
    
    all_service2 = Service2.objects.all()
    
    context["all_service2"] = all_service2
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
        
    if request.method == "POST":
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        
        if username and surname and phone:
            send_mail(subject='enroll',
                    message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER]
            )

    return render(request, 'services/service_second.html', context)

def service_third_view(request):
    context = {}
    
    all_service3 = Service3.objects.all()
    
    context["all_service3"] = all_service3
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
        
    if request.method == "POST":
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        
        if username and surname and phone:
            send_mail(subject='enroll',
                    message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER]
            )

    return render(request, 'services/service_third.html', context)

def service_consultations_view(request):
    context = {}
    
    all_consultations = Consultations.objects.all()
    
    context["all_consultations"] = all_consultations
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
        
    if request.method == "POST":
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        
        if username and surname and phone:
            send_mail(subject='enroll',
                    message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER]
            )

    return render(request, 'services/service_consultations.html', context)