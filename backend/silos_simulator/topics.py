from dataclasses import dataclass


@dataclass
class PublishTopics:
    """Topics for the simulator to publish to."""
    def __init__(self, silos_id: str, slung: str):
        self.topic: str = f't/simulator/silos/{silos_id}/measurements/{slung}'


@dataclass
class SubscribeTopics:
    """Topics for the simulator to subscribe to."""
    def __init__(self, silos_id: str):
        self.fill: str = f't/simulator/silos/{silos_id}/command/fill'
        self.empty: str = f't/simulator/silos/{silos_id}/command/empty'
        self.idle: str = f't/simulator/silos/{silos_id}/command/idle'
        self.kill: str = f't/simulator/silos/{silos_id}/command/kill'

    def __iter__(self):
        return iter([self.fill, self.empty, self.idle, self.kill])


@dataclass
class Topics:
    """Topics for the simulator to publish and subscribe to."""
    publish: PublishTopics
    subscribe: SubscribeTopics

    def __init__(self, silos_id: str, slung: str):
        self.publish: PublishTopics = PublishTopics(silos_id, slung)
        self.subscribe: SubscribeTopics = SubscribeTopics(silos_id)
