from django.shortcuts import render
from .models import About, Mission, Service, Team, Message, Messages, Backgroundimg, Logo, First_advert, Second_advert
# Create your views here.
def index(request):
    about = About.objects.first()
    mission = Mission.objects.first()
    service = Service.objects.all()
    team = Team.objects.all()
    message = Message.objects.all()
    messages = Messages.objects.all()
    backgroundimg = Backgroundimg.objects.first()
    logo = Logo.objects.first()
    first_advert = First_advert.objects.all()
    second_advert = Second_advert.objects.all()
    content = {
        'about': about,
        'mission': mission,
        'service': service,
        'team': team,
        'message': message,
        'messages': messages,
        'backgroundimg': backgroundimg,
        'logo': logo,
        'first_advert': first_advert,
        'second_advert': second_advert,
    }
    return render (request,'index.html', {'content':content})