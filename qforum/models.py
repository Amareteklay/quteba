from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Waiting'), (1, 'Approved'))


class Category(models.Model):
    """
    A class to create categories of forums.
    """
    subject = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="categories")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    thread_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['subject']

    def __str__(self):
        return str(self.subject)


class Thread(models.Model):
    """
    A discussion thread in a certain category.
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name="forums")
    email = models.EmailField()
    topic = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="threads")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.topic)


class Post(models.Model):
    """
    A particular comment posted to a thread
    """
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,
                               related_name="posts")
    content = models.TextField(max_length=1000)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="comments")
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']
    
    def __str__(self):
        return str(self.thread)
    

class Vote(models.Model):
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,
                               related_name="votes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="votes")
    
    class Meta:
        ordering = ['up_count']