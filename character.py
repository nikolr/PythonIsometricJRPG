from attribute_modifier import AttributeModType, AttributeModifier
from attribute_id import AttributeId
from stat_collection import StatCollection


class Character:

    def __init__(self, name: str, stat_collection: StatCollection, sprite, playable: bool = True, scene = None, base_action_points = 4, counter = 10, innate_counter = 10):
        
        self.name = name
        self.stat_collection = stat_collection
        self.sprite = sprite
        self.tile = self.sprite.tile
        self.playable = playable
        self.scene = scene
        self.base_action_points = base_action_points
        self.__action_points = base_action_points
        self.counter = counter
        self.innate_counter = innate_counter
        self.abilities = []
        self.alive = True
    
    @property
    def action_points(self):
        return self.__action_points
    
    @action_points.setter
    def action_points(self, action_points: int):
            
        if action_points < 0:
            #Spent too many actionpoints, do not allow action
            print("Spent too many actionpoints, do not allow action")
            self.__action_points = self.__action_points
        if action_points == 0:
            print("No ap left")
        self.__action_points = action_points

    # MAKE THIS NEXT
    def take_damage(self, damage: float):
        if self.alive == True:
            dmg = AttributeModifier(AttributeModType.FLAT, AttributeId.HP, -damage, 1)
            self.stat_collection.get_attribute(AttributeId.HP).add_modifier(dmg)
            if self.stat_collection.get_attribute(AttributeId.HP).value <= 0:
                self.stat_collection.get_attribute(AttributeId.HP).remove_all_modifiers()
                self.stat_collection.get_attribute(AttributeId.HP).value = 0
                self.alive = False
                self.scene.group_manager.dead_character_indicator = True
                print(f"Character {self.name} is dead!")

    def can_take_action(self, ability):
        """Return True if action points >= 0 after action"""
        if self.__action_points >= ability.ap_cost:
            return True
        else:
            return False


    def gain_ability(self, ability):
        self.abilities.append(ability)
        # ability.user = self
    
    def get_attribute_value(self, attributeid: AttributeId):
        return self.stat_collection.get_attribute(attributeid).value

    def act(self):
        pass

    def __str__(self) -> str:
        return self.name

    def print_info(self):
        print(f"Name: {self.name}")
        self.stat_collection.print_stats()
    