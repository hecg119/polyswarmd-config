import pytest
from polyswarmdconfig.exceptions import MissingConfigValueError
from polyswarmdconfig.profiler import Profiler


def test_enabled_no_uri():
    config = {
        'enabled': True
    }
    with pytest.raises(ValueError):
        Profiler.from_dict(config)


def test_not_enabled_with_uri():
    config = {
        'enabled': False,
        'db_uri': 'http://db_uri:5432'

    }
    profiler = Profiler.from_dict(config)
    assert not profiler.enabled
    assert profiler.db_uri == 'http://db_uri:5432'


def test_enabled_with_uri():
    config = {
        'enabled': True,
        'db_uri': 'http://db_uri:5432'
    }
    profiler = Profiler.from_dict(config)
    assert profiler.enabled
    assert profiler.db_uri == 'http://db_uri:5432'
