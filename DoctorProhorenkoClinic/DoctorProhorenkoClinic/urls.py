"""
URL configuration for DoctorProhorenkoClinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from main.views import *
from services.views import *
from consultations.views import *
from contacts.views import *
from auth_reg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_page'),
    path('services/', services_view, name='services_page'),
    path('consultations/', consultations_view, name='consultations_page'),
    path('contacts/', contacts_view, name='contacts_page'),
    path('auth/', auth_view, name='auth_page'),
    path('reg/', reg_view, name='reg_page'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)