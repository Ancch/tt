from django.db import models
from django.utils.text import slugify

# Create your models here.
class TT(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Comment(models.Model):
    post = models.ForeignKey('board.TT', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()