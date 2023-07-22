from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeform, CustomUserCreationForm
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeform
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
