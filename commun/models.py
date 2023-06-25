from cProfile import label
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from numpy import require
from django.utils.translation import gettext_lazy as _

class Post(models.Model) :
    title = models.CharField(_('title'), max_length=100)
    content = models.TextField(_('content'))
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk' : self.pk})

    labels = {
        'title' : _('title'),
        'content' : _('content'),
    }


class Comment(models.Model): 
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return ('Comment by {} on {}').format(self.name, self.post) 