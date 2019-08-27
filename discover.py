#!/usr/bin/env python
"""
purpose:
Discover device information based on list of known devices
use CDP and LLDP do identify devices not in the known lost

author: Denis Pointer
"""
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
import json


# need to filter information down a bit to just gather information of interest
def gather_info(task):
    """
    TODO add description....
    """

    # default command list:
    command_list = [
        "show version",
        "show ip interface brief",
        "show cdp neighbors detail",
        "show running-config",
    ]
    # gather information for each command in the list
    output = {}
    # for command in command_list:
    for command in command_list:
        results = task.run(
            netmiko_send_command, command_string=command, use_textfsm=True
        )
        output[command] = results.result
    output_json = json.dumps(output, indent=4)
    with open(f"outputs/{task.host.name}.txt", "w") as f:
        f.write(output_json)


# more flexible, but overly confusing version...
# maybe find a better way
# perhaps a class for the commands instead of weird nested dict
# possibly just turb idea...going down a weird rabbit hole here
def gather_info_dict(task):
    """
    TODO add description....
    """

    # default command list:
    command_dict = {
        "show version": {"yaml_name": "version"},
        "show ip interface brief": {"yaml_name": "ip_int_brief"},
        "show running-config": {"yaml_ext": "config"},
    }

    # gather information for each command in the list
    output = {}

    for command in command_dict.keys():
        results = task.run(
            netmiko_send_command, command_string=command, use_textfsm=True
        )
        if command_dict[command].get("yaml_name"):
            output[command_dict[command].get("yaml_name")] = results.result
        if command_dict[command].get("yaml_ext"):
            filename = (
                f"outputs/{task.host.name}-"
                f"{command_dict[command].get('yaml_ext')}.txt"
            )
            with open(filename, "w") as f:
                f.write(results.result)
    output_json = json.dumps(output, indent=4)
    with open(f"outputs/{task.host.name}.txt", "w") as f:
        f.write(output_json)


# Initialize nornir
nr = InitNornir(config_file="nornir.yaml")

# filter inventory based on Site name
targets = nr.filter(site="GNS3")

# run custom task
targets.run(gather_info)
