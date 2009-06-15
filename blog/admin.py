from plunatica.blog.models import Blog, Tag, Author
from django.contrib import admin


admin.site.register ( Tag )
admin.site.register ( Author )

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register ( Blog, BlogAdmin )
    
    
