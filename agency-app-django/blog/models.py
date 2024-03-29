from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Post(models.Model):
      catagory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
      headline = models.CharField(max_length=240)
      sub_headline = models.CharField(max_length=250 , blank=True, null=True)
      thumbnail = models.ImageField(blank=True,null=True,upload_to='images/')
      body = RichTextField()
      author = models.ForeignKey(User, blank=True,on_delete= models.CASCADE, related_name='blog_post')
      slug = models.SlugField(blank=True,null=True)
      active = models.BooleanField(default=True)
      published = models.DateTimeField(default=timezone.now)
      created = models.DateTimeField(auto_now_add=True)

      def get_absolute_url(self):
          return reverse("blog:post_detail", args=[self.id,self.slug])
      

      class Meta:
            ordering = ('-published',)


      def __str__(self):
            return self.headline


class Comments(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_here')
      name = models.CharField(max_length=30)
      email = models.EmailField()
      comment = models.TextField(max_length=200)
      approved = models.BooleanField(default=False,null=True)
      date = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.comment



