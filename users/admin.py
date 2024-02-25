from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserProfile, User


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


admin.site.register(User, BaseUserAdmin)
admin.site.register(UserProfile)
