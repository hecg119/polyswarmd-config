import dataclasses

from kafka import KafkaProducer
from typing import Optional

from polyswarmdconfig.config import Config


@dataclasses.dataclass
class Kafka(Config):
    brokers: Optional[list] = dataclasses.field(default_factory=list)
    producer: Optional[KafkaProducer] = dataclasses.field(init=False, default=None)

    def __post_init__(self):

        if self.brokers:
            self.producer = KafkaProducer(bootstrap_servers=self.brokers)
