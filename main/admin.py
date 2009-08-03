from main.models import Project
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register ( Project )
