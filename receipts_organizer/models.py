from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Category model
class Categories(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


# Entries model
class Entries(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_name')
    title = models.CharField(max_length=30)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='Category')
    image = CloudinaryField("image", blank=True)
    amount = models.IntegerField(blank=True)
    date_of_purchase = models.DateField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.title
