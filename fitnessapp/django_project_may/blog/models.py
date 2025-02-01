from djongo import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    id = models.ObjectIdField()  
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_post'  