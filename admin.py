from django.contrib import admin

import models

# Register your models here.
class Profile(admin.ModelAdmin):
    """user infomation admin
    """
    list_display = ('user', 'private_token')

admin.site.register(models.Profile, Profile)
