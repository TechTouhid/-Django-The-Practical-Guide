from django.contrib import admin
from .models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}  # This field can make slug automatically
    list_filter = ("author", "rating")  # This field can add filters in the admin 
    list_display = ("title", "author", "rating")

admin.site.register(Book, BookAdmin)
