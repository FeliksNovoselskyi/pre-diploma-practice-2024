from django.shortcuts import render
import misc

# Create your views here.
def contacts_view(request):
    context = {}
    
    context['show_footer'] = False
    context['show_sign_in'] = True
    
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['signed_in'] = True
        
    misc.send_on_email(request)
    
    return render(request, 'contacts/contacts.html', context)