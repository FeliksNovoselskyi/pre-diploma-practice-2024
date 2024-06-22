from django.shortcuts import render
import misc

# Create your views here.
def sertificates_view(request):
    context = {}
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    misc.send_on_email(request)
    
    return render(request, 'sertificates/sertificates.html', context)