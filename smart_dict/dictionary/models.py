from django.db import models

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
    
