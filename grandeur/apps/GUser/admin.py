from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import GUser

@admin.register(GUser)
class GUserAdmin(UserAdmin):
    list_display = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('reputation_score',)}),
    )
