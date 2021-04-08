from django.contrib import admin

from .models import *

admin.site.register(Questions)


@admin.register(Responses)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ["name","question","response"]
    list_filter = ["name","response"]