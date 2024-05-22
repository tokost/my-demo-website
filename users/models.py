from django.db import models
from django.contrib.auth.models import AbstractUser # pridane

# from django.contrib import admin                    # pridane III
# from django.contrib.auth.admin import UserAdmin     # pridane III
# from .models import User                            # pridane III

# Create your models here.

"""
modely aplikacie users

model CustomUser - uzivatelia
"""
class CustomUser(AbstractUser): # pridane
    pass


# admin.site.register(User, UserAdmin)                # pridane III
