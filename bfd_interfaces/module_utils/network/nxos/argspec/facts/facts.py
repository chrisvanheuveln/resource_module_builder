#
# -*- coding: utf-8 -*-
# Copyright 2019 Cisco and/or its affiliates.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the nxos facts module.
"""


class FactsArgs(object):  # pylint: disable=R0903
    """ The arg spec for the nxos facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        'bfd_interfaces',
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list'),
        'gather_network_resources': dict(choices=choices,
                                         type='list'),
    }
