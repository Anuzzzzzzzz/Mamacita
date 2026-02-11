from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
