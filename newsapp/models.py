from django.db import models

# Create your models here.


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    source = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

