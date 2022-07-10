from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.functional import cached_property


class Profile(AbstractUser):
    first_name = models.CharField(blank=True,null=True,max_length=255)
    last_name = models.CharField(blank=True,null=True,max_length=255)
    biography = models.TextField(blank=True,null=True,max_length=1024)
    is_public = models.BooleanField(blank=True, null=True)


    constraints = [
        models.UniqueConstraint(fields=['username', 'email'], name='unique login details')
    ]

    friends  = models.ManyToManyField('self',symmetrical=True)


    
    @cached_property
    def cached_friends(self):
        return self.friends
    
    class Meta:
        ordering = ('-pk',)
    



    


        




