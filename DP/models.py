from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Ideas(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=300,blank=True)
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('DP-idea-detail', kwargs={'pk': self.pk})
class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    class_div = models.CharField(max_length=10, default='Null')
    rollno = models.CharField(max_length=10, default='No')
    name = models.CharField(max_length=10, default='No')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('DP-post-detail', kwargs={'pk': self.pk})
