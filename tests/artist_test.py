import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist_1 = Artist("Talking Heads")
    
    def test_artist_has_name(self):
        self.assertEqual("Talking Heads", self.artist_1.name)