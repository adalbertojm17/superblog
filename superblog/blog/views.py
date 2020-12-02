from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, Category, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, request


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['date']

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cats_menu'] = cats_menu
        return context


class ArticlesView(DetailView):
    model = Post
    template_name = 'articles.html'


    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        context['cats_menu'] = cats_menu
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_like = post.total_likes()
        context["total_like"] = total_like
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCommentView(CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def CategoryView(request, cats):
    category = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category': category})


def CategoryListView(request, cats):
    cats_list = Category.objects.all()
    return render(request, 'category_list.html', {'cats_list': cats_list})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article', args={str(pk)}))


