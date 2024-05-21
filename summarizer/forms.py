from django import forms
from .models import Document, TextEntry, UrlEntry

TONE_CHOICES = [
    ('formal', 'Formal'),
    ('informal', 'Informal'),
    ('professional', 'Professional'),
    ('friendly', 'Friendly'),
    ('humorous', 'Humorous'),
    ('serious', 'Serious'),
    ('sarcastic', 'Sarcastic'),
    ('optimistic', 'Optimistic'),
    ('pessimistic', 'Pessimistic'),
    ('neutral', 'Neutral'),
    ('respectful', 'Respectful'),
    ('aggressive', 'Aggressive'),
    ('compassionate', 'Compassionate'),
    ('enthusiastic', 'Enthusiastic'),
    ('motivational', 'Motivational'),
    ('authoritative', 'Authoritative'),
    ('critical', 'Critical'),
    ('cautious', 'Cautious'),
    ('joyful', 'Joyful'),
    ('melancholic', 'Melancholic'),
    ('empathetic', 'Empathetic'),
    ('grateful', 'Grateful'),
    ('pragmatic', 'Pragmatic'),
    ('playful', 'Playful'),
    ('romantic', 'Romantic'),
    ('apologetic', 'Apologetic'),
]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            file_ext = file.name.split('.')[-1].lower()
            if file_ext not in ['pdf', 'pptx', 'xlsx', 'docx', 'txt']:
                raise forms.ValidationError("Unsupported file type. Supported file types are: PDF, PPTX, XLSX, DOCX, TXT.")
        return file

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
