from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TextEntry(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UrlEntry(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Summary(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)
    text_entry = models.ForeignKey(TextEntry, on_delete=models.CASCADE, null=True, blank=True)
    url_entry = models.ForeignKey(UrlEntry, on_delete=models.CASCADE, null=True, blank=True)
    summary_text = models.TextField()
    word_count = models.IntegerField()
    tone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Summary of {self.document.title if self.document else self.text_entry.title if self.text_entry else self.url_entry.title}'

    def save(self, *args, **kwargs):
        self.tone = self.tone.capitalize()
        super(Summary, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('summary_detail', args=[str(self.id)])
