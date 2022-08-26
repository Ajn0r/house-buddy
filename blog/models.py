from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Models for the blog
BLOG_CATEGORIES = (
    (0, 'Unspecified'),
    (1, 'Homeimprovments'),
    (2, 'Savings'),
    (3, 'Garden'),
    (4, 'Usefull tips'),
    (5, 'Home'),
    (6, 'Evereyday life'),
    (7, 'Other')
)
PROCESS = (
    (0, 'Draft'),
    (1, 'Published')
)


class Blogpost(models.Model):
    """
    The blogpost model, this has been greatly inspired
    by Code Institute 'I think therefore I blog' module
    """
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField("image", default='placeholder')
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    category = models.IntegerField(choices=BLOG_CATEGORIES, default=0)
    process = models.IntegerField(choices=PROCESS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns the title as a string
        """
        return f"{self.title}"

    def total_likes(self):
        """
        Method for getting the total amount of likes
        """
        return self.likes.count()


class Comments(models.Model):
    """
    Comment model, this has also been inspired by Code Institue
    'I think therefore I blog' module
    """
    post = models.ForeignKey(
        Blogpost, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    posted_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        """
        returns the name and content of the comment as strings
        """
        return f'Comment {self.content} by {self.name}'
