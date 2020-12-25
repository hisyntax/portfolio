from django.shortcuts import render
from .models import Image
from homepage.models import Logo
# Create your views here.
def index(request):
    image = Image.objects.all()
    logo = Logo.objects.first()
    content = {
        'image': image,
        'logo': logo
    }
    return render (request, 'archive-website.html', {'content': content})