class MessageBus:
    def __init__(self):
        self.messages = []

    def publish(self, message):
        self.messages.append(message)

    def consume(self):
        msgs = self.messages[:]
        self.messages = []
        return msgs