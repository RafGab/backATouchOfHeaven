from django.db import models


class Memory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return '__all__'

