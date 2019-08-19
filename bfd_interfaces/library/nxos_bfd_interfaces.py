#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Cisco and/or its affiliates.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for nxos_bfd_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: bfd_interfaces
version_added: 2.9
short_description: 'Manages BFD attributes of nxos interfaces.'
description: 'Manages attributes of Bidirectional Forwarding Detection (BFD) on the interface.'
author: Chris Van Heuveln (@chrisvanheuveln)
notes:
options:
  config:
    description: The provided configuration
    type: list
    elements: dict
    suboptions:
      name:
        type: str
        description: The name of the interface.
      bfd:
        type: str
        description:
        - Enable/Disable Bidirectional Forwarding Detection (BFD) on the interface.
        choices:
        - enable
        - disable
      bfd_echo:
        type: str
        description:
        - Enable/Disable BFD Echo functionality on the interface.
        choices:
        - enable
        - disable
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted

- name: Configure interfaces
  bfd_interfaces:
    operation: deleted


# Using merged

- name: Configure interfaces
  bfd_interfaces:
    config:
      - name: Ethernet1/1
        bfd: enable
        bfd_echo: enable
      - name: Ethernet1/2
        bfd: disable
        bfd_echo: disable
    operation: merged


# Using overridden

- name: Configure interfaces
  myos_interfaces:
    config:
      - name: Ethernet1/1
        bfd: enable
        bfd_echo: enable
      - name: Ethernet1/2
        bfd: disable
        bfd_echo: disable
    operation: overridden


# Using replaced

- name: Configure interfaces
  nxos_interfaces:
    config:
      - name: Ethernet1/1
        bfd: enable
        bfd_echo: enable
      - name: Ethernet1/2
        bfd: disable
        bfd_echo: disable
    operation: replaced


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.nxos.argspec.bfd_interfaces.bfd_interfaces import Bfd_interfacesArgs
from ansible.module_utils.network.nxos.config.bfd_interfaces.bfd_interfaces import Bfd_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Bfd_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Bfd_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
