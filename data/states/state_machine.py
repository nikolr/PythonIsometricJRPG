from collections import deque
from data.states.state import State

class StateMachine:
    """Keeps track of current state within a scene and changes them. Passes the current state to the scene"""
    def __init__(self, initial_state: State) -> None:
        self.current_state = initial_state
        self.current_state.enter()
        # self.state_queue = deque()
        # self.state_queue.append(self.current_state)

    def change_state(self, new_state: State):
        self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

