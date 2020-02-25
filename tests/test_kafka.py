from polyswarmdconfig.kafka import Kafka
from kafka import KafkaProducer

from unittest.mock import patch, MagicMock


def test_kafka_producer_created():
    test_brokers = ['kafka:9092']
    with patch.object(KafkaProducer, '__init__', return_value=None) as mock_producer:
        config = {
            'brokers': test_brokers
        }
        Kafka.from_dict(config)
        mock_producer.assert_called_once_with(bootstrap_servers=test_brokers)


def test_kafka_producer_not_created():
    config = {}
    kafka = Kafka.from_dict(config)
    assert kafka.producer is None
