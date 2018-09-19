from django.contrib.auth.models import User
from django.db import models



class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=45)
    image = models.ImageField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="liked_players")
    game = models.ManyToManyField('Game', blank=True, related_name="liked_games")
    #loop over "liked_games" when pulling to show all liked games