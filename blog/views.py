from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# model ffrom models.py
from .models import Post, Comment
# class-base views login_Requred and if it is same user for update a post
# so different users cannot change different users post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# class-base-view django builtin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


from .forms import CommentForm

# >>> from django.core.paginator import Paginator
# >>> posts=['1','2','3','4','5']
# >>> p = Paginator(posts,2)
# >>> p1 = p.page(1)
# >>> p1
# <Page 1 of 3>
# >>> p1.object_list
# ['1', '2']
# >>> p1.has_previous()
# False
# >>> p1.has_next()
# True
# >>> p1.next_page_number()
# 2




def home(request):
    # all the post
    posts = Post.objects.all()

    context = {"posts": posts}
    return render(request, "blog/home.html", context)

#login required and class-base views
class PostListView(LoginRequiredMixin,ListView):
    #chooose the model
    model = Post
    # if it not required send them to login reverse
    login_url = 'login'
    # the template class-base looking for it
    # app_name/model_viewtype.html
    template_name = "blog/home.html"  # <app>/model_<viewtype>.html
    # when we send to html we want to render them as posts
    context_object_name = "posts"
    # order by newest
    ordering = ["-date_posted"]

    paginate_by = 8


#login required and class-base views
class UserPostListView(LoginRequiredMixin,ListView):
    #chooose the model
    model = Post
    # if it not required send them to login reverse
    login_url = 'login'
    # the template class-base looking for it
    # app_name/model_viewtype.html
    template_name = "blog/user_posts.html"  # <app>/model_<viewtype>.html
    # when we send to html we want to render them as posts
    context_object_name = "posts"
    # order by newest
    ordering = ["-date_posted"]
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


login required and class-base views
class PostDetailView(LoginRequiredMixin,DetailView):
    # chooose the model
    model = Post


#login required and class-base views
class PostCreateView(LoginRequiredMixin,CreateView):
    # chooose the model
    model = Post
    # specify the fields
    fields = ['title', 'content']

    # ckeck if form is valid and this is built in func
    # rewrite form_valid func so when it check it is gonna run that func
    def form_valid(self, form):
        # for author send current user to form
        form.instance.author = self.request.user
        return super().form_valid(form)

#login required and class-base views
# make sure only the post user can update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post

    fields = ["title", 'content']

    # ckeck if form is valid and this is built in func
    # rewrite form_valid func so when it check it is gonna run that func
    def form_valid(self,form):
        # for author send current user to form
        form.instance.author = self.request.user
        return super().form_valid(form)

    # make sure only the post user can update post
    def test_func(self):
        # get the current post
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


#login required and class-base views
# make sure only the post user can delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # after succes where to send
    success_url ="/"
    # make sure only the post user can update post
    def test_func(self):
        # get the current post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {}
    return render(request, "blog/home.html", context)

def comment(request,pk):
    form = CommentForm()
    comments = Comment.objects.filter(post__id=pk)
    post = Post.objects.get(id=int(pk))
    context = {"form": form, "post": post, "comments": comments}

    if request.method == "POST":
        user = request.user
        subject = request.POST.get("content")
        print(subject ,user,post )
        try:
            post.comment_set.create(user=user,content=subject)
        except:
            print("didnt work out")
        return redirect("blog-comment", pk=post.id)


    return render(request, "blog/comment.html", context)

