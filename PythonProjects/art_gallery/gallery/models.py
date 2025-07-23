from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"
        ordering = ['title']