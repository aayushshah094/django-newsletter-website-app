from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_pic = models.ImageField(default="default.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    followers = models.ManyToManyField(User, null = True, blank = True, on_delete=models)
    
    def __str__(self):
	    return self.name

class Post(models.Model):
    source = models.TextField(max_length=250, null=True, blank=True)
    author = models.TextField(max_length=250,null=True, blank=True)   
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=250, null=True, blank=True)
    urlToImage = models.ImageField(null=True, blank=True)
    publishedAt = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')



    def __str__(self):
        return self.title

    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (('Like', 'Like'), ('Unlike', 'Unlike'))

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    posts = models.ForeignKey(Post,  null=True, blank = True, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.posts} -- {0.value}'
        return template.format(self)
    
    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked +=1
        return total_liked


    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked = 0 
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked
