from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
import DoctorProhorenkoClinic.settings as settings

# Create your views here.
def main_view(request):
    context = {}
    
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
    
    return render(request, 'main/main.html', context)