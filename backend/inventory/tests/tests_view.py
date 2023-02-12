"""Test for Views and Serializers logic"""
import logging

from faker import Faker

from inventory.models import Game
from inventory.tests.tests_setup import TestSetUp

fake = Faker()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    filename='./tests.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

class GameViewSetTestCase(TestSetUp):
    """Class to define basic CRUD tests on views"""
    def test_game_create(self):
        """Try to create a single game on database"""
        logger.info('Test GameViewSetTestCase - test_game_create')
        
        try:
            response = self.client.post(self.game_detail_url, self.game, format='json')
            
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['name'], self.game['name'])

            logger.info('Test GameViewSetTestCase - test_game_create - OK')

        except Exception as exc:
            logger.error(f'Test GameViewSetTestCase - test_game_create - {exc}')
            raise exc

    def test_game_list(self):
        """Try to list all games from database"""
        logger.info('Test GameViewSetTestCase - test_game_list')
        try:
            response = self.client.get(self.games_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['count'], 1)
            self.assertEqual(response.data['results'][0]['name'], self.game['name'])

            logger.info('Test GameViewSetTestCase - test_game_list - OK')

        except Exception as exc:
            logger.error(f'Test GameViewSetTestCase - test_game_list - {exc}')
            raise exc

    def test_game_detail(self):
        """Try to get a single game from database"""
        logger.info('Test GameViewSetTestCase - test_game_detail')
        try:
            response = self.client.get('/games/{self.game_id}/')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['id'], self.game['id'])
            self.assertEqual(response.data['name'], self.game['name'])

            logger.info('Test GameViewSetTestCase - test_game_detail - OK')

        except Exception as exc:
            logger.error(f'Test GameViewSetTestCase - test_game_detail - {exc}')
            raise exc

    def test_game_update(self):
        """Try to update a single game from database"""
        logger.info('Test GameViewSetTestCase - test_game_update')
        
        try:
            response = self.client.put('/games/{self.game_id}/', self.game, format='json')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['name'], self.game['name'])

            logger.info('Test GameViewSetTestCase - test_game_update - OK')

        except Exception as exc:
            logger.error(f'Test GameViewSetTestCase - test_game_update - {exc}')
            raise exc

    def test_game_delete(self):
        """Try to delete a single game from database"""
        logger.info('Test GameViewSetTestCase - test_game_delete')
        try:
            response = self.client.delete('/games/{self.game.id}/')

            self.assertEqual(response.status_code, 204)
            self.assertFalse(Game.objects.filter(id=self.game.id).exists())

            logger.info('Test GameViewSetTestCase - test_game_delete - OK')

        except Exception as exc:
            logger.error(f'Test GameViewSetTestCase - test_game_delete - {exc}')
            raise exc

    def test_game_get_by_genre(self):
        """Try to get games by genre from database"""
        logger.info('Test GameViewSetTestCase - test_game_get_by_genre')
        try:
            response = self.client.get('/games/genre/{self.game.genre}/')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['count'], 1)
            self.assertEqual(response.data['results'][0]['name'], self.game.name)

            logger.info('Test GameViewSetTestCase - test_game_get_by_genre - OK')

        except Exception as exc:
            logger.error(f'Test GameViewSetTestCase - test_game_get_by_genre - {exc}')
            raise exc
        