from django.db import models


class Player(models.Model):
    #rank = models.IntegerField()
    pseudo = models.CharField(max_length=200)
    score = models.IntegerField()
    time = models.DateTimeField()

