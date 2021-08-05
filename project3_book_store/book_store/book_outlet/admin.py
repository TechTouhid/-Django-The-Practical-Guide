from django.contrib import admin
from .models import Book, Author, Address, Country


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}  # This field can make slug automatically
    list_filter = ("author", "rating")  # This field can add filters in the admin 
    list_display = ("title", "author", "rating")

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)