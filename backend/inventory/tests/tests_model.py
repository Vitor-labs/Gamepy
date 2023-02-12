"""Tests for Game model"""
import decimal
from faker import Faker

from django.test import TestCase

from inventory.models import Game


fake = Faker()

class GameTestCase(TestCase):
    """Definition for CRUD tests in database"""
    def setUp(self): # Tested OK
        self.game = Game.objects.create(
            name=fake.name(),
            
            price=decimal.Decimal(fake.random_number(digits=3)),
            score=fake.random_int(min=1, max=100),
            publisher=fake.company(),
            pub_date=fake.date_between(start_date="-10y", end_date="today"),

            cover=fake.image_url(width=None, height=None),
            summary=fake.text(),
            genre=fake.name()
        )

    def test_game_creation(self): # Tested OK
        """Crud Test"""
        _str = f'{self.game.id}: {self.game.name}'
        self.assertIsInstance(self.game, Game)
        self.assertEqual(self.game.__str__(),_str)

    def test_game_list(self): # Tested OK
        """cRud Test"""
        games = Game.objects.all()
        self.assertTrue(len(games) > 0)

    def test_game_update(self): # Tested OK
        """crUd Test"""
        name = fake.name()
        self.game.name = name
        self.game.save()

        _str = f'{self.game.id}: {self.game.name}'
        self.assertEqual(self.game.__str__(),_str)

    def test_game_delete(self): # Tested OK
        """cruD Test"""
        self.game.delete()
        self.assertFalse(Game.objects.filter(id=self.game.id).exists())
        