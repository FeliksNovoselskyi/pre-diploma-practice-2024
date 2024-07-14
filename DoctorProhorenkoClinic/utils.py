from django.core.mail import send_mail
import DoctorProhorenkoClinic.settings as settings

def send_on_email(request):
    if 'enroll_button' in request.POST:
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        additionally_info = request.POST.get('additionally-info')

        if username and surname and email and phone:
            if additionally_info:
                send_mail(subject='enroll',
                        message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone} \nДодатковий коментар користувача: {additionally_info}',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER]
                )
                send_mail(subject='enroll',
                        message=f'Ви записались на прийом у клініці Доктора Прохоренко. \nВами було заповнено форму, ви ввели до неї: \nІм\'я: {username} \nПрізвище: {surname} \nПошту: {email} \nНомер телефону: {phone} \nДодатковий коментар: {additionally_info}',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email]
                )
            else:
                send_mail(subject='enroll',
                        message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone} \nДодатковий коментар: не був вказаний',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER]
                )
                send_mail(subject='enroll',
                        message=f'Ви записались на прийом у клініці Доктора Прохоренко. \nВами було заповнено форму, ви ввели до неї: \nІм\'я: {username} \nПрізвище: {surname} \nПошту: {email} \nНомер телефону: {phone} \nДодатковий коментар: не був вказаний',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email]
                )