from helpers import print_sleep


class Character():

    def __init__(self, is_friend, name, description, conversation=None, weakness=None, gift=None):
        self.is_friend = is_friend
        self.name = name
        self.description = description
        self.conversation = conversation
        self.weakness = weakness
        self.gift = gift

    def describe(self):
        print_sleep(self.name + ' is here! ' + self.description, 2)

    def friendly(self):
        if self.is_friend:
            print_sleep('Well that`s a bit surprising ... You`re actually friends.', 2)
        else:
            print_sleep('Enemy. Of course. Not many people like you.', 2)

    def talk(self):
        if self.conversation is not None:
            print_sleep("[" + self.name + " says]: " + self.conversation, 2)
        else:
            print_sleep(self.name + " doesn't want to talk to you", 2)

    def fight(self, combat_item=None):
        if self.is_friend:
            print_sleep(self.name + ' is a friend. Why would you even try to fight?', 2)
            return True
        else:
            print_sleep(self.name + ' is ready to fight.', 2)
            print_sleep('Fighting ... ', 3)
            if combat_item == self.weakness:
                print_sleep('You won!? I was not expecting that...', 3)
                return True
            else:
                print('Are you even trying? You lost! Happy now?', 1)
                return False

    # TODO: mark a friend as enemy is you're trying to give them something they hate
    def befriend(self, gift):
        if self.is_friend:
            print_sleep('You`re already friends. Not sure why. But you are.', 3)
        else:
            if not self.gift:
                print_sleep("You cannot be friends with " + self.name +
                            ". You do remember you destroyed this lovely human being's life, right?", 5)
            elif self.gift == gift:
                print_sleep('Congrats! You made a friend. We all know you need more of those.', 3)
            else:
                print_sleep('That was definitely not the right gift.', 4)

    def hug(self):
        if self.is_friend:
            print_sleep("You got a hug from " + self.name + ". Now that's an achievement right there!", 4)
        else:
            print_sleep('Smart! Very smart! Trying to hug an enemy. You could be stabbed!', 4)
