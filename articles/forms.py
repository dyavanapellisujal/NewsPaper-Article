from django import forms
from .models import Comment


class commentsform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")
