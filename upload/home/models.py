from django.db import models

# Create your models here.


class UploadImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="home/")
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user} posted {self.title}'
