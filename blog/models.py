from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title     = models.CharField(max_length=200)
    slug      = models.SlugField(unique=True, blank=True)
    author    = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category  = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content   = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    featured  = models.ImageField(upload_to='blog/', null=True, blank=True)

    class Meta:
        ordering = ['-published']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

