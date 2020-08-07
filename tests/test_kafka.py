from unittest.mock import patch

from polyswarmdconfig.kafka import Kafka

from pykafka import KafkaClient


def test_kafka_client_created():
    test_brokers = 'kafka1:9092, kafka2:9092'
    test_use_greenlets = True
    test_broker_version = '1.5.4'
    with patch.object(KafkaClient, '__init__', return_value=None) as mock_client:
        config = {
            'brokers': test_brokers,
            'use_geenlets': test_use_greenlets,
            'broker_version': test_broker_version
        }
        Kafka.from_dict(config)
        mock_client.assert_called_once_with(broker_version=test_broker_version, hosts=test_brokers, use_greenlets=test_use_greenlets)


def test_kafka_client_not_created():
    config = {}
    kafka = Kafka.from_dict(config)
    assert kafka.client is None
