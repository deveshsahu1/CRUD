from atexit import register
from django.contrib import admin
from application.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
