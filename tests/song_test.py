import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Innuendo", "Queen")

    def test_song_exists(self):
        self.assertEqual("Innuendo", self.song.title)
        self.assertEqual("Queen", self.song.artist)

    
