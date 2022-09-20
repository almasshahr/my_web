from .models import blogPost
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy


class PostListview(generic.ListView):
    model = blogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'all_post_pub'

    def get_queryset(self):
        return blogPost.objects.filter(status='pub').order_by(
            '-created_modified')


class PostDetail(generic.DetailView):
    model = blogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class AddPost(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/add_post.html'


class PostEit(generic.UpdateView):
    model = blogPost
    form_class = PostForm
    template_name = 'blog/add_post.html'


class PostDelete(generic.DeleteView):
    model = blogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_blog')
