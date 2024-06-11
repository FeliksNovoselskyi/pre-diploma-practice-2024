from django.shortcuts import render
from .models import *

# Create your views here.
def main_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    service_arrow_footer = Icons.objects.get(id=7)
    
    location = Icons.objects.get(id=3)
    email = Icons.objects.get(id=4)
    instagram = Icons.objects.get(id=5)
    phone = Icons.objects.get(id=6)
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    context["service_arrow_footer"] = service_arrow_footer
    
    context["location"] = location
    context["email"] = email
    context["instagram"] = instagram
    context["phone"] = phone
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
    
    return render(request, 'main/main.html', context)