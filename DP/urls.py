from django.urls import path
from . views import (
PostDetailView,
PostListView,
DocumentCreateView,
DocumentUpdateView,
PostDeleteView,
IdeaListView,
IdeaUpdateView,
IdeaDeleteView,
IdeaCreateView,
IdeaDetailView,
UserIdeaListView,
UserPostListView
)
from . import views
urlpatterns = [
    path('abstract', views.home, name="DP-abstract-home"),
    path('user/<username>/abstract',UserPostListView.as_view(), name="DP-user-abstract"),
    path('abstract/public', PostListView.as_view(), name="DP-abstract-public"),
    path('abstract/new/', DocumentCreateView, name="DP-abstract-create"),
    path('abstract/<pk>/update/', DocumentUpdateView.as_view(), name="DP-abstract-update"),
    path('abstract/<pk>/delete/', PostDeleteView.as_view(), name="DP-abstract-delete"),
    path('abstract/<pk>/', PostDetailView.as_view(), name="DP-abstract-detail"),
    path('idea', views.idea_home, name="DP-idea-home"),
    path('user/<username>/idea', UserIdeaListView.as_view(), name="DP-user-idea"),
    path('idea/public', IdeaListView.as_view(), name="DP-idea-public"),
    path('idea/new/', IdeaCreateView.as_view(), name="DP-idea-create"),
    path('idea/<pk>/update/', IdeaUpdateView.as_view(), name="DP-idea-update"),
    path('idea/<pk>/delete/', IdeaDeleteView.as_view(), name="DP-idea-delete"),
    path('idea/<pk>/', IdeaDetailView.as_view(), name="DP-idea-detail"),
]
