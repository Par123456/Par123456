#!/usr/bin/env python3
"""
Generate a random IPv6 address for a specified subnet
"""

from random import seed, getrandbits
from ipaddress import IPv6Network, IPv6Address

subnet = '2a09:4c0:3e0:f85::/64'

seed()
network = IPv6Network(subnet)
address = IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen))

print(address)
