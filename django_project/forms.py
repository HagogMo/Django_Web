from .models import Comment
from django import forms
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        exclude = ('author', 'email')

        labels = {
            'body' : _('content')
        }