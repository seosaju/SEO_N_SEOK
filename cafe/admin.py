from django.contrib import admin
from .models import Menu, Inquiry, Event


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['korean_name', 'category']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Event)
admin.site.register(Inquiry)
