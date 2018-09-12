from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=45)
    image = models.ImageField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)