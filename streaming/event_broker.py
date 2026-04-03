from collections import defaultdict
from datetime import datetime
import uuid


class EventBroker:
    def __init__(self):
        self.topics = defaultdict(list)
        self.subscribers = defaultdict(list)

    def publish(self, topic, producer, data):
        event = {
            "event_id": str(uuid.uuid4()),
            "topic": topic,
            "producer": producer,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data
        }

        self.topics[topic].append(event)

        for consumer in self.subscribers[topic]:
            consumer(event)

        return event

    def subscribe(self, topic, consumer_callback):
        self.subscribers[topic].append(consumer_callback)

    def get_topic_events(self, topic):
        return self.topics.get(topic, [])

    def replay_events(self, topic):
        return self.topics.get(topic, [])