from character import Character
from collections import deque
from attribute import Attribute
from attribute_modifier import AttributeModType, AttributeModifier
from stat_collection import StatCollection
from attribute_id import AttributeId

class GroupManager:
    """Keeps track of character groups during battle"""
    def __init__(self, participants: list[Character]) -> None:       
        self.participants = participants
        self.player_party = []
        self.active_player_party = []
        self.player_party_is_empty_indicator = False
        self.enemy_party = []
        self.active_enemy_party = []
        self.enemy_party_is_empty_indicator = False

        self.dead_character_indicator = False

        for p in self.participants:
            if p.playable == True:
                self.player_party.append(p)
                self.active_player_party.append(p)
            else:
                self.enemy_party.append(p)
                self.active_enemy_party.append(p)
        self.character_queue = deque()
        self.current_counters = [None] * len(participants)
        self.counter_history = [None] * len(participants)
        # self.current_counters = []
        # self.counter_history = []
        
        self.step_indicator = False
        self.reset = False
        self.first_reset_indicator = False
    #Define functions for manipulating queue
    def determine_turn_queue(self):
        self.character_queue.clear()
        self.step_indicator = False
        self.first_reset_indicator = False
        if len(self.character_queue) >= 10:
            print("Multiple characters ticked to 0 on the same iteration") 
        else:
            while len(self.character_queue) < 10:
                # for a in self.participants:
                #     print(f"{a.name} {a.counter}")
                self.tick_and_add_to_queue(self.participants)
        self.counter_history.clear()
        # for i in range(0, len(self.participants)):
        #     self.participants[i].counter = self.current_counters[i]
        #     self.counter_history.append(self.current_counters[i])
        for i in range(0, len(self.participants)):
            self.participants[i].counter = self.current_counters[i]
            self.counter_history.append(self.current_counters[i])

    def tick_and_add_to_queue(self, part: list[Character]):
        for character in part:
            if self.tick(character):
                self.character_queue.append(character)
                # print(f"Added {character} to character_queue")
                if (self.step_indicator == False and self.first_reset_indicator == True):
                    for i in range(0, len(part)):
                        self.current_counters[i] = part[i].counter
                        # self.current_counters.append(part[i].counter)
                    self.step_indicator = True
        

    def tick(self, character: Character):
        self.reset = False
        character.counter -= 1
        if character.counter <= 0:
            character.counter = character.innate_counter
            self.reset = True
            self.first_reset_indicator = True
            return self.reset
        return self.reset

    def get_next_character(self):
        next_character = self.character_queue.popleft()
        if next_character.alive == True:
            return next_character
        else:
            return self.get_next_character()

    def remove_dead_characters(self):
        alive_participants = []
        for char in self.participants:
            if char.alive == True:
                alive_participants.append(char)
            if char.alive == False and char.playable == True:
                    self.active_player_party.remove(char)
            if char.alive == False and char.playable == False:
                    self.active_enemy_party.remove(char)
        self.participants = alive_participants
        self.dead_character_indicator = False
        print("Listening again for dead character flags")

    def player_party_is_empty(self):
        # if not self.player_party:
        #     return True
        # return False
        pass
    def enemy_party_is_empty(self):
        # if not self.enemy_party:
        #     return True
        # return False
        pass


    def get_list(self):
        l = []
        for c in self.character_queue:
            l.append(c.name)
        return l

    def print_queue(self):
        print("Current character_queue: ")
        for char in self.character_queue:
            print(char, end=", ")
            print(char.counter)