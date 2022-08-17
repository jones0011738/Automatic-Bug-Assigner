from django.contrib import admin
from .models import Request, Result

# Register your models here.
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['request_owner','title']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['request']


