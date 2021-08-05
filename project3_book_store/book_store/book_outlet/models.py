from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        #  use "verbose_name" for singular name
        verbose_name_plural = "Countries"  # To overwrite the singular and plural name in admin

    def __str__(self):
        return f"{self.name}"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        #  use "verbose_name" for singular name
        verbose_name_plural = "Address Entries"  # To overwrite the singular and plural name in admin


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               null=True)  # the Author model is foreign key here a reference of Author class
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True,
                            db_index=True)  # Harry Potter => harry-potter-1, db_index can improve the performance
    published_countries = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    # we added a prepopulated_fields = {"slug": ("title",)} in admin so we don't need this function now
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
