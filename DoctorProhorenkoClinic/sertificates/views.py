from django.shortcuts import render
from main.models import *

# Create your views here.
def sertificates_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    sertificates_page_image = BackgroundImages.objects.get(id=17)

    sertificates_bg_image = BackgroundImages.objects.get(id=18)
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone

    context["sertificates_page_image"] = sertificates_page_image

    context["sertificates_bg_image"] = sertificates_bg_image
    
    burger_menu = Icons.objects.get(id=13)
    context["burger_menu"] = burger_menu
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    return render(request, 'sertificates/sertificates.html', context)