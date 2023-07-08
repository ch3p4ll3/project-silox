from dataclasses import dataclass, field
from string import Template


@dataclass
class PublishTopics:
    """Topics for the simulator to publish to."""
    topic: Template = Template('t/simulator/silos/${silos_id}/measurements/${slug}')


@dataclass
class SubscribeTopics:
    """Topics for the simulator to subscribe to."""
    fill: Template = Template('t/simulator/silos/${silos_id}/command/fill')
    empty: Template = Template('t/simulator/silos/${silos_id}/command/empty')
    idle: Template = Template('t/simulator/silos/${silos_id}/command/idle')
    kill: Template = Template('t/simulator/silos/${silos_id}/command/kill')
    start_simulation: Template = Template('t/simulator/silos/${silos_id}/command/start')
    stop_simulation: Template = Template('t/simulator/silos/${silos_id}/command/stop')
    commands: Template = Template('t/simulator/silos/${silos_id}/command/#')

    def __iter__(self):
        return iter([self.fill, self.empty, self.idle, self.kill, self.stop_simulation, self.start_simulation])


class Topics:
    """Topics for the simulator to publish and subscribe to."""
    publish: PublishTopics = PublishTopics()
    subscribe: SubscribeTopics = SubscribeTopics()
