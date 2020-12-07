from django.shortcuts import render
from .models import Info, Facebook, Instagram
from homepage.models import Logo
# Create your views here.
def index(request):
    info = Info.objects.first()
    facebook = Facebook.objects.first()
    instagram = Instagram.objects.first()
    logo = Logo.objects.first()
    content = {
        'info': info,
        'facebook': facebook,
        'instagram': instagram,
        'logo':logo
    }
    return render (request, 'follow-us.html', {'content': content})