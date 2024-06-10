from django.shortcuts import render
from .models import *

# Create your views here.
def main_view(request):
    context = {}
    logo = Icons.objects.get(id=1)
    service_arrow = Icons.objects.get(id=2)
    
    context["logo"] = logo
    context["service_arrow"] = service_arrow
    
    return render(request, 'main/main.html', context)