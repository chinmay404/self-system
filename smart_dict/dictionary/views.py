from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm


def index(request):
    words = Word.objects.all()
    return render(request, 'index.html', {'words': words})


def german_page(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = WordForm()
    return render(request, 'german.html',{'form': form})