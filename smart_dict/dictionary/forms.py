from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'meaning', 'pronunciation', 'sentence1', 'types', 'notes', 'tags']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'meaning': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'pronunciation': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'sentence1': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'types': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'notes': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'tags': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
