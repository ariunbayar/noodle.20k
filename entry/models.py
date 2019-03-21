from django.db import models
from django.utils.text import slugify


class Post(models.Model):

    slug = models.SlugField(max_length=100, allow_unicode=True)
    title = models.CharField(max_length=500)

    content = models.TextField()
    content_html = models.TextField()

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)
