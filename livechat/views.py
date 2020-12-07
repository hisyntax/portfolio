from django.shortcuts import render
from .models import Link, Phone
from homepage.models import Logo
# Create your views here.
def index(request):
    link = Link.objects.first()
    logo = Logo.objects.first()
    phone = Phone.objects.first()
    content = {
        'link': link,
        'logo': logo,
        'phone': phone
    }
    return render (request, 'live-chat.html', {'content': content})