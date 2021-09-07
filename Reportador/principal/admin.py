from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UrbUser

# Register your models here.
class UrbUserAdmin(BaseUserAdmin):
    list_display=('uid','email','username','last_login','firstname','lastname','is_active','is_admin')
    search_fields=('email','username','firstname','lastname','country','state')
    readonly_fields=('last_login',)
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('email','username','firstname','lastname','phone','password1','password2'),
        }),
    )

    ordering=('uid',)

admin.site.register(UrbUser, UrbUserAdmin)
