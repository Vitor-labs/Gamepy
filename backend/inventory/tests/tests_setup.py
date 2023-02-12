"""Setup for Views tests"""
import decimal
from faker import Faker

from rest_framework.test import APITestCase

from django.urls import reverse


class TestSetUp(APITestCase):
    """class to modelate setup the Views tests"""
    def setUp(self):
        self.games_url = reverse('inventory:game-list')
        self.game_detail_url = reverse('inventory:game-detail')
        self.game_by_genre_url = reverse('inventory:game-by-genre')
        self.fake = Faker()

        self.game : dict = {
            'id':self.fake.random_int(min=100, max=500),
            'name':self.fake.name(),

            'price':decimal.Decimal(self.fake.random_number(digits=3)),
            'score':self.fake.random_int(min=1, max=100),
            'publisher':self.fake.company(),
            'pub_date':self.fake.date_between(start_date="-10y", end_date="today"),

            'cover':self.fake.image_url(width=None, height=None),
            'summary':self.fake.text(),
            'genre':self.fake.name()
        }
        self.game_id = self.game['id']
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
        