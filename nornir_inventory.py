#!/usr/bin/env python
"""
Author: Denis Pointer
Purpose: A framework for a custom Nornir Inventory Plugin
"""

from nornir.core.deserializer.inventory import Inventory
import yaml


class MyInventory(Inventory):
    def __init__(self, **kwargs):
        # TODO write the code...
        # code to get the data
        secrets_file = kwargs.pop("secrets_file", "secrets.yaml")
        with open(secrets_file) as f:
            secrets = yaml.safe_load(f)

        hosts = {
            "R1": {"hostname": "192.168.122.121", "data": {"site": "GNS3"}},
            "R2": {"hostname": "192.168.122.193", "data": {"site": "GNS3"}},
            "R3": {"hostname": "192.168.122.191", "data": {"site": "GNS3"}},
        }
        groups = {}
        defaults = {
            "platform": "ios",
            "username": secrets["defaults"]["username"],
            "password": secrets["defaults"]["password"],
        }

        # passing the data to the parent class so the data is
        # transformed into actual Host/Group objects
        # and set default data for all hosts
        super().__init__(
            hosts=hosts, groups=groups, defaults=defaults, **kwargs
        )
