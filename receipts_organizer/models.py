from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Category model
class Categories(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_name', null=True)

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='unique_category')
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


# Entries model
class Entries(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='Category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = CloudinaryField('image', default='placeholder')
    amount = models.IntegerField(blank=True, null=True, default=0)
    date_of_purchase = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.title
