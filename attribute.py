from attribute_id import AttributeId
from attribute_modifier import AttributeModType, AttributeModifier

class Attribute:

    def __init__(self, attribute_id: AttributeId, base_value: float, attribute_name: str, attribute_description: str):
        self.attribute_id = attribute_id
        self.base_value = base_value
        self.attribute_name = attribute_name
        self.attribute_description = attribute_description
        self.attribute_modifiers = []
        self.need_to_calculate = True

    @property
    def value(self):
        if self.need_to_calculate == True:
            print("Calculated final value")
            self.__value = self.calculate_final_value()
            self.need_to_calculate = False
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value
        self.need_to_calculate = False

    def add_modifier(self, mod: AttributeModifier):
        """Adds a attribute modifier to attribute_modifiers list and sorts it by mod.order. Sets need_to_calculate to true"""
        print(f"Adding modifier {mod}")
        self.need_to_calculate = True
        self.attribute_modifiers.append(mod)
        self.attribute_modifiers.sort(key = lambda x: x.order)

    def remove_modifier(self, mod: AttributeModifier):
        """Removes the mod from attribute_modifiers. Sets need_to_calculate to true"""
        self.need_to_calculate = True
        self.attribute_modifiers.remove(mod)

    def remove_all_modifiers(self):
        self.need_to_calculate = True
        self.attribute_modifiers.clear()
    
    def remove_all_source_modifiers(self, source) -> bool:
        """Removes all modifiers associated with the source given as the argument"""
        self.need_to_calculate = True
        for mod in self.attribute_modifiers:
            if mod.source == source:
                self.remove_modifier(mod)
                return True
        return False

    def get_modifiers(self):
        for mod in self.attribute_modifiers:
            print(mod.value)

    def calculate_final_value(self):
        final_value = self.base_value
        for mod in self.attribute_modifiers:
            if mod.attribute_mod_type == AttributeModType.FLAT:
                final_value += mod.value
                print(f"Added flat value {mod.value} ")
            elif mod.attribute_mod_type == AttributeModType.PERCENTMULTIPLY:
                final_value *= (1 + mod.value)
                print(f"Multiplied by {mod.value}")
        print("Calculations complete")
        return final_value
    