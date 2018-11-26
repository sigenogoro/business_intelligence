from django.contrib import admin
from .models import Friend
from .models import Message
#name => sample
#passworld
# Register your models here.
admin.site.register(Friend)
admin.site.register(Message)