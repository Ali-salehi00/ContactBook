from django.shortcuts import render, get_object_or_404
from .models import Contact


def home(request):
    contacts = Contact.objects.all()

    return render(request, 'core/home.html', {
        'contacts': contacts
    })


def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)

    return render(request, 'core/detail.html', {
        'contact': contact
    })