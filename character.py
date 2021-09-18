from attribute_modifier import AttributeModType, AttributeModifier
from attribute_id import AttributeId
from sprite import Sprite
from stat_collection import StatCollection
from ability import Ability

class Character:

    def __init__(self, name: str, stat_collection: StatCollection, sprite: Sprite, counter = 10, abilities: list[Ability] = []):
        self.name = name
        self.stat_collection = stat_collection
        self.sprite = sprite
        self.counter = counter
        self.abilities = abilities
        self.alive = True
    

    def take_damage(self, damage: float):
        dmg = AttributeModifier(AttributeModType.FLAT, AttributeId.HP, damage, 1)
        self.stat_collection.get_attribute(AttributeId.HP).add_modifier(dmg)

    def gain_ability(self, ability: Ability):
        self.abilities.append(ability)

    def print_info(self):
        print(f"Name: {self.name}")
        self.stat_collection.print_stats()
    