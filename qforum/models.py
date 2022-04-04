from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Waiting'), (1, 'Approved'))

class Forum(models.Model):
    """
    A forum class
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name="forum_topics")
    email = models.EmailField()
    topic = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    link = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.topic)
 

class Discussion(models.Model):
    """
    A particular discussion thread
    """
    forum = models.ForeignKey(Forum, default="Economy today", on_delete=models.CASCADE, related_name="discussion_threads")
    discussion_body = models.TextField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)