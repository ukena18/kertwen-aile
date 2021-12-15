from django.db import models
# for date_posted so we can change it if we want it
from django.utils import timezone
# user model
from django.contrib.auth.models import User
# reverse the url with kwarg
# let say you create a post request and send to that post  but it takes time to create the post
# it is like async and await in the javascript
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # auto_now=True => last updated time
    # auto_now_add=True => first created and cannot be changed
    # default=timezone.now => created time, but we can manually change
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

    # after it created send the user to that url
    # async func take time to create post so it  just make sure it is created then create an url and send it to url
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk":self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

# check this out
"""
>>> post = Post.objects.get(id=1) 
>>> post
<Post: blog 1>
>>> post.author
<User: azrame>
>>> post.author.email
'azrame@ramazan.com'
>>> user.post_set.all() 
<QuerySet [<Post: blog 1>, <Post: blog 2>]>
>>> user.post_set.create>>> user.post_set.create(title="blog 1",content="for blog 1 we had")
'it is created and had current user'


"""

"""
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: zackme>, <User: azrame>, <User: zehrame>]>
>>> User.objects.first()
<User: zackme>
>>> User.objects.filter(username='zehrame') 
<QuerySet [<User: zehrame>]>
>>> User.objects.filter(username='zehrame').first() 
<User: zehrame>
>>> user = User.objects.filter(username='zehrame').first() 
>>> user.id
3
>>> user.pk
3
>>> user = User.objects.get(id=2) 
>>> user
<User: azrame>
"""


"""
>>> Post.objects.all()
<QuerySet []>
>>> post_1 = Post(title="blog 1",content="for blog 1 we had", author=user)
>>> post_1.save()
>>> Post.objects.all()                                                     
<QuerySet [<Post: Post object (1)>]>
>>> Post.objects.all()

"""

