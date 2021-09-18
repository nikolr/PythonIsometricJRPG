from state import State

class StateMachine:
    """Keeps track of current state within a scene and changes them. Passes the current state to the scene"""
    def __init__(self, initial_state: State) -> None:
        self.current_state = initial_state

    def change_state(self, new_state: State):
        self.current_state = new_state

