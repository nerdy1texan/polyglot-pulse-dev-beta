from django import forms
from .models import Document, TextEntry, UrlEntry

TONE_CHOICES = [
    ('formal', 'Formal'),
    ('informal', 'Informal'),
    ('professional', 'Professional'),
    ('friendly', 'Friendly'),
    ('humorous', 'Humorous'),
]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

class TextForm(forms.ModelForm):
    class Meta:
        model = TextEntry
        fields = ['title', 'text']

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlEntry
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class SummaryForm(forms.Form):
    word_count = forms.IntegerField(label='Word Count')
    tone = forms.ChoiceField(choices=TONE_CHOICES, label='Tone')
