from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Ideas, Document
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import DocumentForm
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def home(request):
    context = {
        'posts': Document.objects.all(),
        'title': 'Design Project',
    }
    return render(request, 'DP/abstract_home.html',context)

#
class PostListView(LoginRequiredMixin,ListView):
    model = Document
    template_name = 'DP/abstract_public.html'
    context_object_name = 'posts'
    ordering = ['uploaded_at']
class UserPostListView(LoginRequiredMixin,ListView):
    model = Document
    template_name = 'DP/user_abstract.html'
    context_object_name = 'posts'
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Document.objects.filter(author=user).order_by('uploaded_at')
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Document
    template_name = 'DP/abstract_detail.html'

@login_required
def DocumentCreateView(request):
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Document Uploaded')
            return redirect('DP-abstract-detail', form.instance.pk)
    else:
        form = DocumentForm()

    context = {
        'form': form
        }
    return render(request, 'DP/abstract_create.html', context)

class DocumentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Document
    fields = ['title','description','document']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Document
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




@user_passes_test(lambda u: u.is_superuser)
def idea_home(request):
    context = {
        'posts': Ideas.objects.all(),
        'title': 'Design Project',
    }
    return render(request, 'DP/idea_home.html',context)

#
class IdeaListView(LoginRequiredMixin,ListView):
    model = Ideas
    template_name = 'DP/idea_public.html'
    context_object_name = 'posts'
    ordering = ['date_submitted']
class UserIdeaListView(LoginRequiredMixin,ListView):
    model = Ideas
    template_name = 'DP/user_idea.html'
    context_object_name = 'posts'
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ideas.objects.filter(author=user).order_by('uploaded_at')
class IdeaDetailView(LoginRequiredMixin,DetailView):
    model = Ideas
    template_name = 'DP/idea_detail.html'
class IdeaCreateView(LoginRequiredMixin,CreateView):
    model = Ideas
    fields = ['title','summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IdeaUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Ideas
    fields = ['title','summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False
class IdeaDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Ideas
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
