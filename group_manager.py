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
        self.character_queue = deque()
        self.current_counters = [None] * len(participants)
        self.counter_history = [None] * len(participants)
        # self.current_character = None
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
                for a in self.participants:
                    print(f"{a.name} {a.counter}")
                self.tick_and_add_to_queue(self.participants)
        self.counter_history.clear()
        for i in range(len(self.participants)):
            self.participants[i].counter = self.current_counters[i]
            self.counter_history.append(self.current_counters[i])
            i += 1
        self.print_queue()

    def tick_and_add_to_queue(self, part: list[Character]):
        for character in part:
            if self.tick(character):
                self.character_queue.append(character)
                print(f"Added {character} to character_queue")
                if self.step_indicator == False and self.first_reset_indicator == True:
                    for i in range(len(part)):
                        self.current_counters[i] = part[i].counter
                        i += 1
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
        return self.character_queue.popleft()

    def print_queue(self):
        print("Current character_queue: ")
        for char in self.character_queue:
            print(char, end=", ")
            print(char.counter)