from django.contrib import admin
from myblog.models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

# register the model (especially important)

admin.site.register(BlogPost,BlogPostAdmin)