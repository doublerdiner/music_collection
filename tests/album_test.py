import unittest
from models.album import Album
from models.artist import Artist

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.artist_1 = Artist("Talking Heads")
        self.album_1 = Album("Speaking in Tongues", "New Wave", self.artist_1)

    def test_album_has_a_name(self):
        self.assertEqual("Speaking in Tongues", self.album_1.name)

    def test_album_has_a_genre(self):
        self.assertEqual("New Wave", self.album_1.genre) 

    def test_album_has_an_artist(self):
        self.assertEqual(self.artist_1, self.album_1.artist)
        self.assertEqual(self.artist_1.name, self.album_1.artist.name)