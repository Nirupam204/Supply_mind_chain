class AgentRegistry:
    def __init__(self):
        self.agents = {}

    def register(self, name, agent):
        self.agents[name] = agent

    def get_agent(self, name):
        return self.agents.get(name)