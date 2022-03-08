from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=50)
    ans1 = models.CharField(max_length=50)
    ans2 = models.CharField(max_length=50)


class UserIsVote(models.Model):
    id = models.IntegerField(primary_key=True)
    choice = models.CharField(max_length=100)



