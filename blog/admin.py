from blog.models import BlogEntry, Tag, Author
from django.contrib import admin


admin.site.register ( Tag )
admin.site.register ( Author )

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register ( BlogEntry, BlogAdmin )
    
