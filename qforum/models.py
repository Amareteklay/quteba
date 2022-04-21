from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, 'Waiting'), (1, 'Approved'))


class Category(models.Model):
    """
    A class to create categories of forums.
    """
    subject = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
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
    topic = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="category_threads")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.topic)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic)
        super(Thread, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    A particular comment posted to a thread
    """
    content = models.TextField(max_length=1000)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    commented_on = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread_comments', null=True)

    class Meta:
        ordering = ['-commented_on']
    
    def __str__(self):
        return self.content


class Reply(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies", null=True)
    message = models.TextField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replies', null=True)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return self.message


class Vote(models.Model):
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,
                               related_name="votes")
    post = models.ForeignKey(Comment, on_delete=models.CASCADE,
                             related_name="votes")
    
    class Meta:
        ordering = ['up_count']