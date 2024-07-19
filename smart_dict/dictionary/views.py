from django.shortcuts import render, redirect
from .models import Word ,TimeEntry
from django.utils import timezone
from .forms import WordForm
import random
from collections import defaultdict
from datetime import timedelta


def index(request):
    total_words = Word.total_words()
    words_today = Word.words_learned_today()
    words_week = Word.words_learned_this_week()
    words_month = Word.words_learned_this_month()
    weekly_words = Word.get_words_of_the_week()
    time_entries = TimeEntry.objects.all()
    grouped_entries = defaultdict(list)
    total_times = defaultdict(timedelta)

    for entry in time_entries:
        date = entry.start_time.date()
        grouped_entries[date].append(entry)
        if entry.duration:
            total_times[date] += entry.duration

    context = {
        'total_words': total_words,
        'words_today': words_today,
        'words_week': words_week,
        'words_month': words_month,
        'weekly_words': weekly_words,
    }

    return render(request, 'index.html', context)

def german_page(request):
    # weekly_words = Word.get_words_of_the_week()
    weekly_words = Word.objects.all()
    
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('german_page')
    else:
        
        form = WordForm()
    weekly_words = list(weekly_words)
    random.shuffle(weekly_words)
    words = Word.objects.all()
    return render(request, 'german.html',{'form': form ,'words': words , 'weekly_words': weekly_words })






def start_timer(request):
    time_entry = TimeEntry.objects.create(start_time=timezone.now())
    return redirect('index')

def stop_timer(request, entry_id):
    time_entry = TimeEntry.objects.get(id=entry_id)
    time_entry.stop_time = timezone.now()
    time_entry.calculate_duration()
    print(time_entry.duration)
    return redirect('index')