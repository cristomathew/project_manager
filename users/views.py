from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, StudentProfileUpdateForm, TeacherProfileUpdateForm, StudentGrade
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
ListView
)
from .models import Grade
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
def teacherprofile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = TeacherProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile has been successfully update!')
            return redirect('teacher-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = TeacherProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form

    }
    return render(request, 'users/profile.html', context)

@user_passes_test(lambda u: u.is_superuser)
def studentgrade(request):
    if request.method == "POST":
        form = StudentGrade(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('Student')
            form.instance.StudentName = username.profile.name
            form.instance.class_div = username.profile.class_div
            form.instance.rollno = username.profile.rollno
            form.save()
            name = username.profile.name
            clas = username.profile.class_div
            rollno = username.profile.rollno
            messages.success(request, f'Grade has been successfully uploaded for {name} rollno {rollno} of {clas}')
            return redirect('/')
    else:
        form = StudentGrade()

    context = {
        'form': form,
        'title':'Student Grade'

    }
    return render(request, 'users/grade.html', context)
@user_passes_test(lambda u: u.is_superuser)
def all_grade(request):
    context = {
        'posts': Grade.objects.all(),
        'title': 'Student Grade',
    }
    return render(request, 'users/grade_users.html',context)
class PostListView(LoginRequiredMixin,ListView):
    model = Grade
    template_name = 'users/my_grade.html'
    context_object_name = 'posts'
@login_required
def studentprofile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = StudentProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile has been successfully update!')
            return redirect('student-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = StudentProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form

    }
    return render(request, 'users/profile.html', context)
