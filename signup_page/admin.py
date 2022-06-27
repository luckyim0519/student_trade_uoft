from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('email', 'username', 'password')

admin.site.register(User,UserAdmin)