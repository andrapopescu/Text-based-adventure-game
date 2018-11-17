from character import Character
from room import Room


def setup_characters():
    return {
        'jim': Character(
            is_friend=False,
            name='Jim',
            description='A smelly zombie',
            conversation='You do realize you are trying to talk to zombie, right?',
            weakness='dab',
        ),
        'emily': Character(
            is_friend=False,
            name='Emily',
            description='A friendly bee (But she is still your enemy. What did you do to upset her?)',
            conversation='Beep beep I`m a sheep. I said beep beep I`m a sheep.',
            weakness='honey',
            gift='a heart',
        ),
        'jamie': Character(
            is_friend=True,
            name='Jamie',
            description='Pigeon',
            conversation='I`m in denial about being a pigeon ... ',
        ),
    }


def setup_rooms():

    characters = setup_characters()

    rooms_info = {
        'kitchen': {
            'description': 'This is my kitchen.',
            'linked-rooms': (('living-room', 'east'), ('bathroom', 'south')),
            'characters': ('jamie',),
        },
        'living-room': {
            'description': 'This is my living room.',
            'linked-rooms': (('kitchen', 'west'),),
            'characters': ('jim',),
        },
        'bathroom': {
            'description': 'This is my bathroom.',
            'linked-rooms': (('kitchen', 'north'),),
            'characters': ('emily',),
        },
    }

    rooms = {name: Room(name) for name in rooms_info}
    for name, room in rooms.items():
        room.set_description(rooms_info[name]['description'])
        for character_name in rooms_info[name]['characters']:
            room.set_character(characters[character_name])
        for linked_room, direction in rooms_info[name]['linked-rooms']:
            room.link_rooms(rooms[linked_room], direction)

    return rooms


def get_initial_room():
    rooms = setup_rooms()
    return rooms['kitchen']
