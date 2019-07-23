from django.db import models


class Image(models.Model):

    class Meta:
        ordering = ['-created_at']

    uploaded_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    created_at = models.DateTimeField(auto_now_add=True)
