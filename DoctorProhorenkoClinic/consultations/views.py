from django.shortcuts import render

# Create your views here.
def consultations_view(request):
    return render(request, 'consultations/consultations.html')