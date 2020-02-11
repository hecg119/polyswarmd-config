import pytest
from polyswarmdconfig.consul import Consul, ConsulClient
from polyswarmdconfig.exceptions import MissingConfigValueError


def test_consul_uri_not_set():
    config = {}
    with pytest.raises(MissingConfigValueError):
        Consul.from_dict(config)


def test_consul_uri_set():
    config = {
        'uri': 'http://consul:8500'
    }
    consul = Consul.from_dict(config)
    assert consul.client is not None
    assert consul.token is None
    assert isinstance(consul.client, ConsulClient)
    assert consul.client.token is None


def test_consul_token_set():
    config = {
        'uri': 'http://consul:8500',
        'token': 'test-token'
    }
    consul = Consul.from_dict(config)
    assert consul.client is not None
    assert consul.token == 'test-token'
    assert consul.client.token == 'test-token'
