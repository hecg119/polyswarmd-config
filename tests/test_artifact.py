import pytest
from polyswarmdconfig.artifact import Library, Artifact, DEFAULT_FALLBACK_SIZE
from polyswarmdconfig.exceptions import MissingConfigValueError

from tests import TestArtifactServiceClient


def test_artifact_library_module_not_set():
    config = {
        'class_name': 'TestArtifactServiceClient',
        'args': []
    }
    with pytest.raises(MissingConfigValueError):
        Library.from_dict(config)


def test_artifact_library_class_name_not_set():
    config = {
        'module': 'tests',
        'args': []
    }
    with pytest.raises(MissingConfigValueError):
        Library.from_dict(config)


def test_artifact_library_args_no_set():
    config = {
        'module': 'tests',
        'class_name': 'TestArtifactServiceClient',
        'args': []
    }
    library = Library.from_dict(config)
    assert len(library.args) == 0
    assert isinstance(library.args, list)


def test_artifact_library_client_created():
    config = {
        'module': 'tests',
        'class_name': 'TestArtifactServiceClient',
        'args': []
    }
    library = Library.from_dict(config)
    assert library.module == 'tests'
    assert library.class_name == 'TestArtifactServiceClient'
    assert isinstance(library.args, list)
    assert library.client is not None
    assert isinstance(library.client, TestArtifactServiceClient)


config = {'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []}}


def test_artifact_library_not_set():
    config = {}
    with pytest.raises(MissingConfigValueError):
        Artifact.from_dict(config)


def test_artifact_library_set():
    config = {'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []}}
    artifact = Artifact.from_dict(config)
    assert isinstance(artifact.client, TestArtifactServiceClient)


def test_artifact_limit_set():
    config = {
        'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []},
        'limit': 1}
    artifact = Artifact.from_dict(config)
    assert artifact.limit == 1


def test_artifact_limit_not_set():
    config = {'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []}}
    artifact = Artifact.from_dict(config)
    assert artifact.limit == 256


def test_artifact_max_size_set():
    config = {
        'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []},
        'max_size': 1}
    artifact = Artifact.from_dict(config)
    assert artifact.max_size == 1


def test_artifact_max_size_not_set():
    config = {'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []}}
    artifact = Artifact.from_dict(config)
    assert artifact.max_size == DEFAULT_FALLBACK_SIZE


def test_artifact_fallback_max_size_set():
    config = {
        'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []},
        'fallback_max_size': 1}
    artifact = Artifact.from_dict(config)
    assert artifact.fallback_max_size == 1


def test_artifact_fallback_max_size_not_set():
    config = {'library': {'module': 'tests', 'class_name': 'TestArtifactServiceClient', 'args': []}}
    artifact = Artifact.from_dict(config)
    assert artifact.fallback_max_size == DEFAULT_FALLBACK_SIZE
