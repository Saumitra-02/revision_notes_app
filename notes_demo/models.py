# In myapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    extracted_text = models.TextField(blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.content[:50]  # Display the first 50 characters of the note as its string representation
