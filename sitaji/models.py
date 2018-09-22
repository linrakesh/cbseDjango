from django.db import models
from django.urls import reverse


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length = 50)
    email = models.CharField(max_length= 100)
    intro = models.TextField(default="")
    image = models.FileField()

    def get_absolute_url(self):
    	return reverse('sitaji:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' - ' + self.fname