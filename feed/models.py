from django.db import models
from profiles.models import Profile
# Create your models here.



class Post(models.Model):

    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='post_creator')
    image = models.ImageField(blank=True,null=True,upload_to="media")
    title = models.CharField(blank=True,null=True,max_length=255)
    description = models.TextField(blank=True,null=True,max_length=1024)
    liked_by = models.ManyToManyField(Profile,related_name='liked_by',blank=True)
    date_published = models.DateTimeField(auto_now=True,blank=True)
    
    class Meta:
        ordering = ('-date_published',)
    def __str__ (self):
        return self.title
    


class Comment(models.Model):

    author_id  = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='posts')
    post_id  = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField(blank=True,null=True)
    date_commented = models.DateTimeField(auto_now=True,blank=True)


    class Meta:
        ordering = ('-date_commented',)
    







    
