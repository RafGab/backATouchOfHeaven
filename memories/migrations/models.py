from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memories")
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
