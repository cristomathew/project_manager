from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from model_utils import Choices
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="name")
    class_div = models.CharField(max_length=10)
    rollno = models.CharField(max_length=10)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Grade(models.Model):
    STATUS = Choices('Design Project', 'ASDL Lab')
    Abstract_Marks = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)],default=0)
    Code_Marks = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)],default=0)
    Idea = models.BooleanField(default=False)
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    StudentName = models.CharField(max_length=30, default="Name")
    Subject = models.CharField(max_length=30,default="Design Project",choices=STATUS)
    class_div = models.CharField(max_length=10,null=True)
    rollno = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.StudentName
