from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name="owner", null=True, on_delete=models.CASCADE)

    # @classmethod
    # def add_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(
    #         current_user = current_user
    #     )
    #     friend.users.add(new_friend)

    # @classmethod
    # def remove_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(
    #         current_user = current_user
    #     )
    #     friend.users.remove(new_friend)

    # def __str__(self):
    #     return str(self.current_user)

class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=45)
    image = models.ImageField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)