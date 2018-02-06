import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_cutdown_user_wont_eat(self):
        data = utils.load_input('./input/users.json')
        self.assertEqual(data[0]['wont_eat'][0], 'fish')

    def test_cutdown_drinks(self):
        data = utils.load_input('./input/users.json')

        # check if every letter is lowercase
        for drink in data[0]['drinks']:
            for c in drink:
                # cheeky ignore spaces
                if c != ' ':
                    self.assertEqual(c.islower(), True)

    def test_cutdown_venues_food(self):
        data = utils.load_input('./input/venues.json')
        self.assertEqual(data[0]['food'][0], 'mexican')

    def test_cutdown_venues_drink(self):
        data = utils.load_input('./input/venues.json')

        # check if every letter is lowercase
        for drink in data[0]['drinks']:
            for c in drink:
                # cheeky ignore spaces
                if c != ' ':
                    self.assertEqual(c.islower(), True)

    def test_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as context:
            utils.load_input('foo.json')

