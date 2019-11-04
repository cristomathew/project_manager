from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class ADSL_Abstract(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_submitted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class_div = models.CharField(max_length=10, default='Null')
    rollno = models.CharField(max_length=10, default='No')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('DP-idea-detail', kwargs={'pk': self.pk})
class ADSL_Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('ADSL-abstract-detail', kwargs={'pk': self.pk})
