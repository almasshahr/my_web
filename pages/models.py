from django.db import models


class pages(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    auther = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} , {self.auther}'
