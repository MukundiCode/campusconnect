from django.contrib import admin
from meet.models import Profile,MeetUp,Meet_User,Event,Requests
# Register your models here.

admin.site.register(Profile)
admin.site.register(MeetUp)
admin.site.register(Meet_User)
admin.site.register(Event)
admin.site.register(Requests)

