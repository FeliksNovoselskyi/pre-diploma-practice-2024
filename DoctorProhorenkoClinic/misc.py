from django.core.mail import send_mail
import DoctorProhorenkoClinic.settings as settings

def send_on_email(request):
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