from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    objects = models.Manager()

    # def __str__(self):
    #     return self.owner


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.user', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta():
        ordering =['created']


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    owner = models.ForeignKey('auth.user', related_name='comments', on_delete=models.CASCADE)
    port = models.ForeignKey('Post', related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'categories'
# Create your models here.
