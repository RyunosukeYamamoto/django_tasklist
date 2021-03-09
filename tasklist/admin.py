from django.contrib import admin
from tasklist.models import Task, User


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    raw_id_fields = ('user', )


admin.site.register(Task, TaskAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


admin.site.register(User, UserAdmin)


