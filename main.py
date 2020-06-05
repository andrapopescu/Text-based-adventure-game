from helpers import instructions, print_sleep
from setup import get_initial_room


def run():
    alive = True
    current_room = get_initial_room()
    print_sleep('Would you like to skip the instructions? (yes/no)')
    command = input('> ')
    if command == 'no':
        instructions()

    while alive:
        print_sleep('\n')
        current_room.get_details()
        inhabitant = current_room.get_character()
        if inhabitant:
            inhabitant.describe()
        command = input('> ')
        if command in {'help', 'Help! O mighty voice in my head!', 'I`m useless and I need help.'}:
            instructions(beginning=False)
        if command in {'north', 'south', 'east', 'west'}:
            current_room = current_room.move(command)
        elif command == 'friend?':
            if inhabitant:
                inhabitant.friendly()
            else:
                print_sleep('You`re asking if an empty room is a friend or an enemy?', 1)
                print_sleep('Right ...', 2)
                print_sleep('An enemy. Definitely an enemy.', 2)
        elif command == 'talk':
            if inhabitant:
                inhabitant.talk()
            else:
                print_sleep('Yeah, I bet you will get a reply from an empty room.', 3)
        # TODO: display some weapon options
        elif command == 'fight':
            if inhabitant:
                print_sleep('What will you fight with?')
                weapon = input('> ')
                if not inhabitant.fight(weapon):
                    alive = False
            else:
                print_sleep("There is no one here to fight with. Did you even read the room's description?", 4)
        # TODO: display some gift options
        elif command == 'befriend':
            if inhabitant:
                print_sleep('What do you bring as a gift?')
                gift = input('> ')
                inhabitant.befriend(gift)
            else:
                print_sleep('I am about to point out the obvious here, but here it goes: you are alone in this room!', 5)
        elif command == 'hug':
            if inhabitant:
                inhabitant.hug()
            else:
                print_sleep('Yeah, sometimes I like to try and get hugs from my favourite wall too.', 4)
        else:
            print_sleep('Are you feeling alright? What are you trying to type?', 2)


if __name__ == '__main__':
    run()
