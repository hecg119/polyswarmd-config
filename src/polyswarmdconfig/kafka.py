import dataclasses

from pykafka import KafkaClient
from typing import Optional

from polyswarmdconfig.config import Config


@dataclasses.dataclass
class Kafka(Config):
    brokers: Optional[str] = None
    use_greenlets: Optional[bool] = True
    client: Optional[KafkaClient] = dataclasses.field(init=False, default=None)

    def __post_init__(self):
        if self.brokers:
            self.client = KafkaClient(hosts=str.encode(self.brokers),
                                      use_greenlets=self.use_greenlets)
