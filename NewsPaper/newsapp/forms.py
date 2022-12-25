from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['options',
                  'title',
                  'text',
                  'postConnection',
                  'author',
                  ]

    def clean(self):
        cleaned_data = super().clean()
        title, text = cleaned_data.get('title'), cleaned_data.get('text')
        if text is not None and len(text) < 15:
            raise ValidationError({
                'text': 'Your text must contain at least 15 symbols.'
            })
        if title == text:
            raise ValidationError({'title': "Rewrite your title."})
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError("Please, capitalize the first word.")
        return title
