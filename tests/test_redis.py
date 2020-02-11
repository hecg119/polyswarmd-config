from polyswarmdconfig.redis import Redis, RedisClient


def test_redis_client_created():
    config = {
        'uri': 'redis://redis:6379'
    }
    redis = Redis.from_dict(config)
    assert redis.client is not None
    assert isinstance(redis.client, RedisClient)


def test_redis_client_not_created():
    config = {}
    redis = Redis.from_dict(config)
    assert redis.client is None
