import dataclasses

from polyswarmdconfig.artifact import Artifact
from polyswarmdconfig.artifactclient import AbstractArtifactServiceClient
from polyswarmdconfig.auth import Auth
from polyswarmdconfig.config import Config
from polyswarmdconfig.consul import Consul
from polyswarmdconfig.redis import Redis


class TestArtifactServiceClient(AbstractArtifactServiceClient):
    __test__ = False

    def __init__(self):
        super().__init__('', '')

    def add_artifacts(self, artifacts, session):
        pass

    def add_artifact(self, artifact, session, redis=None):
        pass

    def check_uri(self, uri):
        pass

    def details(self, identifier, index, session):
        pass

    def get_artifact(self, identifier, index, session, max_size=None, redis=None):
        pass

    def ls(self, identifier, session):
        pass

    def status(self, session):
        pass


@dataclasses.dataclass
class Test(Config):
    __test__ = False

    enabled: bool = True
    path: str = ''
    number: int = 0
    list_of_string: list = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class SubConfigTest(Config):
    __test__ = False

    artifact: Artifact
    auth: Auth
    redis: Redis
    consul: Consul
    enabled: bool = True
    path: str = ''
    number: int = 0
