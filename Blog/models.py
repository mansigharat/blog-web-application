from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) # when post is created this execute
    author = models.ForeignKey(User, on_delete = models.CASCADE) #if user get deleted all the post of that user also get deleted

    def __str__(self):
        return self.title