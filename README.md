# Doctor Prohorenko Clinic

Цей проект є сайтом для доктора Прохоренко. На цьому сайті ви можете ознайомитись з інформацією про доктора та клініку, та як з нею зв'язатись. Ви можете продивитись наявні послуги й консультації, та їх ціни. Сайт має зручний дизайн та функціонал, тому ви маєте змогу швидко отримати потрібну вам інформацію, та записатись на прийом.

## Учасники команди
- [Новосельський Фелікс/Novoselskyi Feliks](https://github.com/FeliksNovoselskyi) - лідер команди
- [Гераймович Семен/Heraimovych Semen](https://github.com/arman455) - дизайнер проекту, та його розробник
- [Людмила Махиня/Makhynia Liudmyla](https://github.com/LiudmylaMakhynia) - дизайнер проекту, та його розробник
- [Михненко Данило/Mykhnenko Danylo](https://github.com/danil-michnenko) - дизайнер проекту, та його розробник

## Опис сторінок проекту
- **Головна сторінка** - можливість швидко переглянути наявні пропозиції клініки.
- **Сторінки послуг та консультацій** - сторінки, на яких ви зможете зручно переглянути наявні послуги та консультації, з наявними до них цінами. А також записатись на прийом.
- **Сторінка сертифікатів** - на цій сторінці ви можете продивитись сертифікати лікаря.
- **Сторінка контактів** - на цій сторінці ви можете переглянути основну інформацію клініки, де вона знаходиться, її соцмережі, номер телефону, та пошту для зв'язку.
- **Сторінка авторизації та реєстрації** - на цих сторінках ви можете створити свій акаунт на сайті, та увійти в нього.

## Використані технології
- **Python/Django** - мова програмування та основний веб-фреймворк, які забезпечують роботу сайту.
- **Bootstrap** - фронтенд-фреймворк, допомагає у створенні фронтенд частини сайту.
- **HTML та CSS** - використовуються для створення основної фронтенд частини сайту.
- **JavaScript** - робить контент сайту динамічним, та покращує використання сайту користувачем.
- **SQLite3** - база даних, яка була використана для розробки сайту.
- **MySQL** - база даних, яка використовується для забезпечення роботи сайту.
- **Figma** - онлайн-сервіс, використаний для планування дизайну сайту.
- **FigJam** - онлайн-сервіс, який був використаний для планування функціоналу сайту.

## Посилання на Figma та FigJam
- [Figma проект](https://www.figma.com/design/Cmxt8OjIxcQVkusZVgJpJS/Untitled?node-id=0-1&t=IXh6wswWVGBAbsu6-1)
- [FigJam](https://www.figma.com/board/Y5U9mctjukxSB2A5laDTnH/pre-diploma-practice-2024-FIGJAM?t=iRElZM5fwQltrSYK-1)

## Функціонал проекту

### Файл DoctorProhorenkoClinic/main/backends/email_backend.py

```python
# Імпортує модуль ssl, який надає доступ до основних функцій і констант, необхідних для створення захищених з'єднань SSL/TLS
import ssl

from django.core.mail.backends.smtp import EmailBackend as SMTPBackend  # Імпортує клас EmailBackend з модуля django.core.mail.backends.smtp і перейменовує його на SMTPBackend для зручності
from django.utils.functional import cached_property  # Імпортує декоратор cached_property з модуля django.utils.functional

# Визначає новий клас EmailBackend, який успадковує всі властивості та методи від SMTPBackend
class EmailBackend(SMTPBackend):
    # Цей декоратор надає можливість кешувати результат обчислення властивості, щоб його обчислювали тільки один раз і потім використовували повторно
    @cached_property
    def ssl_context(self):
        # Перевіряє, чи визначено атрибути ssl_certfile або ssl_keyfile. Ці атрибути вказують на файли сертифіката та ключа для SSL
        if self.ssl_certfile or self.ssl_keyfile:
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)  # Якщо вказані файли сертифіката або ключа, створюється новий SSL-контекст з використанням протоколу PROTOCOL_TLS_CLIENT
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)  # Завантажує сертифікат і ключ в SSL-контекст, використовуючи зазначені файли
            return ssl_context
        else:
            ssl_context = ssl.create_default_context() # Використання стандартного SSL контексту, якщо сертифікат і ключ не задані
            ssl_context.check_hostname = False  # Відключення перевірки імені хоста
            ssl_context.verify_mode = ssl.CERT_NONE  # Відключення перевірки сертифікату
            return ssl_context
```

Таким чином, цей клас розширює стандартний EmailBackend, додаючи підтримку користувацького SSL-контексту для шифрування з'єднань під час надсилання електронної пошти через SMTP.

### Файл DoctorProhorenkoClinic/misc.py

```python
from django.core.mail import send_mail # Імпортуємо функцію send_mail, яку використовуємо для відправки запису на пошту
import DoctorProhorenkoClinic.settings as settings # Імпортуємо налаштування з файлу проекту settings

# Створюємо функцію, яка відправляє запис на пошту
def send_on_email(request):
    # Перевіряємо, чи є метод запиту POST (тобто форма була відправлена)
    if request.method == "POST":
        # Отримуємо з форми для запису введену користувачем інформацію
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')

        # Перевіряємо, чи була заповнена форма
        if username and surname and phone:
            # Відправляємо запис на пошту використовуючи функцію send_mail
            send_mail(subject='enroll', # Вказуємо тему листу
                    message=f'{username} {surname} має потребу у ваших послугах. Його/Її номер телефону: {phone}', # Формуємо текст повідомлення
                    from_email=settings.EMAIL_HOST_USER, # Вказуємо адресу відправника листа, беручи її з файлу settings
                    recipient_list=['doctorprohorenkoclinic@gmail.com', settings.EMAIL_HOST_USER] # Вказуємо отримувача листа з записом
            )
```

Отже цей файл забезпечує відправлення записів на пошту, створюючи функцію, яку можна використати у будь-якому файлі проекту.

### Файл DoctorProhorenkoClinic/auth_reg/views.py

#### Функція auth_view:
```python
def auth_view(request):
    context = {}
    
    # Вимкнути відображення нижнього колонтитула та форми входу
    context['show_footer'] = False
    context['show_sign_in'] = False
    
    # Якщо користувач автентифікований
    if request.user.is_authenticated:
        # Додати ім'я користувача до контексту
        context['username'] = request.user.username
        # Вказати, що користувач увійшов у систему
        context['signed_in'] = True
        # Відобразити кнопку виходу
        context['leave_btn'] = True
    
    # Якщо натиснута кнопка реєстрації
    if 'join_btn' in request.POST:
        # Якщо користувач вже автентифікований
        if request.user.is_authenticated:
            # Додати повідомлення про помилку до контексту
            context['error'] = 'Ви вже зареєстровані'
        else:
            # Отримати ім'я користувача та пароль з POST-запиту
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # Додати введені дані до контексту
            context["username_input"] = username
            context["password_input"] = password
            
            # Якщо ім'я користувача та пароль заповнені
            if username and password:
                # Спробувати автентифікувати користувача
                user = authenticate(username=username, password=password)
                if user:
                    # Увійти у систему як автентифікований користувач
                    login(request, user)
                    # Перенаправити на головну сторінку
                    return redirect('main_page')
                else:
                    # Додати повідомлення про помилку до контексту
                    context['error'] = "Ім'я або пароль невірні"
            else:
                # Додати повідомлення про помилку до контексту, якщо поля порожні
                context['error'] = 'Заповніть усі поля'
    
    # Якщо натиснута кнопка виходу
    if 'leave_btn' in request.POST:
        # Вийти з системи
        logout(request)
        # Перенаправити на сторінку авторизації
        return redirect('auth_page')
    
    # Відобразити шаблон авторизації з контекстом
    return render(request, 'auth_reg/auth.html', context)
```
Ця функція відповідальна за авторизацію користувача, вхід в його акаунт

#### Функція reg_view:
```python
def reg_view(request):
    # Ініціалізуємо контекст для передачі даних у шаблон
    context = {}
    
    # Вимкнути відображення нижнього колонтитула та увімкнути відображення форми входу
    context['show_footer'] = False
    context['show_sign_in'] = True
    
    # Якщо користувач автентифікований
    if request.user.is_authenticated:
        # Додаємо ім'я користувача до контексту
        context['username'] = request.user.username
        # Вказуємо, що користувач увійшов у систему
        context['signed_in'] = True
    
    # Якщо метод запиту POST (тобто форма була відправлена)
    if request.method == 'POST':
        # Отримуємо дані з POST-запиту
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Додаємо введені дані до контексту
        context["username_input"] = username
        context["surname_input"] = surname
        context["phone_input"] = phone
        context["email_input"] = email
        context["password_input"] = password
        
        # Перевіряємо, що всі поля заповнені
        if username and surname and phone and email and password:
            # Перевіряємо, що довжина пароля не менше 8 символів
            if len(password) >= 8:
                try:
                    # Створюємо нового користувача
                    User.objects.create_user(
                        username=username,
                        last_name=surname,
                        # phone=phone, # Цей рядок закоментований, оскільки поле phone, можливо, не визначене в моделі User
                        email=email,
                        password=password,
                    )
                    # Перенаправляємо на сторінку авторизації
                    return redirect('auth_page')
                except IntegrityError:
                    # Якщо користувач з таким ім'ям вже існує, додаємо повідомлення про помилку до контексту
                    context['error'] = 'Такий користувач вже існує'
            else:
                # Якщо пароль занадто короткий, додаємо повідомлення про помилку до контексту
                context['error'] = 'Пароль занадто малий'
        else:
            # Якщо не всі поля заповнені, додаємо повідомлення про помилку до контексту
            context['error'] = 'Заповніть усі поля'
    
    # Відображаємо шаблон реєстрації з контекстом
    return render(request, 'auth_reg/reg.html', context)
```
Ця функція відповідальна за реєстрацію користувача, створення його акаунту
