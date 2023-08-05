from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateField()
    source = models.URLField()

    def __str__(self):
        return self.title