#!/usr/bin/env python

'''
Example custom dynamic inventory script for Ansible, in Python.
'''

import os
import sys
import argparse
import requests


try:
    import json
except ImportError:
    import simplejson as json


#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
# The department for which this script will return machines
# Make this the exact format as see on screen in the Inventory Management system
# for example 'Electrical Engineering' or 'Quality Assurance'

department_name = 'Software Engineering'

# this has to match the spelling in the inventory management system
# example: 'Windows' 'Linux' 'macOS'
machine_os = 'Linux'
ip_type = 'Static'

#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************
#****************************************************************************



class AnsibleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()
        self.department = department_name

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.machine_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory))


    # make a call to the inventory management API endpoint with the department parameter
    def get_hosts_from_api(self):
        url = 'http://appserver.example.com/tools/ittools/inventorymanagement/api/machinesindepartment'
        # send department parameter with the get request to the api
        payload = {'department': self.department}
        # send request to url
        r = requests.get(url, params=payload)
        return r.json()


   # Format the JSON that and return the inventory for a department.
    def machine_inventory(self):
        returned_json  = self.get_hosts_from_api()
        hosts = []
        for record in returned_json:
            if record['fields']['os'] == machine_os and record['fields']['ip_type'] == ip_type:
                hosts.append(record['fields']['machine_name'])
        return {
            'group': {
                'hosts': [host for host in hosts],
                'vars': {
                    'ansible_connection': 'ssh'
                }
            },
            '_meta': {
                'hostvars': {
                }
            }
        }


    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}


    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()


# Get the inventory.
AnsibleInventory()
