class Room:
    def __init__(self, enemies):
        self.enemies_list = enemies
        self.rooms_list = self._initialize_rooms()
        self.room_number = 1
        self.room = self.rooms_list[self.room_number]

    def _initialize_rooms(self):
        list_of_rooms = []
        for i in range(2):
            enemies = self.enemies_list
            if i == 0:
                enemies = self.enemies_list[i]
            background = f"background_{i}"
            room = {"background": background,
                    "enemies": enemies
                    }
            list_of_rooms.append(room)
        return list_of_rooms

    def next_room(self):
        self.room_number += 1
