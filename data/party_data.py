

class PartyData:
    """Holds information regarding the player party. Initialized at the start of a run and updated after encounters or player menuing"""

    def __init__(self, party: list, inventory: list = []) -> None:
        """"""
        self.party = party

    def add_item_to_inventory(self):
        pass

    def add_perk_to_character(self):
        pass