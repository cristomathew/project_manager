from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Abstract(models.Model):
    title = models.CharField(max_length=100)
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class_div = models.CharField(max_length=10, default='Null')
    rollno = models.CharField(max_length=10, default='No')

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class_div = models.CharField(max_length=10, default='Null')
    rollno = models.CharField(max_length=10, default='No')
    name = models.CharField(max_length=10, default='Name')
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
