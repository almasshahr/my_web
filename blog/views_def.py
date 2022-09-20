from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import blogPost
from .forms import NewPostForm


def Post_Blog(request):
    all_post = blogPost.objects.filter(status='pub').order_by(
        '-created_modified')
    return render(request, 'blog/post_list.html', {'all_post': all_post})


def Post_Detail_Blog(request, pk):  # primary key
    post = get_object_or_404(blogPost, pk=pk)
    # post = blogPost.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def Add_Post_Blog(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            # form = NewPostForm()
            return redirect('post_blog')
    else:
        form = NewPostForm()
    return render(request, 'blog/add_post.html', context={'form': form})


def Post_edit_Blog(request, pk):
    post = get_object_or_404(blogPost, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        # form = NewPostForm()
        return redirect('post_blog')
    return render(request, 'blog/add_post.html', context={'form': form})


def Post_Delete_Blog(request, pk):
    post = get_object_or_404(blogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_blog')
    return render(request, 'blog/delete_post.html', context={'post': post})
