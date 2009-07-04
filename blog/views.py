
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list_detail import object_detail
from blog.models import BlogEntry

@staff_member_required
def preview(request, object_id):
    return object_detail(request, object_id=object_id, queryset=BlogEntry.objects.all(), template_object_name = 'blog', )