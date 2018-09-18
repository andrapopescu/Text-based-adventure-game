class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.gift = 'Way too much gold'

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def set_gift(self, gift):
        self.gift = gift

    def get_gift(self):
        return self.gift

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print('You killed ' + self.name + ' with the ' +  combat_item + '. You monster!')
            return True
        else:
            print(self.name + ' completely obliterated you. Step up your game!')
            return False

    def become_friend(self, gift):
        if self.gift == 'Way too much gold':
            print("You cannot be friends with " + self.name + ". You do remember you destroyed this lovely human being's life, right?")
        elif self.gift == gift:
            print('Congrats! You made a friend. We all know you need more of those.')
        else:
            print('If you actually listened to what people say, you would now know what to bring as a gift.')

    def send_to_sleep(self):
        return

    def steal(self):
        return


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print("You got a hug from " + self.name + ". Now that's an achievement right there!")
