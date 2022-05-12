#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

import json
from unittest.mock import Mock

import pytest

from lib.charms.osm_libs.v0.osm_config import OsmConfig


@pytest.fixture
def charm():
    charm = Mock()
    charm.config = {"osm-config": json.dumps({"v0": {}})}
    return charm


def test_osm_config_not_found(charm):
    charm.config = {}
    with pytest.raises(Exception) as e_info:
        OsmConfig(charm)
    assert str(e_info.value) == "config option osm-config not provided."


def test_osm_config_without_version(charm):
    charm.config = {"osm-config": "{}"}
    with pytest.raises(Exception) as e_info:
        OsmConfig(charm)
    assert str(e_info.value) == "version v0 not present in osm-config."


def test_osm_config_empty(charm):
    osm_config = OsmConfig(charm)
    assert osm_config.k8s.config == {}


def test_osm_config_with_k8s_services(charm):
    charm.config["osm-config"] = json.dumps(
        {
            "v0": {
                "k8s": {
                    "services": {
                        "openldap": {
                            "ip": ["1.1.1.1"],
                            "ports": {"openldap": {"port": 389, "protocol": "TCP"}},
                        }
                    }
                }
            }
        }
    )
    osm_config = OsmConfig(charm)
    openldap_service = osm_config.k8s.get_service("openldap")
    assert openldap_service.ip == "1.1.1.1"
    assert openldap_service.get_port("openldap") == 389
