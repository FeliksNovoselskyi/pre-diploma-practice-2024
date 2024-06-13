from django.shortcuts import render
from .models import *

# Create your views here.
def main_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    main_page_logo = Icons.objects.get(id=8)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    main_page = BackgroundImages.objects.get(id=1)
    
    onkoderm = BackgroundImages.objects.get(id=10)
    kriodest = BackgroundImages.objects.get(id=11)
    mezoter = BackgroundImages.objects.get(id=12)
    prices_background = BackgroundImages.objects.get(id=14)
    
    location_slide = BackgroundImages.objects.get(id=5)
    fast_service_slide = BackgroundImages.objects.get(id=3)
    kids_consultation_slide = BackgroundImages.objects.get(id=4)

    about_doctor_bg = BackgroundImages.objects.get(id=15)
    consultations_bg = BackgroundImages.objects.get(id=2)
    
    context["logo"] = logo
    context["main_page_logo"] = main_page_logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context["main_page"] = main_page

    context["onkoderm"] = onkoderm
    context["kriodest"] = kriodest
    context["mezoter"] = mezoter
    context["prices_background"] = prices_background
    
    context["location_slide"] = location_slide
    context["fast_service_slide"] = fast_service_slide
    context["kids_consultation_slide"] = kids_consultation_slide

    context["about_doctor_bg"] = about_doctor_bg

    context["consultations_bg"] = consultations_bg
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
    
    return render(request, 'main/main.html', context)