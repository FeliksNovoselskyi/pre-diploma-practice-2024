from django.shortcuts import render
import misc

# Create your views here.
def main_view(request):
    context = {}
    
    context['show_footer'] = True
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
        
    misc.send_on_email(request)
    
    return render(request, 'main/main.html', context)