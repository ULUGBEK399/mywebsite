from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords= models.CharField(max_length=255)
    description=models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
