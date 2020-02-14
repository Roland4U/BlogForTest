from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name='posts')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_det", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse('post_edit', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
    
    def get_delete_url(self):
        return reverse('post_del', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("tag_det", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse('tag_edit', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_del', kwargs={'slug': self.slug})
    

    def __str__(self):
        return self.title
