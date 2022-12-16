from django.contrib import admin
from .models import Subscribers


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ("email",)
    search_fields = ("email",)


admin.site.register(Subscribers, SubscribersAdmin)
