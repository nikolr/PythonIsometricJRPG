from stat_id import StatId
from stat_modifier import StatModType, StatModifier

class Attribute:

    def __init__(self, stat_id: StatId, base_value: float, stat_name: str, stat_description: str):
        self.stat_id = stat_id
        self.base_value = base_value
        self.stat_name = stat_name
        self.stat_description = stat_description
        self.stat_modifiers = []
        self.need_to_calculate = True

    @property
    def value(self):
        if self.need_to_calculate == True:
            self.__value = self.calculate_final_value()
            self.need_to_calculate = False
        return self.__value

    # @value.setter
    # def rekisteritunnus(self, tunnus):
    #     if Rekisteriote.rekisteritunnus_kelpaa(tunnus):
    #         self.__rekisteritunnus = tunnus
    #     else:
    #         raise ValueError("Rekisteritunnus ei kelpaa")

    def add_modifier(self, mod: StatModifier):
        """Adds a stat modifier to stat_modifiers list and sorts it by mod.order. Sets need_to_calculate to true"""
        self.stat_modifiers.append(mod)
        self.stat_modifiers.sort(key = lambda x: x.order)

    def remove_modifier(self, mod: StatModifier):
        """Removes the mod from stat_modifiers. Sets need_to_calculate to true"""
        self.stat_modifiers.remove(mod)

    def remove_all_modifiers(self):
        self.stat_modifiers.clear()
    
    def remove_all_source_modifiers(self, source) -> bool:
        """Removes all modifiers associated with the source given as the argument"""
        for mod in self.stat_modifiers:
            if mod.source == source:
                self.remove_modifier(mod)
                return True
        return False

    def get_modifiers(self):
        for mod in self.stat_modifiers:
            print(mod.value)

    def calculate_final_value(self):
        final_value = self.base_value
        for mod in self.stat_modifiers:
            if mod.stat_mod_type == StatModType.FLAT:
                final_value += mod.value
                print(f"Added flat value {mod.value} ")
            if mod.stat_mod_type == StatModType.PERCENTMULTIPLY:
                final_value *= (1 + mod.value)
                print(f"Multiplied by {mod.value}")

        return final_value
    