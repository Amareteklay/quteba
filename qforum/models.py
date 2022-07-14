from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = ((0, 'Waiting'), (1, 'Approved'))


class Category(models.Model):
    """
    A class to create categories of forums.
    """
    subject = models.CharField(default='Uncategorized', max_length=50)
    description = models.TextField(max_length=255)
    name = models.ForeignKey(User, on_delete=models.CASCADE,
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
    A class for discussion forum thread
    """
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="forum_topics")
    topic = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="threads")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    up_votes = models.ManyToManyField(User, blank=True,
                                      related_name='up_votes')
    down_votes = models.ManyToManyField(User, blank=True,
                                        related_name='down_votes')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.topic)

    def no_of_upvotes(self):
        """ Count the number of up votes """
        return self.up_votes.count()

    def no_of_downvotes(self):
        """ Count the number of down votes """
        return self.down_votes.count()

    def get_absolute_url(self):
        return reverse('qforum:thread_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic)
        super(Thread, self).save(*args, **kwargs)


class Comment(models.Model):
    """
    A particular comment posted to a thread
    """
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE,
                               related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="forum_comments")
    content = models.TextField(null=True, max_length=255)
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='replies')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, blank=True,
                                   related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True,
                                      related_name='comment_dislikes')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.content}"

    def no_of_likes(self):
        """ Count the number of likes """
        return self.likes.count()

    def no_of_dislikes(self):
        """ Count the number of dislikes """
        return self.dislikes.count()

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
