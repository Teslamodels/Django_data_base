from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    Body = models.TextField()

    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])