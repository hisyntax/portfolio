from django.contrib import admin
from .models import Author, About, Service, Message, Mission , Team, Messages, Backgroundimg, Logo
# Register your models here.
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Message)
admin.site.register(Messages)
admin.site.register(Mission)
admin.site.register(Team)
admin.site.register(Backgroundimg)
admin.site.register(Logo)