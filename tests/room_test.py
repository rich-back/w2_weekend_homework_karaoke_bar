import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(["Room One", "Room Two", "Room Three"])
        self.song_1 = Song("Crazy", "Gnarls Barkley")
        self.song_2 = Song("Nova", "Burial")
        self.guest_1 = Guest("Mar")
        self.guest_2 = Guest("Colette")
        self.guest_3 = Guest("James")


    def test_room_has_name(self):
        self.assertEqual("Room One", self.room.room_number[0])

    def test_can_add_song(self):
        self.room.add_song(self.song_1, self.room.room_number[0])
        self.assertEqual(1, self.room.songs_in_list())

    def test_can_add_guest(self):
        self.room.add_guest_to_room(self.guest_1, self.room.room_number[0])
        self.room.add_guest_to_room(self.guest_2, self.room.room_number[0])
        self.room.add_guest_to_room(self.guest_3, self.room.room_number[0])
        self.assertEqual(3, self.room.guests_in_list())

    def test_can_add_all_guests(self):
        self.room.add_guest_to_room(self.guest_1, self.room.room_number[0])
        self.room.add_guest_to_room(self.guest_2, self.room.room_number[0])
        self.room.add_guest_to_room(self.guest_3, self.room.room_number[0])
        self.assertEqual(3, self.room.guests_in_list())

    def test_can_remove_guests(self):
        self.room.add_guest_to_room(self.guest_1, self.room.room_number[0])
        self.room.add_guest_to_room(self.guest_2, self.room.room_number[0])
        self.room.add_guest_to_room(self.guest_3, self.room.room_number[0])
        self.room.remove_guest_from_room(self.guest_1, self.room.room_number[0])
        self.assertEqual(2, self.room.guests_in_list())


   