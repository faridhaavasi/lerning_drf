from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title