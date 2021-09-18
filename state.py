from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def handle(self):
        pass

class BattleSetup(State):
    
    def enter(self):
        pass
        #Load sprites 
        #Load map
        #Place sprites in starting tiles

    def exit(self):
        pass

    