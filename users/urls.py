from django.urls import path
from . import views
from .views import PostListView
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('register/',views.register, name="register"),
    path('grade/',views.studentgrade, name="studentgrade"),
    path('mygrade/',PostListView.as_view(), name="mygrade"),
    path('students/',views.all_grade, name="allgrades"),
    path('profile/',views.teacherprofile, name="teacher-profile"),
    path('student-profile/',views.studentprofile, name="student-profile"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
