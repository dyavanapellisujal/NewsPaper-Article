from django.db import models
from django_project import settings
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("articleslist")


# Create your models here.
