from django.db import models

# Create your BLOG models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog_images/")

    def __self__(self):
        return self.title

    def short_body(self):
        return self.body[:50]

    def pretty_published_date(self):
        return self.published_date.strftime("%b %e %Y")
