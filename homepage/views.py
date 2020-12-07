from django.shortcuts import render
from .models import About, Mission, Service, Team, Message, Messages, Backgroundimg, Logo
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
    content = {
        'about': about,
        'mission': mission,
        'service': service,
        'team': team,
        'message': message,
        'messages': messages,
        'backgroundimg': backgroundimg,
        'logo': logo
    }
    return render (request,'index.html', {'content':content})