from scene import Scene


class SceneHome(Scene):
    """ Welcome screen of the game, the first one to be loaded."""
 
    def __init__(self, director):
        Scene.__init__(self, director)
 
    def on_update(self):
        print(f"{self.__str__()} update")
        pass
 
    def on_event(self):
        pass
 
    def on_draw(self, screen):
        pass