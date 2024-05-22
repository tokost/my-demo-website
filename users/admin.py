from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin    # pridane III
from .models import CustomUser                      # pridane III

# Register your models here. Pridal som do Django aministration zlozku USERS
# Muselo sa to riesit takto lebo bolo v settings.py nastavene 
# Custom user mode AUTH_USER_MODEL = "users.CustomUser"

class UserAdmin(BaseUserAdmin):                     # pridane III
    model = CustomUser

admin.site.register(CustomUser, UserAdmin)          # pridane III
