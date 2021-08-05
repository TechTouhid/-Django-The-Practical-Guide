from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True,
                            db_index=True)  # Harry Potter => harry-potter-1, db_index can improve the performance

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    # we added a prepopulated_fields = {"slug": ("title",)} in admin so we don't need this function now
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
