from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


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
class Post(models.Model):
    visits_count = models.IntegerField()
    slug = AutoSlugField(populate_from='title')





