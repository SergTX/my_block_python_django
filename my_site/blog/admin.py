from django.contrib import admin

from .models import Author, Post, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):                    # modifying Admin menu adding filters , slug-auto
    list_filter = ("author", "tags", "date")          # adding filters by name in the tuple - will be available on ui side
    list_display = ("title", "date", "author")        # display title , date , author columns
    prepopulated_fields = {"slug": ("title",)}        # adding in dic what fields to populate and from what to take it


admin.site.register(Post, PostAdmin)      # passing admin class as a second parameter
admin.site.register(Author)
admin.site.register(Tag)
