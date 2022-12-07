from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'phone', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'city', 'phone', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'city', 'phone', 'avatar', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email', )


admin.site.register(User, CustomUserAdmin)
