from django.db import models
from django.utils import timezone
from datetime import timedelta


class Word(models.Model):
    word = models.CharField(max_length=255, primary_key=True)
    meaning = models.TextField()
    pronunciation = models.TextField(null=True, blank=True)
    sentence1 = models.TextField(null=True, blank=True)
    sentence2 = models.TextField(null=True, blank=True)
    sentence3 = models.TextField(null=True, blank=True)
    sentence4 = models.TextField(null=True, blank=True)
    sentence5 = models.TextField(null=True, blank=True)
    types = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    last_seen_date = models.DateField(auto_now=True)
    learned = models.BooleanField(default=True)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    last_tested_date = models.DateField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.word
    
    @classmethod
    def total_words(cls):
        return cls.objects.count()

    @classmethod
    def words_learned_today(cls):
        today = timezone.now().date()
        return cls.objects.filter(added_date=today).count()

    @classmethod
    def words_learned_this_week(cls):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        return cls.objects.filter(added_date__gte=start_of_week).count()

    @classmethod
    def words_learned_this_month(cls):
        today = timezone.now().date()
        start_of_month = today.replace(day=1)
        return cls.objects.filter(added_date__gte=start_of_month).count()
    
    
    @classmethod
    def get_words_of_the_week(cls):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        return cls.objects.filter(added_date__gte=start_of_week)





class TimeEntry(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    stop_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def calculate_duration(self):
        if self.start_time and self.stop_time:
            self.duration = self.stop_time - self.start_time
            self.save()