from django.contrib import admin
from .models import blogPost


@admin.register(blogPost)
class blogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_modified', )
    # ordering = ('-id', )


# admin.site.register(blogPost, blogPostAdmin)
