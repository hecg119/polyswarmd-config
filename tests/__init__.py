import dataclasses

from polyswarmdconfig.artifact import Artifact
from polyswarmdconfig.artifactclient import AbstractArtifactServiceClient
from polyswarmdconfig.auth import Auth
from polyswarmdconfig.config import Config
from polyswarmdconfig.consul import Consul
from polyswarmdconfig.redis import Redis


class TestArtifactServiceClient(AbstractArtifactServiceClient):
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
    enabled: bool = True
    path: str = ''
    number: int = 0


@dataclasses.dataclass
class SubConfigTest(Config):
    artifact: Artifact
    auth: Auth
    redis: Redis
    consul: Consul
    enabled: bool = True
    path: str = ''
    number: int = 0
