import time


# TODO: calculate the number of seconds based on how long the message is
def print_sleep(message, seconds=0):
    print(message)
    time.sleep(seconds)


def instructions(beginning=True):
    if beginning:
        print_sleep('Do you seriously have nothing better to do? You woke me up!', 2)
        print_sleep('Ummm ... ', 2)
        print_sleep('Still waiting for an excuse ... ', 1)
        print_sleep('Ungreatful being.', 1)
        print_sleep('Welcome!', 1)
        print_sleep('To this magical world of ... whatever the developer had in mind at the time ...', 3)
        print_sleep('I will be your guide.', 2)
        print_sleep('You will start the game in a random room (if the developer could even be bothered to implement this).', 4)
        print_sleep('If you want to go in a different room, just let me know what direction that`s in.', 3)
        print_sleep('You might encounter other creatures along the way.', 3)
        print_sleep('I will make sure to let you know if somebody is in the room.', 3)

    print_sleep('You can talk to them by typing `talk` (duh ... )', 3)
    print_sleep('You can fight them by typing `fight` (duh ... )', 3)
    print_sleep('You can befriend them by typing `befriend` (duh ... )', 3)
    print_sleep('You can hug them by typing `hug` (duh ... )', 3)

    if not beginning:
        print_sleep('Some are friends, some are enemies. Just type `friend?` to find out.', 3)
        print_sleep('If you want to go in a different room, just let me know what direction that`s in.', 3)
        print_sleep('I won`t bother tell you about the `help` command as you obviously know about it.', 5)
    else:
        print_sleep('Some are friends, some are enemies. If you want to know what they are, just ask me.', 4)
        print_sleep('By typing ... ', 2)
        print_sleep('???', 2)
        print_sleep('`friend?`', 0.5)
        print_sleep('Duh ... ', 1)

    if beginning:
        print_sleep('Now ....', 1)
        print_sleep('Don`t die! I have to clean the mess afterwards and I don`t like it.', 3)
        print_sleep('Loading ...', 5)
        print_sleep('Oh yeah! I almost forgot!', 1)
        print_sleep('If you don`t remember these simple instructions, just type:', 3)
        print_sleep('`Help! O mighty voice in my head!`', 2)
        print_sleep('Or you know, something like: ', 2)
        print_sleep('`I`m useless and I need help.`', 2)
        print_sleep('With capitals, punctuation and all that.', 4)
        print_sleep('Or I guess this will do:', 2)
        print_sleep('`help`', 3)