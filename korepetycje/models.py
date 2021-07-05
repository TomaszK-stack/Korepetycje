from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.shortcuts import reverse

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname =models.CharField(max_length=200)
    subject = models.ManyToManyField(Subject, blank = True)

    def __str__(self):
        if self.name == "":
            return f"{self.user.username}"
        else:
            return f"{self.name} {self.surname}"
    def get_absolute_url(self):
        return reverse('korepetycje:detail', kwargs={'pk': self.pk})

class Post(models.Model):
    visits_count = models.IntegerField()






