from django.db import models
from django.shortcuts import reverse


class blogPost(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_dataTime = models.DateTimeField(auto_now_add=True)
    created_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title  # return f'{self.title} , {self.auther}'

    def get_absolute_url(self):
        return reverse('post_detail_blog', args=[self.id])
