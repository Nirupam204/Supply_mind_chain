class StateManager:
    def __init__(self):
        self.state_history = []

    def update_state(self, state):
        self.state_history.append(state)

    def get_latest(self):
        return self.state_history[-1] if self.state_history else None