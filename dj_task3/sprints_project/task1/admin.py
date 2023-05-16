from django.contrib import admin
from .models import Student


class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address",)


admin.site.register(Student, PostAdmin)# Register your models here.
