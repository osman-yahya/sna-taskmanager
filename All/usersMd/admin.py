from django.contrib import admin
from .models import User, Companies, Work

# User Model için Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'isManager')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('isManager',)

# Companies Model için Admin
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Work Model için Admin
class WorkAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'work_hour', 'date','about')
    list_filter = ('user', 'company', 'date')
    search_fields = ('user__username', 'company__name')


admin.site.register(User, UserAdmin)
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Work, WorkAdmin)
