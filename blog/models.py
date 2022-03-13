from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    contract = models.CharField(max_length=10, blank= True, null=True)
    profile_img = models.ImageField(upload_to='image/', blank=True, null=True)
    bio = models.CharField(default='No bio.......', max_length=50,blank= True, null=True)
    friends = models.ManyToManyField("self",blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def get_no_of_friends(self):
        return self.friends.all().count()

    def get_friends(self):
        return self.friends.all()
    

class Blog(models.Model):

    title = models.CharField(max_length=50)
    desc = models.TextField()
    banner_img = models.ImageField(upload_to='posts', validators=[FileExtensionValidator] )
    liked = models.ManyToManyField(Profile,blank=True, related_name='likes')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author',blank =True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def no_likes(self):
        return self.liked.all().count()
    
  
            
