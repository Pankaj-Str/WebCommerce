from django.db import models

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=120, default='')
    description = models.TextField(help_text='Description', default='')

    def __str__(self):
        return self.name


