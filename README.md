# Network Discovery Toolkit
**NOTE:** This is very much a work in progress

## Initial Goals
Take a known input list of devices connect to each device and gather device information including:
* hostname
* hardware model
* inventory components
* software version
* interace information
  * interfacfce #'s
  * IP / subnet
  * vlan tagging (if configured)
  * status (up/down)

Check CDP Neighbours look for any other Cisco devices not already in known inventory list

## Usage:
1. add list of known devices to nornir_inventory.py
2. create a "secrets.yaml" file with:
    ```yaml
    ---
    defaults:
    username: (username)
    password: (password))
    ```
3. output will be saved in a file per device in json format

## TODO items
* finish initial goals
* find an easier input method for inventory (maybe look at SimpleInventory instead of building custom inventory class)
* define next steps