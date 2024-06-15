from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView,FormView, UpdateView,DeleteView,CreateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.http import HttpResponse
# Create your views here.
def indexView (request):
    return render(request, "index.html")


class IndexView(TemplateView):
    template_name= 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context

class PostList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required ='blog.view_post'
    queryset = Post.objects.all()
    context_object_name = "posts"
    ordering = 'id'
    #def get_queryset(self):
        #posts = Post.objects.filter(status= True)
        #return posts
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'
    def form_valid(self, form):
        form.instance.author = self.request.user 
        form.save()
        return super().form_valid(form)
        
class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"

def api_post_list_view(request):
    return HttpResponse("ok")