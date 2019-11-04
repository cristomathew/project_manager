from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ADSL_Abstract, ADSL_Document
from .forms import DocumentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def home(request):
    context = {
        'posts': ADSL_Document.objects.all(),
        'title': 'Design Project',
    }
    return render(request, 'ADSL/abstract_home.html',context)


class PostListView(LoginRequiredMixin,ListView):
    model = ADSL_Document
    template_name = 'ADSL/abstract_public.html'
    context_object_name = 'posts'
    ordering = ['uploaded_at']
class UserPostListView(LoginRequiredMixin,ListView):
    model = ADSL_Document
    template_name = 'ADSL/user_abstract.html'
    context_object_name = 'posts'
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ADSL_Document.objects.filter(author=user).ordery_by('uploaded_at')

class PostDetailView(LoginRequiredMixin,DetailView):
    model = ADSL_Document
    template_name = 'ADSL/abstract_detail.html'
def DocumentCreateView(request):
    if request.method == "POST":
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, f'Document Uploaded')
            return redirect('ADSL-abstract-detail', form.instance.pk)
    else:
        form = DocumentForm()

    context = {
        'form': form
        }
    return render(request, 'ADSL/abstract_create.html', context)

class DocumentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ADSL_Document
    fields = ['title','description','document']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = ADSL_Document
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# ideas
@user_passes_test(lambda u: u.is_superuser)
def idea_home(request):
    context = {
        'posts': ADSL_Abstract.objects.all(),
        'title': 'Design Project',
    }
    return render(request, 'ADSL/idea_home.html',context)

#
class IdeaListView(LoginRequiredMixin,ListView):
    model = ADSL_Abstract
    template_name = 'ADSL/idea_public.html'
    context_object_name = 'posts'
    ordering = ['date_submitted']
class UserIdeaListView(LoginRequiredMixin,ListView):
    model = ADSL_Abstract
    template_name = 'ADSL/user_idea.html'
    context_object_name = 'posts'
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ADSL_Abstract.objects.filter(author=user).ordery_by('uploaded_at')
class IdeaDetailView(LoginRequiredMixin,DetailView):
    model = ADSL_Abstract
    template_name = 'ADSL/idea_detail.html'


class IdeaCreateView(LoginRequiredMixin,CreateView):
    model = ADSL_Abstract
    fields = ['title','description']
    template_name = 'ADSL/idea_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IdeaUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ADSL_Abstract
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False
class IdeaDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = ADSL_Abstract
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
