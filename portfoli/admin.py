from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'live_url', 'github_url')
    list_filter = ('technologies',)
    search_fields = ('title', 'description')


# admin.site.register(Project)
