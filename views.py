from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.utils import translation
from .models import Post
from .forms import CommentForm
from users.models import Profile

# Create your views here.




def home(request) :
    if request.user.is_authenticated:
        translation.activate(Profile.language)
    print(Profile.language)
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'commun/home.html', context)

    

    

class PostListView(ListView) :
    model = Post
    template_name = 'commun/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    

def post_detail(request, pk):
    # if request.user.is_authenticated:
    #     translation.activate(Profile.language)
    post = get_object_or_404(Post, pk = pk)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if hasattr(request.user, 'lang'):
        request.session['django_language'] = request.user.lang

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.author = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'commun/post_detail.html', context)

class PostCreateView(LoginRequiredMixin, CreateView) : 
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

    labels = {
        'title' : _('title'),
        'content' : _('content')
    }

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    labels = {
        'title' : _('title'),
        'content' : _('content')
    }

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    labels = {
        'title' : _('title'),
        'content' : _('content')
    }
    
class UserPostListView(ListView):
    model = Post
    template_name = 'commun/user_posts.html'
    context_object_name = _('posts')
    paginate_by = 5

    def get_queryset(self) :
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    labels = {
        'title' : _('title'),
        'content' : _('content')
    }


def about(request) :
    # if request.user.is_authenticated:
    #     translation.activate(Profile.language)
    return render(request, 'commun/about.html')