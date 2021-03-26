from django.contrib import admin
from testapp.models import TicketSignup,Location,Theatre
# Register your models here.
class TicketSignupAdmin(admin.ModelAdmin):
    list_display=['username','password','email','first_name','last_name']

admin.site.register(TicketSignup,TicketSignupAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display=['location']

admin.site.register(Location,LocationAdmin)

class TheatreAdmin(admin.ModelAdmin):
    list_display=['theatre']

admin.site.register(Theatre,TheatreAdmin)
