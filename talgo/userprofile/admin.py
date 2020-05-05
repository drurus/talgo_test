from django.contrib import admin
from .models import Activity, User, Shop


admin.site.register(Activity)
admin.site.register(Shop)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'name', 'lastname', 'display_activity', 'email', )
    fields = ['login', ('name', 'lastname'), ('age', 'activity'), ('email', 'social')]
