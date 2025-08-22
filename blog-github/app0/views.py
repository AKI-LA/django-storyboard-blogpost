from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def test_login(request):
    return render(request, 'app0/registration/login.html')


# View to list all blog posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    # For posts
    return render(request, 'app0/post_list.html',{'posts': posts})

# View to create a new blog post (only for logged-in users)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'app0/post_form.html',{'form': form})
