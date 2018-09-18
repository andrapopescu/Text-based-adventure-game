class Room:

    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)

    def link_rooms(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print('----------------')
        self.describe()
        for direction, room in self.linked_rooms.items():
            print('The ' + room.get_name().lower() + ' is ' + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('You cannot go that way')
            return self
