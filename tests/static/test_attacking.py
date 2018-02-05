import unittest
import requests

from utils import TEST_INSTANCE, TestGameData


@unittest.skip("Skipping as snake currently doesn't attack. These could be implemented as improvements.")
class TestAttackLogic(unittest.TestCase):
    def test_head_to_head_bigger(self):
        """ attack in a head to head fashion """
        data = TestGameData()
        data.set_self([(5, 5), (5, 6), (5, 7)])
        data.add_enemy([(5, 4), (5, 3)])

        response = requests.post(TEST_INSTANCE,  json=data.data)
        self.assertEqual(response.json()['move'], 'up')

    def test_enemy_between_snake_wall(self):
        """ attack an enemy snake when it is between you and the wall """
        data = TestGameData()
        data.set_self([(1, 5), (1, 6), (1, 7)])
        data.add_enemy([(0, 7), (0, 8)])

        response = requests.post(TEST_INSTANCE,  json=data.data)
        self.assertEqual(response.json()['move'], 'left')

    def test_enemy_between_snake_wall_collision(self):
        """ attack an enemy with head collision when between you and the wall """
        data = TestGameData()
        data.set_self([(1, 5), (1, 6), (1, 7)])
        data.add_enemy([(0, 6), (0, 7)])

        response = requests.post(TEST_INSTANCE,  json=data.data)
        self.assertEqual(response.json()['move'], 'left')

    def test_enemy_between_snake_snake(self):
        """ attack an enemy snake when it is between you and another snake"""
        data = TestGameData()
        data.set_self([(3, 5), (3, 6), (3, 7)])
        data.add_enemy([(2, 7), (2, 8)])
        data.add_enemy([(1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4)])

        response = requests.post(TEST_INSTANCE,  json=data.data)
        self.assertEqual(response.json()['move'], 'left')

    def test_enemy_between_snake_snake_collision(self):
        """ attack an enemy snake when it is between you and another snake but is level (head on collision) """
        data = TestGameData()
        data.set_self([(3, 5), (3, 6), (3, 7)])
        data.add_enemy([(2, 6), (2, 7)])
        data.add_enemy([(1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4)])

        response = requests.post(TEST_INSTANCE,  json=data.data)
        self.assertEqual(response.json()['move'], 'left')