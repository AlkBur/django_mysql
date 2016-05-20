from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True)
    likes = models.ManyToManyField(User, related_name='+', null=True)
    def __unicode__(self):              
        return self.title
    def get_url(self):
        return 'question/%s' % self.id

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True)
    def __unicode__(self):          
        return self.text
    def get_url(self):
        return 'question/%s' % self.question.id
