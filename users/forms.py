from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Grade
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','rollno','class_div','image']
class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','image']
class StudentGrade(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['Abstract_Marks','Code_Marks','Student','Subject']
class StudentIdeaGrade(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['Idea']
