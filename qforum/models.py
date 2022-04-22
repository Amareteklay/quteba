from django.db import models
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('qforum:thread_detail', args=[self.slug])
    
    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic)
        super(Thread, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    A particular comment posted to a thread
    """
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments', null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f"{self.body}"

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)


class Vote(models.Model):
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,
                               related_name="votes")
    post = models.ForeignKey(Comment, on_delete=models.CASCADE,
                             related_name="votes")
    
    class Meta:
        ordering = ['up_count']