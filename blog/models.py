from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blog(models.Model):

    title = models.CharField(max_length = 30)
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.title
