from collections import Counter

import pytest

from src.constants.resource import Resource
from src.models.resource_bundle import ResourceBundle


def test_single_resource():
    bundle = ResourceBundle(wood=1)
    assert bundle.resources == Counter({Resource.wood: 1})


def test_multiple_resources():
    bundle = ResourceBundle(wood=1, clay=2)
    assert bundle.resources == Counter({Resource.wood: 1, Resource.clay: 2})


def test_empty_bundle_is_falsy():
    bundle = ResourceBundle()
    assert bundle.resources == Counter()
    assert not bundle.resources


def test_missing_resource_defaults_to_zero():
    bundle = ResourceBundle(wood=1)
    assert bundle.resources[Resource.clay] == 0


def test_unknown_resource_name_raises():
    with pytest.raises(KeyError):
        ResourceBundle(unobtainium=1)


def test_bundles_can_be_combined():
    total = ResourceBundle(wood=1).resources + ResourceBundle(wood=2, clay=1).resources
    assert total == Counter({Resource.wood: 3, Resource.clay: 1})
