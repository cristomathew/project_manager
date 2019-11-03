from django.shortcuts import render
from django.http import HttpResponse
from .models import Abstract, Document
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    context = {
        'posts': Document.objects.all(),
        'title': 'Design Project',
    }
    return render(request, 'DP/home.html',context)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
