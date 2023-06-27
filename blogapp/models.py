from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    #Adds topic user is blogging about
    topic=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        #return string representation of model topic
        return self.topic
    
class Post(models.Model):
    #adds a blog post user is blogging about
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,default='')
    post=models.TextField()
    publication_date=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural='posts'

    def __str__(self):
       #returns string representation of model
       return self.post[:50]+'...'
