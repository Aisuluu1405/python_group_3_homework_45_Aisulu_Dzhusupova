from django.contrib import admin
from webapp.models import Plan


class PlanAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'text', 'status', 'deadline']
    list_filter = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    exclude = []


admin.site.register(Plan, PlanAdmin)


