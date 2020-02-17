import os
import pytest
from consul import Consul
from polyswarmdconfig.artifact import Artifact
from redis import Redis

from tests import Test, SubConfigTest, TestArtifactServiceClient


@pytest.fixture(autouse=True)
def test_env():
    original = os.environ
    os.environ = {}
    os.environ.update(original)
    yield
    os.environ = original


def test_fills_in_dict():
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_MODULE'] = "ipfs"
    config = {'artifact': {'library': {}}}
    SubConfigTest.overlay_environment(config)
    assert config == {'artifact': {'library': {'module': 'ipfs'}}}


def test_replaces_value():
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_MODULE'] = "ipfs"
    config = {}
    SubConfigTest.overlay_environment(config)
    assert config == {'artifact': {'library': {'module': 'ipfs'}}}


def test_does_not_change_other_values():
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_MODULE'] = "ipfs"
    config = {'artifact': {'library': {'module': 's3', 'class_name': 'IpfsServiceClient'}}}
    SubConfigTest.overlay_environment(config)
    assert config == {'artifact': {'library': {'module': 'ipfs', 'class_name': 'IpfsServiceClient'}}}


def test_replaces_value_with_dict():
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_MODULE'] = "ipfs"
    config = {'artifact': {'library': 'tests'}}
    SubConfigTest.overlay_environment(config)
    assert config == {'artifact': {'library': {'module': 'ipfs'}}}


def test_adds_entire_structure():
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_MODULE'] = "ipfs"
    config = {'enabled': True}
    SubConfigTest.overlay_environment(config)
    assert config == {'enabled': True, 'artifact': {'library': {'module': 'ipfs'}}}


def test_set_bool_value():
    os.environ['TEST_ENABLED'] = '1'
    config = {'enabled': False}
    test = Test.from_dict_and_environment(config)
    assert isinstance(test.enabled, bool)
    assert test.enabled


def test_set_int_value():
    os.environ['TEST_NUMBER'] = '10'
    config = {}
    test = Test.from_dict_and_environment(config)
    assert isinstance(test.number, int)
    assert test.number == 10


def test_set_str_value():
    os.environ['TEST_PATH'] = 'tests'
    config = {}
    test = Test.from_dict_and_environment(config)
    assert isinstance(test.path, str)
    assert test.path == 'tests'


def test_set_list_value():
    os.environ['TEST_LIST_OF_STRING'] = 'moe, larry, curly'
    config = {}
    test = Test.from_dict_and_environment(config)
    assert isinstance(test.list_of_string, list)
    assert test.list_of_string == ['moe', 'larry', 'curly']


def test_wipes_out_value():
    os.environ['TEST_ENABLED'] = ''
    config = {'enabled': True}
    test = Test.from_dict_and_environment(config)
    assert config == {'enabled': ''}
    assert not test.enabled


def test_set_multi_word_value():
    os.environ['SUBCONFIGTEST_ARTIFACT_MAX_SIZE'] = "10"
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_MODULE'] = "ipfs"
    os.environ['SUBCONFIGTEST_ARTIFACT_LIBRARY_CLASS_NAME'] = "IpfsServiceClient"
    config = {'artifact': {'library': {}}}
    SubConfigTest.overlay_environment(config)
    assert config == {
        'artifact': {
            "max_size": '10',
            'library': {
                'module': 'ipfs',
                'class_name': 'IpfsServiceClient'
            }
        }
    }


def test_fill_out_full_test():
    config = {
        'artifact': {
            'library': {
                'module': 'tests',
                'class_name': 'TestArtifactServiceClient'
            }
        },
        'auth': {
            'uri': 'http://auth:80'
        },
        'redis': {
            'uri': 'redis://redis:6379'
        },
        'consul': {
            'uri': 'http://consul:8500'
        },
    }
    test = SubConfigTest.from_dict(config)
    assert test.auth.uri is not None
    assert isinstance(test.redis.client, Redis)
    assert isinstance(test.artifact, Artifact)
    assert isinstance(test.artifact.library.client, TestArtifactServiceClient)
    assert isinstance(test.consul.client, Consul)
    assert test.enabled
    assert test.path == ''
    assert test.number == 0


def test_does_not_load_extra_values():
    config = {'extra_key': True}
    Test.from_dict(config)
