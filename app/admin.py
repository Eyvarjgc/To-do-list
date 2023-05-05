from django.contrib import admin
from .models import days,task,Messages
# Register your models here.

admin.site.register(days)
admin.site.register(task)
admin.site.register(Messages)