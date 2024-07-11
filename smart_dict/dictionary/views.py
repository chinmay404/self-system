from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm


def index(request):
    total_words = Word.total_words()
    words_today = Word.words_learned_today()
    words_week = Word.words_learned_this_week()
    words_month = Word.words_learned_this_month()
    weekly_words = Word.get_words_of_the_week()

    context = {
        'total_words': total_words,
        'words_today': words_today,
        'words_week': words_week,
        'words_month': words_month,
        'weekly_words': weekly_words,
    }

    return render(request, 'index.html', context)

def german_page(request):
    weekly_words = Word.get_words_of_the_week()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('german_page')
    else:
        
        form = WordForm()
    words = Word.objects.all()
    return render(request, 'german.html',{'form': form ,'words': words , 'weekly_words': weekly_words })