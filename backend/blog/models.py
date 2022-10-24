from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_dictionary_path(instance,filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    # This is a post
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to=user_dictionary_path, default='blog/default.jpg', blank=True, null= True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null= False, unique= True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    
    # This is how we look up for posts
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

