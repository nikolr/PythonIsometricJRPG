from attribute_modifier import AttributeModType, AttributeModifier
from attribute_id import AttributeId
from stat_collection import StatCollection


class Character:

    def __init__(self, name: str, stat_collection: StatCollection, sprite, counter = 10, innate_counter = 10):
        self.name = name
        self.stat_collection = stat_collection
        self.sprite = sprite
        self.counter = counter
        self.innate_counter = innate_counter
        self.abilities = []
        self.alive = True
    

    def take_damage(self, damage: float):
        dmg = AttributeModifier(AttributeModType.FLAT, AttributeId.HP, damage, 1)
        self.stat_collection.get_attribute(AttributeId.HP).add_modifier(dmg)



    def gain_ability(self, ability):
        self.abilities.append(ability)

    def __str__(self) -> str:
        return self.name

    def print_info(self):
        print(f"Name: {self.name}")
        self.stat_collection.print_stats()
    