from django.shortcuts import render
from main.models import *

# Create your views here.
def contacts_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)

    contacts_map = BackgroundImages.objects.get(id=16)
    
    contacts_location = Icons.objects.get(id=9)
    contacts_instagram = Icons.objects.get(id=10)
    contacts_email = Icons.objects.get(id=11)
    contacts_phone = Icons.objects.get(id=12)
    
    contacts_bg_image = BackgroundImages.objects.get(id=14)
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone

    burger_menu = Icons.objects.get(id=13)
    
    context["contacts_map"] = contacts_map
    
    context["contacts_location"] = contacts_location
    context["contacts_instagram"] = contacts_instagram
    context["contacts_email"] = contacts_email
    context["contacts_phone"] = contacts_phone
    context["burger_menu"] = burger_menu

    context["contacts_bg_image"] = contacts_bg_image
    
    context['show_footer'] = False
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
    
    return render(request, 'contacts/contacts.html', context)