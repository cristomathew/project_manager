from django.urls import path
from . views import (
PostDetailView,
DocumentCreateView,
PostListView,
DocumentUpdateView,
PostDeleteView,
IdeaListView,
IdeaUpdateView,
IdeaDeleteView,
IdeaCreateView,
IdeaDetailView,
UserPostListView,
UserIdeaListView
)
from . import views
urlpatterns = [
    path('abstract', views.home, name="ADSL-abstract-home"),
    path('user/<username>/abstract',UserPostListView.as_view(), name="ADSL-user-abstract"),
    path('abstract/public', PostListView.as_view(), name="ADSL-abstract-public"),
    path('abstract/new/', DocumentCreateView, name="ADSL-abstract-create"),
    path('abstract/<pk>/update/', DocumentUpdateView.as_view(), name="ADSL-abstract-update"),
    path('abstract/<pk>/delete/', PostDeleteView.as_view(), name="ADSL-abstract-delete"),
    path('abstract/<pk>/', PostDetailView.as_view(), name="ADSL-abstract-detail"),
    path('idea', views.idea_home, name="ADSL-idea-home"),
    path('user/<username>/idea', UserIdeaListView.as_view(), name="ADSL-user-idea"),
    path('idea/public', IdeaListView.as_view(), name="ADSL-idea-public"),
    path('idea/new/', IdeaCreateView.as_view(), name="ADSL-idea-create"),
    path('idea/<pk>/update/', IdeaUpdateView.as_view(), name="ADSL-idea-update"),
    path('idea/<pk>/delete/', IdeaDeleteView.as_view(), name="ADSL-idea-delete"),
    path('idea/<pk>/', IdeaDetailView.as_view(), name="ADSL-idea-detail"),
]
