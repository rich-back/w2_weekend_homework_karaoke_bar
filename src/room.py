class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        
        self.song_list = []
        self.guest_list = []

    def songs_in_list(self):
        return len(self.song_list)
    
    def add_song(self, song, room_number):
        self.song_list.append(song)

    def guests_in_list(self):
        return len(self.guest_list)

    def add_guest_to_room(self, name, room_number):
        self.guest_list.append(name)

    def remove_guest_from_room(self, name, room_number):
        self.guest_list.remove(name)
