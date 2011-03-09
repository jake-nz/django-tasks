from tasks.models import *
from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'type', 'submitted_date', 'modified_date')
    list_display_editable = ('status', 'priority', )
    list_display_links = ('title', )
    list_filter = ('priority', 'status', 'submitted_date', 'type',)
    search_fields = ('title', 'description',)
    date_hierarchy = 'submitted_date'
    save_on_top = True
    save_as = True


admin.site.register(Priority)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Task, TaskAdmin)