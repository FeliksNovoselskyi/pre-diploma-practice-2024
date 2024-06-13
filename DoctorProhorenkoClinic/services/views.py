from django.shortcuts import render
from main.models import *
from .models import *

# Create your views here.
def service_first_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    onkoderm_page_image = BackgroundImages.objects.get(id=7)
    service_bg_image = BackgroundImages.objects.get(id=19)
    
    all_service1 = Service1.objects.all()
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context["onkoderm_page_image"] = onkoderm_page_image
    context["service_bg_image"] = service_bg_image
    
    context["all_service1"] = all_service1
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True

    return render(request, 'services/service_first.html', context)

def service_second_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    kriodestruction_page_image = BackgroundImages.objects.get(id=8)
    service_bg_image = BackgroundImages.objects.get(id=19)
    
    all_service2 = Service2.objects.all()
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context["kriodestruction_page_image"] = kriodestruction_page_image
    context["service_bg_image"] = service_bg_image
    
    context["all_service2"] = all_service2
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True

    return render(request, 'services/service_second.html', context)

def service_third_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    mezoterapia_page_image = BackgroundImages.objects.get(id=6)
    service_bg_image = BackgroundImages.objects.get(id=19)
    
    all_service3 = Service3.objects.all()
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context["mezoterapia_page_image"] = mezoterapia_page_image
    context["service_bg_image"] = service_bg_image
    
    context["all_service3"] = all_service3
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True

    return render(request, 'services/service_third.html', context)

def service_consultations_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    consultations_page_image = BackgroundImages.objects.get(id=9)
    consultations_bg_image = BackgroundImages.objects.get(id=14)
    
    all_consultations = Consultations.objects.all()
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context["consultations_page_image"] = consultations_page_image
    context["consultations_bg_image"] = consultations_bg_image
    
    context["all_consultations"] = all_consultations
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True

    return render(request, 'services/service_consultations.html', context)