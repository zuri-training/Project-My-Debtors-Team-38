from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SchoolProfile, GuardianProfile, GuardianChild, Student

# how to handle User model on admin page


class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'date_joined',
                    'last_login', 'is_admin', 'is_staff',)
    search_fields = ('email', 'role', 'name')
    readonly_fields = ('id', 'date_joined', 'last_login')

    ordering = ("email",)
    filter_horizontally = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)
admin.site.register(SchoolProfile)
admin.site.register(Student)
admin.site.register(GuardianProfile)
admin.site.register(GuardianChild)
