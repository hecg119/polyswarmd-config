from polyswarmdconfig.auth import Auth


def test_auth_uri_set():
    config = {
        'uri': 'http://auth:80'
    }
    auth = Auth.from_dict(config)
    assert auth.uri == 'http://auth:80'
    assert auth.require_api_key


def test_auth_uri_not_set():
    config = {}
    auth = Auth.from_dict(config)
    assert auth.uri is None
    assert not auth.require_api_key
