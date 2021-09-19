from director import Director


class State():
    def __init__(self, director: Director) -> None:
        self.director = director
        self.prev_state = None


    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

class BattleSetup(State):
    
    def enter(self):
        pass
        #Load sprites 
        #Load map
        #Place sprites in starting tiles

    def exit(self):
        pass

    