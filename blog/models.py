from django.db import models

# Create your BLOG models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog_images/")
