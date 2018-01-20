from django.db import models


class Character(models.Model):
    char_name = models.CharField(max_length=200)
    player_name = models.CharField(max_length=200)
    health = models.IntegerField(default=1)
    max_health = models.IntegerField(default=1)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    proficiencies = models.CharField(max_length=1000, default='[]')


