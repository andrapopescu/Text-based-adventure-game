from room import Room
from character import Enemy, Friend

kitchen = Room('Kitchen')
kitchen.set_description('This is my kitchen')

living_room = Room('Living Room')
living_room.set_description('This is my living room')

bathroom = Room('Bathroom')
bathroom.set_description('This is my bathroom')

kitchen.link_rooms(living_room, 'east')
living_room.link_rooms(kitchen, 'west')
kitchen.link_rooms(bathroom, 'south')
bathroom.link_rooms(kitchen, 'north')

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('You do realize you are trying to talk to zombie, right?')
dave.set_weakness('dab')
living_room.set_character(dave)

emily = Enemy('Emily', "A friendly bee (But she's still your enemy. What did you do to upset her?)")
emily.set_conversation("Beep beep I'm a sheep. I said beep beep I'm a sheep.")
emily.set_weakness('honey')
emily.set_gift('my heart')
bathroom.set_character(emily)

jamie = Friend('Jamie', 'Pigeon')
jamie.set_conversation('I am in denial about being a pigeon ... ')
kitchen.set_character(jamie)

current_room = kitchen
alive = True
while alive:
    print('\n')
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant:
        inhabitant.describe()
    command = input('> ')
    if command in ['north', 'south', 'east', 'west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        if inhabitant:
            inhabitant.talk()
        else:
            print('Yeah, I bet you will get a reply from an empty room.')
    elif command == 'fight':
        if inhabitant:
            print('What will you fight with?')
            weapon = input('> ')
            if not inhabitant.fight(weapon):
                alive = False
        else:
            print("There is no one here to fight with. Did you even read the room's description?")
    elif command == 'befriend':
        if inhabitant:
            print('What do you bring as a gift?')
            gift = input('> ')
            inhabitant.become_friend(gift)
        else:
            print('I am about to point out the obvious here, but here it goes: you are alone in this room!')
    elif command == 'hug':
        if inhabitant:
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
            else:
                print('Smart! Very smart! Trying to hug an enemy. You could be stabbed!')
        else:
            print('Yeah, sometimes I like to try and get hugs from my favourite wall too.')
    else:
        print('Are you feeling alright? What are you trying to type?')
