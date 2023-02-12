"""Models for inventory app"""
from django.db import models


class Game(models.Model):
    """Class to modelete a game instance"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.IntegerField()
    publisher = models.CharField(max_length=200)
    pub_date = models.DateField()

    class Tags(models.TextChoices):
        """Class for modeling the game Tags"""
        ACT = 'Action'
        SUS = 'Suspense'
        PUZ = 'Puzzle'
        MIS = 'Mistery'
        ADV = 'Adventury'
        __empty__ = '(Unknown)'

    cover = models.ImageField(upload_to='covers/', blank=True)
    summary = models.TextField(max_length=350, default="It's a game")
    genre = models.CharField(choices=Tags.choices, max_length=9)

    class Meta:
        """Game Table metadata"""
        db_table = 'Games'

    objects = models.Manager()

    def __str__(self):
        return f'{self.id}: {self.name}'
