from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    description = models.CharField('Description',
                                   max_length=1000, blank=True,
                                   help_text='simple description')

    def __str__(self):
        return self.title
