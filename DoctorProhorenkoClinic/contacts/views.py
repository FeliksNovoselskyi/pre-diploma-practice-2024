from django.shortcuts import render

# Create your views here.
def contacts_view(request):
    return render(request, 'contacts/contacts.html')