from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Post
from .forms import BlogForm, PostForm


def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')


@login_required
def blogs(request):
    """Shows all blogs."""
    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


@login_required
def blog(request, blog_id):
    """Shows a single blog and all its posts."""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)


@login_required
def new_blog(request):
    """Adds a new blog."""
    if request.method != 'POST':  # user is requesting a blank form
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blogs:blogs')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def new_post(request, blog_id):
    """Adds a new post for a particular blog."""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request)

    if request.method != 'POST':  # user is requesting a blank form
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)
    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edits an existing post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # Initial request, pre-fill form with the current post
        form = PostForm(instance=post)
    else:
        # POST data submitted and process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


def check_blog_owner(blog, request):
    """Checks of the current user is the owner of the requested page."""
    if blog.owner != request.user:
        raise Http404
